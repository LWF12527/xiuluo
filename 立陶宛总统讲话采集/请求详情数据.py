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
MAX_WORKERS = 20
RETRY_DELAY = 3

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "dnt": "1",
    "origin": "https://grybauskaite.lrp.lt",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://grybauskaite.lrp.lt/en/activities/speeches/6590/2009-11?__cf_chl_tk=KNgUN1NZLJkciKLjcZj95zW73_aGPPCNlUfaRkxCGn4-1762483183-1.0.1.1-HfZvhOlyKNnPqkqCnddQn4KK.l2KgAAXcnX4q8Edbn4",
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
    "sec-fetch-site": "same-origin",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}
cookies = {
    "privacy_2": "0",
    "privacy_3": "0",
    "privacy_4": "0",
    "privacy_verify": "1",
    "EW4SITE": "ev7ebvcitv5mav9nsddfq8c4bi",
    "SITEXSRF141": "dfxnugw99p2729nefhk4vcznnjpv9rka",
    "cf_clearance": "_ztSJ2bTRYcaPnqxb.lvqYJYQqjUoxtdisBipDVjsdU-1762487174-1.2.1.1-rmDmH6iK_ld9R6zQWFE4xaEJsOs3.qGKhN2zAcT6UF_dQ5hHLICvcIHD.PqZTnf5fYIcyRR8Ru2CtyeWr_QvRXg5EIw.dPB8eKvP2p2I_wjZO8COebnQLMqewrnfe2RjtDiy4Xjh8i4DysOdg8VokaIuhjTowH6Yd6OfS6SV_HGqUzPuJRC61syWbdfuDRAsgGZX1ygAHc5fikQXhhxahU2CAQTugfTEyk4OF2sAKks"
}


async def fetch_page_with_retry(url, retries=3) -> str:
    """带重试机制的页面获取"""
    for attempt in range(retries):
        try:
            await asyncio.sleep(random.uniform(0.3, 0.8))
            async with aiohttp.ClientSession(
                    connector=aiohttp.TCPConnector(
                        limit=50,
                        ssl=False,
                        force_close=True
                    ),
                    timeout=aiohttp.ClientTimeout(total=30),
                    headers=headers,
                    cookies=cookies
            ) as session:
                async with session.get(url) as response:
                    if response.status in (444, 418, 413):
                        raise Exception(f'反爬: HTTP {response.status}')

                    html_content = await response.text()

                    # 反爬内容检查
                    if 'Just a moment...' in html_content:
                        raise Exception(f'反爬：请求失败！URL: {html_content[:200]}')

                    return html_content

        except Exception as e:
            if attempt == retries - 1:
                raise
            await asyncio.sleep(RETRY_DELAY * (attempt + 1))

    raise Exception(f'所有重试失败: {url}')


async def extract_news(url):
    # url = 'https://archyvas.lrp.lt/adamkus/en/oneef42.html?id=3562'  # 类型1
    # url = 'http://grybauskaite.lrp.lt/lt/nato-generalinio-sekretoriaus-jenso-stoltenbergo-kalba-manfredo-wernerio-apdovanojimo-iteikimo-prezidentei-daliai-grybauskaitei-ceremonijoje/32897'  # 类型3
    # url = 'https://archyvas.lrp.lt/adamkus3/en/activities/speeches/remarks_by_h.e._valdas_adamkus_president_of_the_republic_of_lithuania_at_the_22nd_european_meeting_of_cultural_journals.html'  # 类型3

    html_text = await fetch_page_with_retry(url=url, retries=3)
    tree = html.fromstring(html_text)

    # 标题提取 - 按照类型1、2、3的顺序
    article_title = ""
    # 类型1: //font[@face="Times New Roman"]
    article_title = tree.xpath('//font[@face="Times New Roman"]/text()')
    if not article_title:  # 类型2: //h4[@class="news_content_title"]
        article_title = tree.xpath('//h4[@class="news_content_title"]/text()')
    if not article_title:  # 类型3: //h1[@class="main_title"]
        article_title = tree.xpath('//h1[@class="main_title"]/text()')

    if article_title:
        article_title = article_title[0].strip()

    # 内容提取 - 按照类型1、2、3的顺序
    article_text = ""

    # 类型1: //div[@align="justify"]/p
    if not article_text:
        elements_p = tree.xpath('//div[@align="justify"]/p')
        result_lines = []
        for p in elements_p:
            result_lines.append(''.join(p.xpath('./text() | ./br/text()')))
            result_lines.append('\n')
        article_text = '\n'.join(result_lines)

    # 类型3: //p[@align="justify"]/text()
    if not article_text:
        article_text = "\n\n".join(tree.xpath('//p[@align="justify"]/text() |//p[contains(@style,"justify")]/span/text()'))
        if not article_text:
            article_text ="\n".join(tree.xpath('//div[contains(@style,"justify")]/text()'))

    # 类型2: //div[@class="news_inner"]/div/p
    if not article_text:
        elements_p = tree.xpath('//div[@class="news_inner"]/div/p | //div[@id="inner-container" or @class="dynamic_cont"]/p')
        result_lines = []
        for p in elements_p:
            for br in p.xpath('./text() | ./br/text()'):
                result_lines.append(br)
            result_lines.append('\n')
        article_text = '\n'.join(result_lines)
    return article_title, article_text


async def process_single_queue(db_manager, queue):
    """处理单个队列项"""
    try:
        logger.info(f"开始处理产品URL: {queue['id']} - {queue['url']}")
        title, text = await extract_news(queue['url'])
        if not title:
            await db_manager.table_update(
                table='lt_news_queue',
                data={'sync_status': 2, 'sync_result': "没有标题数据"},
                where={'id': queue["id"]}
            )
            return False
        if not text:
            await db_manager.table_update(
                table='lt_news_queue',
                data={'sync_status': 2, 'sync_result': "没有内容数据"},
                where={'id': queue["id"]}
            )
            return False
        data = {
            'article_title': title,
            'article_text': text,
            'type': queue['source_type'],
            'date': queue['date'],
            'q_id': queue['id'],
            'url': queue['url'],
            'lang': queue['lang'],
        }
        await db_manager.table_insert(
            table='lt_news_detail',
            data=data,
        )
        await db_manager.table_update(
            table='lt_news_queue',
            data={'sync_status': 1},
            where={'id': queue["id"]}
        )
        return True
    except Exception as e:
        logger.exception(e)
        await db_manager.table_update(
            table='lt_news_queue',
            data={'sync_count': queue['sync_count'] + 1},
            where={'id': queue["id"]}
        )
        return False


async def fetch_queues_async(db_manager):
    sql = f"""
        SELECT * 
        FROM lt_news_queue 
        WHERE sync_status = 0 and sync_count<3
    """
    return await db_manager.table_select(sql)


async def main_async():
    async with DbManager(config=0) as db_manager:  # 自动初始化 db 和 aiohttp session
        db_manager.fsign = 1
        while True:
            queues = await fetch_queues_async(db_manager)
            if not queues:
                logger.info("无待处理任务，等待3600秒...")
                await asyncio.sleep(3600)
                continue

            logger.info(f"获取到 {len(queues)} 个待处理任务, 并发数量={MAX_WORKERS}")
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
