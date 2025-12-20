import asyncio
import aiohttp
from typing import List
import time


class PureAsyncCrawler:
    """纯协程爬虫，不使用线程池"""

    def __init__(self, max_concurrent_tasks: int = 500, delay_seconds: float = 0):
        """
        初始化爬虫

        Args:
            max_concurrent_tasks: 最大并发协程数
            delay_seconds: 每个请求后的延迟时间（秒）
        """
        self.max_concurrent_tasks = max_concurrent_tasks
        self.delay_seconds = delay_seconds
        self.session = None

    async def __aenter__(self):
        """异步上下文管理器入口"""
        timeout = aiohttp.ClientTimeout(total=30, connect=10)
        connector = aiohttp.TCPConnector(
            limit=self.max_concurrent_tasks + 10,
            limit_per_host=min(100, self.max_concurrent_tasks),
            verify_ssl=False
        )

        self.session = aiohttp.ClientSession(
            connector=connector,
            timeout=timeout,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """异步上下文管理器退出"""
        if self.session:
            await self.session.close()

    async def crawl(self, urls: List[str]):
        """主爬取方法"""
        if not self.session:
            raise RuntimeError("请使用异步上下文管理器（async with）")

        # 使用信号量控制并发数
        semaphore = asyncio.Semaphore(self.max_concurrent_tasks)

        async def bounded_fetch(url):
            async with semaphore:
                return await self.fetch_url(url)

        # 创建所有任务
        tasks = []
        for url in urls:
            task = asyncio.create_task(bounded_fetch(url))
            tasks.append(task)

        # 等待所有任务完成
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # 处理异常结果
        processed_results = []
        for result in results:
            if isinstance(result, Exception):
                processed_results.append({
                    'url': 'unknown',
                    'error': str(result),
                    'thread': 0,
                    'status': None,
                    'time': None,
                    'text_length': 0,
                    'is_successful': False
                })
            else:
                processed_results.append(result)

        return processed_results

    async def fetch_url(self, url: str):
        """异步获取URL"""
        try:
            start = time.time()
            async with self.session.get(url) as response:
                # 读取完整的响应文本
                text = await response.text()

                # 添加可控制的延迟
                if self.delay_seconds > 0:
                    await asyncio.sleep(self.delay_seconds)

                elapsed = time.time() - start

                # 判断响应文本长度是否大于10万字符
                text_length = len(text)
                is_successful = response.status < 400 and text_length > 100000

                return {
                    'url': url,
                    'status': response.status,
                    'thread': 0,  # 纯协程模式下线程ID固定为0
                    'time': elapsed,
                    'error': None,
                    'text_length': text_length,
                    'is_successful': is_successful
                }
        except Exception as e:
            return {
                'url': url,
                'error': str(e),
                'thread': 0,
                'status': None,
                'time': None,
                'text_length': 0,
                'is_successful': False
            }


def analyze_results(results):
    """分析结果"""
    successful = [r for r in results if r.get('is_successful')]
    errors = [r for r in results if r.get('error')]
    valid_times = [r['time'] for r in results if r['time'] is not None]
    avg_time = sum(valid_times) / len(valid_times) if valid_times else 0

    print(f"\n=== 详细分析 ===")
    print(f"成功请求: {len(successful)}")
    print(f"失败请求: {len(errors)}")
    print(f"平均响应时间: {avg_time:.3f}秒")

    if errors:
        print(f"\n前5个错误:")
        for error in errors[:5]:
            print(f"  URL: {error['url'][:50]}...")
            print(f"  错误: {error['error']}")


async def run_test(concurrency: int, total_requests: int, delay_seconds: float = 0, test_urls: List[str] = None):
    """运行测试

    Args:
        concurrency: 并发协程数
        total_requests: 总请求数
        delay_seconds: 每个请求后的延迟时间
        test_urls: 测试URL列表
    """
    if test_urls is None:
        test_urls = [
            "https://httpbin.org/get",
            "https://httpbin.org/json",
            "https://httpbin.org/html"
        ]

    # 生成测试URL列表
    urls = []
    for i in range(total_requests):
        for base_url in test_urls:
            urls.append(f"{base_url}?request={i}&test={time.time()}")

    print(f"\n{'=' * 50}")
    print(f"测试配置:")
    print(f"并发协程数: {concurrency}")
    print(f"总请求数: {total_requests}")
    print(f"请求延迟: {delay_seconds}秒")
    print(f"理论最大并发: {concurrency}")
    print(f"{'=' * 50}")

    start_time = time.time()

    # 使用纯协程爬虫
    async with PureAsyncCrawler(max_concurrent_tasks=concurrency, delay_seconds=delay_seconds) as crawler:
        results = await crawler.crawl(urls)

    elapsed = time.time() - start_time

    # 输出结果
    print(f"\n=== 性能统计 ===")
    print(f"总URL数: {len(urls)}")
    print(f"完成请求数: {len(results)}")
    print(f"总耗时: {elapsed:.2f}秒")
    print(f"平均QPS: {len(results) / elapsed:.1f}")

    analyze_results(results)

    return elapsed, len(results) / elapsed


async def main():
    """主函数 - 运行多个并发数测试"""

    # 测试不同的并发数
    concurrency_levels = [50]
    total_requests = 500  # 总请求数
    delay_seconds = 2  # 每个请求后的延迟

    # 使用更稳定的测试URL
    test_urls = [
        "https://fyndiq.se/produkt/iphone-6-7-8-se-skal-mobilskal-eminem-multifarg-ff05e4fba85d47a7/"
    ]

    results = []

    for concurrency in concurrency_levels:
        elapsed, qps = await run_test(
            concurrency=concurrency,
            total_requests=total_requests,
            delay_seconds=delay_seconds,
            test_urls=test_urls
        )
        results.append((concurrency, elapsed, qps))

    # 输出汇总结果
    print(f"\n{'=' * 60}")
    print(f"汇总结果 (总请求数: {total_requests}):")
    print(f"{'并发数':<10} {'总耗时(秒)':<12} {'QPS':<10}")
    print(f"{'-' * 60}")
    for concurrency, elapsed, qps in results:
        print(f"{concurrency:<10} {elapsed:<12.2f} {qps:<10.1f}")
    print(f"{'=' * 60}")


# 使用示例
if __name__ == "__main__":
    # 直接运行单个测试
    # asyncio.run(run_test(concurrency=100, total_requests=200, delay_seconds=0))

    # 运行多个并发数对比测试
    asyncio.run(main())