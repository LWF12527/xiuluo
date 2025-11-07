import asyncio
import os
import random
import sys
import time

import aiohttp
from loguru import logger
from lxml import html

from async_custom_mysql_pool import DbManager

# Windows 平台兼容性设置
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

cmd = sys.argv
mod = 1
n = 0
if len(cmd) > 1:
    mod = int(cmd[1])
    n = int(cmd[2])

# 并发配置
MAX_WORKERS = 100
BATCH_SIZE = MAX_WORKERS * 200
RETRY_DELAY = 3

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "dnt": "1",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"141.0.7390.123\"",
    "sec-ch-ua-full-version-list": "\"Google Chrome\";v=\"141.0.7390.123\", \"Not?A_Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"141.0.7390.123\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"15.0.0\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}
cookies = {
    "privacy_2": "0",
    "privacy_3": "0",
    "privacy_4": "0",
    "privacy_verify": "1",
    "cf_clearance": "9OspfTJUwgBfX0ppwWljCvG4zhJBbYE6285VV8FZM6c-1762478537-1.2.1.1-biYo2Gen.10fZPTG222gkgikXyOEyKZEfgAGREcdleMYs6ampFTPaxehFV2jr9rIJmtAl3PPtyMSSOZquZs7XCTkac9wJ.khepFv0T4cD90zQJncpftnOipAcTUJDUQ9Gf2yqHZLfSxcE71Hb27ZQMygmIDHv3PLA8_PpPDLwd7ZBVgkAzQPa2GREwkxl5SE8v4PVRNu60QVuo21Wd84temPDiOG0recBRHD4PtC9Do",
    "EW4SITE": "ccl554rjlv88trqcd2ktlg9nsc",
    "SITEXSRF141": "qhp7n3buuccx8r8b248ptt32rj1wd6zj"
}

# 页面增量-请求-获取文章链接-获取下一页链接--请求-获取文章链接
add_url_list1_map = {
    "https://archyvas.lrp.lt/adamkus/sarasas15ee.html?nuo=1&kat=4&search=": "LT",
    "https://archyvas.lrp.lt/adamkus/en/sarasasdd13.html?nuo=1&kat=12&search=": "EN",
    "https://archyvas.lrp.lt/paksas/sarasas8710.html?kat=4": "LT",
    "https://archyvas.lrp.lt/paksas/en/sarasasdd13.html?nuo=1&kat=12&search=": "EN"
}

# 关键词增量年份--请求后-提取每年-请求-提取每个文章链接
add_url_list2_map = {
    "https://grybauskaite.lrp.lt/en/activities/speeches/6590/2009-11": "EN",
    "https://grybauskaite.lrp.lt/lt/prezidentes-veikla/kalbos/6588/2023-06": "LT"
}
# 页面增量3-同1
add_url_list3_map = {'https://archyvas.lrp.lt/adamkus3/en/activities/speeches/p15.html': "LT"}


async def fetch_page(url):
    """异步获取网页内容"""
    # 随机延迟防止请求过于频繁
    await asyncio.sleep(random.uniform(0.5, 1.2))

    # 使用 aiohttp 异步请求
    try:
        async with aiohttp.ClientSession(
                connector=aiohttp.TCPConnector(
                    limit=50,  # 最大连接数
                    ssl=False,  # 禁用SSL验证（可选）
                    force_close=True,  # 强制关闭空闲连接
                    enable_cleanup_closed=True  # 清理已关闭的连接
                ),
                timeout=aiohttp.ClientTimeout(total=30)
        ) as session:

            async with session.get(url=url, headers=headers, cookies=cookies) as response:
                # 检查反爬状态码
                if response.status in (444, 418, 413):
                    raise Exception(f'反爬: HTTP {response.status} - 被识别为机器人')

                # 获取 HTML 内容
                html_content = await response.text()

                # 反爬内容检查
                if 'Just a moment...' in html_content:
                    raise Exception(f'反爬：请求失败！（内容过短）URL: {url}')
                else:
                    return html_content

    except Exception as e:
        raise Exception(f'反爬：请求失败！{e}')


# 请求第一种列表，
# 页面增量-请求-获取文章链接-获取下一页链接--请求-获取文章链接
async def request_1(dict_item):
    """处理第一种页面增量请求"""
    all_articles = []

    for url, lang in dict_item.items():
        current_url = url
        page_count = 1
        continue_fign = True  # 是否跳出循环
        BASE_URL_1 = url.split('sarasas')[0]

        while continue_fign:
            try:
                print(f"正在请求 {lang} 页面 {page_count}: {current_url}")
                html_content = await fetch_page(current_url)
                tree = html.fromstring(html_content)
                # 获取文章链接
                url_list = tree.xpath('//div[@align="justify"]//tbody//a/@href')
                # 获取日期
                date_list = tree.xpath('//div[@align="justify"]//tbody//td[1]/text()')
                # 将三个列表合并为字典列表
                articles_on_page = [
                    {
                        'url': BASE_URL_1 + url_item,
                        'date': date_list[i],
                        'lang': lang
                    }
                    for i, url_item in enumerate(url_list)
                ]

                # 获取下一页
                next_url_ele = tree.xpath('//a[.="Toliau >>"]/@href')
                if next_url_ele:
                    current_url = BASE_URL_1 + next_url_ele[0]
                # 到达最后一页
                else:
                    continue_fign = False

                all_articles.extend(articles_on_page)
                print(f"在页面 {page_count} 找到 {len(articles_on_page)} 篇文章")


            except Exception as e:
                print(f"请求失败 {current_url}: {e}")
                current_url = None

    return all_articles


