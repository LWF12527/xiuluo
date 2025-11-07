import asyncio
import os
import random
import sys
import time
import json
from typing import List, Dict, Any, Tuple
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor
import aiohttp
from loguru import logger
from lxml import html

from async_custom_mysql_pool import DbManager
from 立陶宛总统讲话采集.增量爬虫_获取请求链接 import cookies

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
MAX_CONCURRENT_REQUESTS = 20
BATCH_SIZE = 50  # 减少批量大小，更频繁插入
REAL_TIME_INSERT_THRESHOLD = 10  # 达到这个数量就立即插入
MAX_RETRIES = 3
RETRY_DELAY = 2

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

# URL配置
add_url_list1_map = {
    "https://archyvas.lrp.lt/adamkus/sarasas15ee.html?nuo=1&kat=4&search=": "LT",
    "https://archyvas.lrp.lt/adamkus/en/sarasasdd13.html?nuo=1&kat=12&search=": "EN",
    "https://archyvas.lrp.lt/paksas/sarasas8710.html?kat=4": "LT",
    "https://archyvas.lrp.lt/paksas/en/sarasasdd13.html?nuo=1&kat=12&search=": "EN"
}

add_url_list2_map = {
    "https://grybauskaite.lrp.lt/en/activities/speeches/6590/2009-11": "EN",
    "https://grybauskaite.lrp.lt/lt/prezidentes-veikla/kalbos/6588/2023-06": "LT"
}

add_url_list3_map = {'https://archyvas.lrp.lt/adamkus3/en/activities/speeches/p15.html': "LT"}


@dataclass
class ArticleData:
    """文章数据结构"""
    url: str
    date: str
    lang: str
    source_type: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            'url': self.url,
            'date': self.date,
            'lang': self.lang,
            'source_type': self.source_type,
        }

    def __str__(self) -> str:
        return f"Article({self.lang}-{self.source_type}): {self.date} - {self.url}"


