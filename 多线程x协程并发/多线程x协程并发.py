import asyncio
import concurrent.futures
import aiohttp
from typing import List
import time


def run_async_in_thread(urls: List[str], thread_id: int, max_concurrent_tasks: int = 50):
    """在单个线程中运行异步事件循环"""
    asyncio.set_event_loop(asyncio.new_event_loop())

    async def thread_main():
        """线程内的异步主函数"""
        # 优化连接参数
        timeout = aiohttp.ClientTimeout(total=30, connect=10)
        connector = aiohttp.TCPConnector(
            limit=max_concurrent_tasks + 10,  # 略大于协程数量
            limit_per_host=min(20, max_concurrent_tasks),
            verify_ssl=False
        )

        async with aiohttp.ClientSession(
                connector=connector,
                timeout=timeout,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
        ) as session:
            # 使用信号量控制并发协程数量
            semaphore = asyncio.Semaphore(max_concurrent_tasks)

            async def bounded_fetch(url):
                async with semaphore:
                    return await fetch_url(url, session, thread_id)

            tasks = []
            for url in urls:
                task = asyncio.create_task(bounded_fetch(url))
                tasks.append(task)

            results = await asyncio.gather(*tasks, return_exceptions=True)
            return results

    return asyncio.run(thread_main())


async def fetch_url(url: str, session: aiohttp.ClientSession, thread_id: int):
    """异步获取URL"""
    try:
        start = time.time()
        async with session.get(url) as response:
            # 读取完整的响应文本
            text = await response.text()
            await asyncio.sleep(2)
            elapsed = time.time() - start

            # 判断响应文本长度是否大于10万字符
            text_length = len(text)
            is_successful = response.status < 400 and text_length > 100000

            return {
                'url': url,
                'status': response.status,
                'thread': thread_id,
                'time': elapsed,
                'error': None,
                'text_length': text_length,
                'is_successful': is_successful
            }
    except Exception as e:
        return {
            'url': url,
            'error': str(e),
            'thread': thread_id,
            'status': None,
            'time': None,
            'text_length': 0,
            'is_successful': False
        }


class ThreadPoolAsyncCrawler:
    """使用线程池管理多个异步事件循环"""

    def __init__(self, max_workers: int = 4, max_concurrent_tasks: int = 50):
        self.max_workers = max_workers
        self.max_concurrent_tasks = max_concurrent_tasks  # 每个线程的最大协程并发数
        self.executor = concurrent.futures.ThreadPoolExecutor(
            max_workers=max_workers,
            thread_name_prefix='async_crawler'
        )

    def crawl(self, all_urls: List[str]):
        """主爬取方法"""
        # 将URL分片到各个线程
        chunk_size = len(all_urls) // self.max_workers
        url_chunks = []

        for i in range(self.max_workers):
            start = i * chunk_size
            end = start + chunk_size if i < self.max_workers - 1 else len(all_urls)
            url_chunks.append(all_urls[start:end])

        # 提交任务到线程池
        futures = []
        for i, urls in enumerate(url_chunks):
            if urls:  # 避免空列表
                future = self.executor.submit(
                    run_async_in_thread,
                    urls,
                    i,
                    self.max_concurrent_tasks  # 传递协程并发数
                )
                futures.append(future)

        # 收集结果
        all_results = []
        for future in concurrent.futures.as_completed(futures):
            try:
                results = future.result(timeout=300)
                all_results.extend(results)
            except Exception as e:
                print(f"线程执行出错: {e}")

        return all_results

    def shutdown(self):
        """关闭线程池"""
        self.executor.shutdown(wait=True)


def analyze_results(results):
    """分析结果（保持不变）"""
    # ... 原有的分析代码保持不变


# 使用示例
if __name__ == "__main__":
    test_urls = [
        "https://fyndiq.se/produkt/iphone-6-7-8-se-skal-mobilskal-eminem-multifarg-ff05e4fba85d47a7/"
    ]

    urls = []
    for i in range(500):
        for base_url in test_urls:
            urls.append(f"{base_url}?request={i}")

    print(f"开始爬取 {len(urls)} 个URL...")
    print(f"线程数: 10, 每个线程最大协程并发数: 50")
    print(f"理论最大并发: 10线程 × 50协程 = 500并发")

    # 创建爬虫，设置线程数和协程并发数
    crawler = ThreadPoolAsyncCrawler(max_workers=1, max_concurrent_tasks=50)

    start_time = time.time()
    results = crawler.crawl(urls)
    elapsed = time.time() - start_time

    # 输出结果
    print(f"\n=== 性能统计 ===")
    print(f"总URL数: {len(urls)}")
    print(f"完成请求数: {len(results)}")
    print(f"总耗时: {elapsed:.2f}秒")
    print(f"平均QPS: {len(results) / elapsed:.1f}")

    analyze_results(results)
    crawler.shutdown()