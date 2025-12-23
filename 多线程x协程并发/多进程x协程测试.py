import asyncio
import concurrent.futures
import time
from typing import List
import multiprocessing
from multiprocessing import Pool, Manager
import aiohttp


def run_async_in_process(urls: List[str], process_id: int, max_concurrent_tasks: int = 50, result_queue=None):
    """在单个进程中运行异步事件循环"""
    # 为每个进程创建独立的事件循环
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        # 运行异步主函数
        results = loop.run_until_complete(process_main(urls, process_id, max_concurrent_tasks))

        # 如果有结果队列，将结果放入队列
        if result_queue is not None:
            for result in results:
                result_queue.put(result)

        loop.close()
        return results
    except Exception as e:
        print(f"进程 {process_id} 执行出错: {e}")
        if result_queue is not None:
            result_queue.put({'error': f"进程 {process_id} 异常: {str(e)}"})
        return []


async def process_main(urls: List[str], process_id: int, max_concurrent_tasks: int):
    """进程内的异步主函数"""
    # 优化连接参数
    timeout = aiohttp.ClientTimeout(total=30, connect=10)
    connector = aiohttp.TCPConnector(
        limit=max_concurrent_tasks + 10,  # 略大于协程数量
        # limit_per_host=min(20, max_concurrent_tasks),
        limit_per_host=100,
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
                return await fetch_url(url, session, process_id)

        tasks = []
        for url in urls:
            task = asyncio.create_task(bounded_fetch(url))
            tasks.append(task)

        results = await asyncio.gather(*tasks, return_exceptions=True)

        # 过滤掉异常对象，转换为字典
        final_results = []
        for result in results:
            if isinstance(result, Exception):
                final_results.append({
                    'url': 'unknown',
                    'error': str(result),
                    'process': process_id,
                    'status': None,
                    'time': None,
                    'text_length': 0,
                    'is_successful': False
                })
            else:
                final_results.append(result)

        return final_results


async def fetch_url(url: str, session: aiohttp.ClientSession, process_id: int):
    """异步获取URL"""
    try:
        start = time.time()
        async with session.get(url) as response:
            # 读取完整的响应文本
            text = await response.text()
            # await asyncio.sleep(1)
            elapsed = time.time() - start

            # 判断响应文本长度是否大于10万字符
            text_length = len(text)
            is_successful = response.status < 400 and text_length > 100000

            return {
                'url': url,
                'status': response.status,
                'process': process_id,
                'time': elapsed,
                'error': None,
                'text_length': text_length,
                'is_successful': is_successful
            }
    except Exception as e:
        return {
            'url': url,
            'error': str(e),
            'process': process_id,
            'status': None,
            'time': None,
            'text_length': 0,
            'is_successful': False
        }


class ProcessPoolAsyncCrawler:
    """使用进程池管理多个异步事件循环"""

    def __init__(self, max_processes: int = None, max_concurrent_tasks: int = 50):
        self.max_processes = max_processes or multiprocessing.cpu_count()
        self.max_concurrent_tasks = max_concurrent_tasks  # 每个进程的最大协程并发数
        self.manager = Manager()
        self.result_queue = self.manager.Queue()

    def crawl(self, all_urls: List[str]):
        """主爬取方法"""
        # 将URL分片到各个进程
        chunk_size = len(all_urls) // self.max_processes
        url_chunks = []

        for i in range(self.max_processes):
            start = i * chunk_size
            if i == self.max_processes - 1:
                end = len(all_urls)  # 最后一个进程处理剩余的所有URL
            else:
                end = start + chunk_size
            url_chunks.append(all_urls[start:end])

        print(f"创建 {self.max_processes} 个进程，每个进程处理约 {chunk_size} 个URL")

        # 使用进程池
        with Pool(processes=self.max_processes) as pool:
            # 准备进程参数
            process_args = []
            for i, urls in enumerate(url_chunks):
                if urls:  # 避免空列表
                    process_args.append((urls, i, self.max_concurrent_tasks, self.result_queue))

            # 异步启动所有进程
            async_results = []
            for args in process_args:
                # 使用apply_async非阻塞方式启动进程
                async_result = pool.apply_async(run_async_in_process, args=args)
                async_results.append(async_result)

            # 等待所有进程完成
            pool.close()
            pool.join()

        # 从队列中收集结果
        all_results = []
        while not self.result_queue.empty():
            try:
                result = self.result_queue.get_nowait()
                all_results.append(result)
            except:
                break

        return all_results

    def shutdown(self):
        """关闭管理器"""
        self.manager.shutdown()


# 使用示例
if __name__ == "__main__":
    # 在Windows上多进程需要这个保护
    multiprocessing.freeze_support()

    test_urls = [
        "https://fyndiq.se/produkt/coque-la-casa-de-papel-iphone-6-svart-mjuk-stotskydd-a8d0ce71f6fd411d/"

    ]

    max_processes = 10  # 进程数量
    max_concurrent = 50  # 每个进程的协程并发数

    # 生成测试URL
    urls = []
    for i in range(1000):
        for base_url in test_urls:
            urls.append(f"{base_url}?id={i}")

    print(f"开始爬取 {len(urls)} 个URL...")
    print(f"进程数: {max_processes}, 每个进程最大协程并发数: {max_concurrent}")
    print(f"理论最大并发: {max_processes * max_concurrent}并发")

    # 创建爬虫，设置进程数和协程并发数
    crawler = ProcessPoolAsyncCrawler(max_processes=max_processes, max_concurrent_tasks=max_concurrent)

    start_time = time.time()
    results = crawler.crawl(urls)
    elapsed = time.time() - start_time

    # 输出结果统计
    successful_count = sum(1 for r in results if r.get('is_successful', False))
    error_count = sum(1 for r in results if r.get('error'))

    print(f"\n=== 性能统计 ===")
    print(f"总URL数: {len(urls)}")
    print(f"完成请求数: {len(results)}")
    print(f"成功请求数: {successful_count}")
    print(f"错误请求数: {error_count}")
    print(f"总耗时: {elapsed:.2f}秒")
    print(f"平均QPS: {len(results) / elapsed:.1f}")

    # 显示一些示例结果
    print(f"\n=== 示例结果 ===")
    for i, result in enumerate(results[:5]):
        print(f"结果 {i + 1}: {result}")

    crawler.shutdown()
    print("爬取完成！")