class RealTimeSpider:
    def __init__(self, db_manager: DbManager, max_concurrent_requests: int = MAX_CONCURRENT_REQUESTS):
        self.db_manager = db_manager
        self.semaphore = asyncio.Semaphore(max_concurrent_requests)
        self.session = None
        self.article_queue = asyncio.Queue()
        self.processed_count = 0
        self.start_time = time.time()

        # 统计信息
        self.stats = {
            'total_articles': 0,
            'successful_inserts': 0,
            'failed_inserts': 0,
            'type1_count': 0,
            'type2_count': 0,
            'type3_count': 0
        }

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(
                limit=MAX_CONCURRENT_REQUESTS,
                ssl=False,
                force_close=True,
                enable_cleanup_closed=True
            ),
            timeout=aiohttp.ClientTimeout(total=30),
            headers=headers,
            cookies=cookies
        )

        # 启动实时插入任务
        asyncio.create_task(self._real_time_inserter())

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

        # 插入队列中剩余的数据
        await self._flush_queue()

    async def _real_time_inserter(self):
        """实时插入器，定期检查并插入队列中的数据"""
        buffer = []

        while True:
            try:
                # 等待新数据或超时
                article = await asyncio.wait_for(self.article_queue.get(), timeout=1.0)
                buffer.append(article)

                # 达到阈值或缓冲区有一定数量时立即插入
                if (len(buffer) >= REAL_TIME_INSERT_THRESHOLD or
                        self.article_queue.empty() and buffer):
                    await self._insert_batch(buffer)
                    buffer = []

            except asyncio.TimeoutError:
                # 超时但缓冲区有数据，插入
                if buffer:
                    await self._insert_batch(buffer)
                    buffer = []
            except Exception as e:
                logger.error(f"实时插入器错误: {e}")

    async def _insert_batch(self, articles: List[ArticleData]):
        """批量插入数据"""
        if not articles:
            return

        try:
            data_to_insert = [article.to_dict() for article in articles]

            await self.db_manager.table_insert_batch(
                table='lt_news_queue',
                data=data_to_insert,
            )

            self.stats['successful_inserts'] += len(articles)

            # 打印插入的数据
            for article in articles:
                self._print_article(article)
                self.stats['total_articles'] += 1

            logger.info(f"✓ 成功插入 {len(articles)} 篇文章到数据库")

        except Exception as e:
            self.stats['failed_inserts'] += len(articles)
            logger.error(f"插入失败: {e}")
            # 可以选择重试或记录到文件

    async def _flush_queue(self):
        """清空队列中的所有数据"""
        buffer = []
        while not self.article_queue.empty():
            try:
                article = self.article_queue.get_nowait()
                buffer.append(article)
            except asyncio.QueueEmpty:
                break

        if buffer:
            await self._insert_batch(buffer)

    def _print_article(self, article: ArticleData):
        """格式化打印文章信息"""
        elapsed = time.time() - self.start_time
        rate = self.stats['total_articles'] / elapsed if elapsed > 0 else 0

        print("┌" + "─" * 80 + "┐")
        print(f"│ 📰 文章 #{self.stats['total_articles'] + 1:04d} | 速率: {rate:.2f} 篇/秒")
        print(f"│ 来源: {article.source_type:8} | 语言: {article.lang:2} | 日期: {article.date:15}")
        print(f"│ 链接: {article.url}")
        print("└" + "─" * 80 + "┘")

    async def fetch_page_with_retry(self, url: str, retries: int = MAX_RETRIES) -> str:
        """带重试机制的页面获取"""
        for attempt in range(retries):
            try:
                async with self.semaphore:
                    await asyncio.sleep(random.uniform(0.3, 0.8))

                    async with self.session.get(url) as response:
                        if response.status in (444, 418, 413):
                            raise Exception(f'反爬: HTTP {response.status}')

                        html_content = await response.text()

                        # 反爬内容检查
                        if 'Just a moment...' in html_content:
                            raise Exception(f'反爬：请求失败！（内容过短）URL: {url}')

                        return html_content

            except Exception as e:
                if attempt == retries - 1:
                    raise
                await asyncio.sleep(RETRY_DELAY * (attempt + 1))

        raise Exception(f'所有重试失败: {url}')

    async def process_type1_urls(self):
        """处理type1 URLs - 页面增量"""
        logger.info("🚀 开始处理Type1 URLs (页面增量)")

        tasks = []
        for url, lang in add_url_list1_map.items():
            tasks.append(self._process_single_type1_site(url, lang))

        await asyncio.gather(*tasks, return_exceptions=True)

    async def _process_single_type1_site(self, base_url: str, lang: str):
        """处理单个type1站点"""
        current_url = base_url
        page_count = 1
        site_base = base_url.split('sarasas')[0]

        while current_url:
            try:
                logger.debug(f"Type1-{lang} 第{page_count}页: {current_url}")
                html_content = await self.fetch_page_with_retry(current_url)
                tree = html.fromstring(html_content)

                # 提取文章数据
                url_list = tree.xpath('//div[@align="justify"]//tbody//a/@href')
                date_list = tree.xpath('//div[@align="justify"]//tbody//td[1]/text()')

                articles = []
                for i, url_item in enumerate(url_list):
                    article = ArticleData(
                        url=site_base + url_item,
                        date=date_list[i],
                        lang=lang,
                        source_type='TYPE1',
                    )
                    articles.append(article)
                    self.stats['type1_count'] += 1

                # 立即放入队列
                for article in articles:
                    await self.article_queue.put(article)

                logger.info(f"Type1-{lang} 第{page_count}页: 找到 {len(articles)} 篇文章")

                # 检查下一页
                next_url_ele = tree.xpath('//a[.="Toliau >>"]/@href')
                current_url = site_base + next_url_ele[0] if next_url_ele else None
                page_count += 1

            except Exception as e:
                logger.error(f"Type1-{lang} 页面处理失败: {e}")
                current_url = None

    async def process_type2_urls(self):
        """处理type2 URLs - 年份月份增量"""
        logger.info("🚀 开始处理Type2 URLs (年份月份增量)")

        tasks = []
        for base_url, lang in add_url_list2_map.items():
            tasks.append(self._process_single_type2_site(base_url, lang))

        await asyncio.gather(*tasks, return_exceptions=True)

    async def _process_single_type2_site(self, base_url: str, lang: str):
        """处理单个type2站点"""
        site_base = 'https://grybauskaite.lrp.lt'
        ID = 6590 if lang == 'EN' else 6588

        # 创建所有年份月份的任务
        year_tasks = []
        for year in range(2009, 2024):
            year_tasks.append(self._process_type2_year(year, lang, ID, site_base))

        # 控制并发，避免同时处理太多年份
        for i in range(0, len(year_tasks), 3):  # 每次并发3个年份
            batch = year_tasks[i:i + 3]
            await asyncio.gather(*batch, return_exceptions=True)
            await asyncio.sleep(1)  # 批次间短暂延迟

    async def _process_type2_year(self, year: int, lang: str, site_id: int, site_base: str):
        """处理单个年份"""
        month_tasks = []
        for month in range(1, 13):
            url = f'https://grybauskaite.lrp.lt/{lang.lower()}/activities/speeches/{site_id}/{year}-{month:02d}'
            month_tasks.append(self._process_type2_month(url, lang, site_base, year, month))

        # 并发处理所有月份
        await asyncio.gather(*month_tasks, return_exceptions=True)

    async def _process_type2_month(self, url: str, lang: str, site_base: str, year: int, month: int):
        """处理单个月份"""
        try:
            logger.debug(f"Type2 处理: {year}-{month:02d}")
            html_content = await self.fetch_page_with_retry(url)
            tree = html.fromstring(html_content)

            url_list = tree.xpath('//div[@class="news_list"]/div/a/@href')
            if not url_list:
                return

            date_list = tree.xpath('//div[@class="news_list"]/div/a/div/span[@class="date"]/text()')

            articles = []
            for i, url_item in enumerate(url_list):
                article = ArticleData(
                    url=site_base + url_item,
                    date=date_list[i] if i < len(date_list) else f"{year}-{month:02d}",
                    lang=lang,
                    source_type='TYPE2',
                )
                articles.append(article)
                self.stats['type2_count'] += 1

            # 立即放入队列
            for article in articles:
                await self.article_queue.put(article)

            logger.info(f"Type2 {year}-{month:02d}: 找到 {len(articles)} 篇文章")

        except Exception as e:
            logger.error(f"Type2 {year}-{month:02d} 处理失败: {e}")

    async def process_type3_urls(self):
        """处理type3 URLs"""
        logger.info("🚀 开始处理Type3 URLs")

        tasks = []
        site_base = 'https://archyvas.lrp.lt/adamkus3/en/activities/speeches/'

        for page in range(0, 16):
            url = f'https://archyvas.lrp.lt/adamkus3/en/activities/speeches/p{page}.html'
            tasks.append(self._process_single_type3_page(url, site_base, page))

        await asyncio.gather(*tasks, return_exceptions=True)

    async def _process_single_type3_page(self, url: str, site_base: str, page_num: int):
        """处理单个type3页面"""
        try:
            logger.debug(f"Type3 第{page_num}页: {url}")
            html_content = await self.fetch_page_with_retry(url)
            tree = html.fromstring(html_content)

            url_list = tree.xpath('//div[@id="inner-container"]/div[@class="news_date_and_title"]/span/a/@href')
            date_list = tree.xpath('//div[@id="inner-container"]/div[@class="news_date_and_title"]/span[@class="news_date"]/text()')

            articles = []
            for i, url_item in enumerate(url_list):
                article = ArticleData(
                    url=site_base + url_item,
                    date=date_list[i] if i < len(date_list) else '未知日期',
                    lang='LT',
                    source_type='TYPE3',
                )
                articles.append(article)
                self.stats['type3_count'] += 1

            # 立即放入队列
            for article in articles:
                await self.article_queue.put(article)

            logger.info(f"Type3 第{page_num}页: 找到 {len(articles)} 篇文章")

        except Exception as e:
            logger.error(f"Type3 第{page_num}页处理失败: {e}")

    def print_stats(self):
        """打印统计信息"""
        elapsed = time.time() - self.start_time
        rate = self.stats['total_articles'] / elapsed if elapsed > 0 else 0

        print("\n" + "=" * 80)
        print("📊 爬取统计报告")
        print("=" * 80)
        print(f"总运行时间: {elapsed:.2f} 秒")
        print(f"处理速率: {rate:.2f} 篇/秒")
        print(f"总文章数: {self.stats['total_articles']}")
        print(f"成功插入: {self.stats['successful_inserts']}")
        print(f"插入失败: {self.stats['failed_inserts']}")
        print(f"Type1文章: {self.stats['type1_count']}")
        print(f"Type2文章: {self.stats['type2_count']}")
        print(f"Type3文章: {self.stats['type3_count']}")
        print("=" * 80)


async def main_async():
    """主异步函数"""
    async with DbManager(config=0) as db_manager:
        db_manager.fsign = 1

        async with RealTimeSpider(db_manager) as spider:
            try:
                # 并发执行所有URL类型处理
                logger.info("开始并发爬取所有URL类型...")

                await asyncio.gather(
                    spider.process_type1_urls(),
                    spider.process_type2_urls(),
                    spider.process_type3_urls(),
                    return_exceptions=True
                )

                # 确保所有数据都已插入
                await asyncio.sleep(2)

                # 打印最终统计
                spider.print_stats()

            except Exception as e:
                logger.error(f"主流程执行失败: {e}")
                raise
            finally:
                # 最终统计
                spider.print_stats()


if __name__ == "__main__":
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        logger.info("用户中断执行")
    except Exception as e:
        logger.error(f"程序执行失败: {e}")
        sys.exit(1)