async def request_2(dict_item):
    """处理第一种页面增量请求"""
    all_articles = []

    for url, lang in dict_item.items():
        BASE_URL_2 = 'https://grybauskaite.lrp.lt'
        ID = 6590 if lang == 'EN' else 6588
        for year in range(2009, 2024):
            for mouth in range(1, 13):
                try:
                    # 构建url
                    url = f'https://grybauskaite.lrp.lt/en/activities/speeches/{ID}/{year}-{mouth}'
                    print(f'2开始请求：{url}')
                    html_content = await fetch_page(url)
                    tree = html.fromstring(html_content)
                    # 获取文章链接
                    url_list = tree.xpath('//div[@class="news_list"]/div/a/@href')
                    if not url_list:
                        continue
                    # 获取日期
                    date_list = tree.xpath('//div[@class="news_list"]/div/a/div/span[@class="date"]/text()')
                    # 将三个列表合并为字典列表
                    articles_on_page = [
                        {
                            'url': BASE_URL_2 + url_item,
                            'date': date_list[i],
                            'lang': lang
                        }
                        for i, url_item in enumerate(url_list)
                    ]

                    all_articles.extend(articles_on_page)
                    print(f"在页面 {ID}/{year}-{mouth} 找到 {len(articles_on_page)} 篇文章")


                except Exception as e:
                    print(f"请求失败{url}-{e}")

    return all_articles


async def request_3():
    """处理第一种页面增量请求"""
    all_articles = []

    for page in (0, 15):
        BASE_URL_3 = 'https://archyvas.lrp.lt/adamkus3/en/activities/speeches/'
        current_url = f'https://archyvas.lrp.lt/adamkus3/en/activities/speeches/p{page}.html'
        try:
            print(f"正在请求 LT 页面 {page}: {current_url}")
            html_content = await fetch_page(current_url)
            tree = html.fromstring(html_content)
            # 获取文章链接
            url_list = tree.xpath('//div[@id="inner-container"]/div[@class="news_date_and_title"]/span/a/@href')
            # 获取日期
            date_list = tree.xpath('//div[@id="inner-container"]/div[@class="news_date_and_title"]/span[@class="news_date"]/text()')
            # 将三个列表合并为字典列表
            articles_on_page = [
                {
                    'url': BASE_URL_3 + url_item,
                    'date': date_list[i],
                    'lang': 'LT'
                }
                for i, url_item in enumerate(url_list)
            ]

            all_articles.extend(articles_on_page)
            print(f"在页面 {page} 找到 {len(articles_on_page)} 篇文章")


        except Exception as e:
            print(f"请求失败 {current_url}: {e}")

    return all_articles


async def process_single_queue(db_manager):
    """处理单个队列项"""
    try:
        data1 = await request_1(add_url_list1_map)
        data2 = await request_2(add_url_list2_map)
        data3 = await request_3(add_url_list3_map)
        data = data1 + data2 + data3
        await db_manager.table_insert_batch(
            table='lt_news_queue',
            data=data,
        )

    except Exception as e:
        logger.exception(e)


async def main_async():
    async with DbManager(config=0) as db_manager:  # 自动初始化 db 和 aiohttp session
        db_manager.fsign = 1
        while True:
            start_time = time.time()

            semaphore = asyncio.Semaphore(MAX_WORKERS)

            async def limited_task(queue):
                async with semaphore:
                    return await process_single_queue(db_manager, queue)

            tasks = [limited_task(q) for q in queues]
            results = await asyncio.gather(*tasks, return_exceptions=True)

            success_count = sum(1 for r in results if r is True)
            failed_count = sum(1 for r in results if r is False)
            error_count = sum(1 for r in results if isinstance(r, Exception))

            batch_time = time.time() - start_time
            logger.debug(
                f"批次完成: 总数={len(queues)}, 成功={success_count}, "
                f"失败={failed_count}, 异常={error_count}, 耗时={batch_time:.2f}s"
            )
            logger.info(f"等待 {RETRY_DELAY} 秒后处理下一批...")
            await asyncio.sleep(RETRY_DELAY)


if __name__ == "__main__":
    asyncio.run(main_async())
