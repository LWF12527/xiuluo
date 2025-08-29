import asyncio
import aiohttp
import random
import time
import json
from datetime import datetime

# 配置参数
CONCURRENCY_LIMIT = 5  # 并发限制数量
TOTAL_REQUESTS = 10000  # 总共要发送的请求数量
REQUEST_TIMEOUT = 30  # 请求超时时间（秒）


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "dnt": "1",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-site",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}
cookies = {
    "bid": "Sb016leI0q4",
    "__gads": "ID=d4f05b1d3d5e50fb:T=1755842317:RT=1755842317:S=ALNI_MbLswBOhDWlJUnEEG9OPqcPfONRtA",
    "__gpi": "UID=000011841d2fdd9c:T=1755842317:RT=1755842317:S=ALNI_MayVehzBYJSpW8nMZQYJykgpXF4Lw",
    "__eoi": "ID=112afe0797c8c4db:T=1755842317:RT=1755842317:S=AA-AfjZkjZIJ03hMG3kk6L4O5DOC",
    "_ga": "GA1.1.561688829.1755842317",
    "_sharedID": "da608c03-aa48-4703-8bfb-7bf0dbdf7183",
    "_sharedID_cst": "2SzgLJUseQ%3D%3D",
    "FCNEC": "%5B%5B%22AKsRol-_SpxDNgNu8F-syyHlFQA0JYjxoq03HFJZ2kSAMGNnGlS2unwjJDao21nJt5Cc4IBbDP2_x1LjO9i65Af-l3V5E0wLj8v1-3GGNm5NH2JzLvcHCAutyrui1e6YtZcITc7LTjT2jstYz0wd8GTPY0im-UGVoA%3D%3D%22%5D%5D",
    "__utmc": "30149280",
    "__utmz": "30149280.1755842320.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
    "regpop": "1",
    "ll": "\"108231\"",
    "__utma": "30149280.561688829.1755842317.1755842320.1756280932.2",
    "__utmt": "1",
    "ap_v": "0,6.0",
    "_ga_P83QWMDYS1": "GS2.1.s1756280939$o2$g0$t1756280939$j60$l0$h0",
    "__utmb": "30149280.2.10.1756280932"
}
url = "https://site.douban.com/jessechow/"
# 全局计数器
request_count = 0
success_count = 0
failure_count = 0


async def fetch(session, semaphore):
    """异步获取页面内容"""
    global request_count, success_count, failure_count

    async with semaphore:
        try:
            # 随机延迟 (2-3秒)
            await asyncio.sleep(random.uniform(0.5, 1))

            # 发送异步请求
            async with session.get(url,timeout=REQUEST_TIMEOUT) as response:
                html_text = await response.text()
                print(f"{request_count} 次:请求成功: {len(html_text)} 字节")

                # 更新计数器
                request_count += 1
                success_count += 1

                # 这里可以添加处理返回数据的逻辑
                # 例如：解析HTML、提取数据等
                len_text = len(html_text)
                print(len_text)
                request_count += 1

                if len_text > 50000:
                    return True
                else:
                    return False
        except Exception as e:
            print(f"请求出错: {e}")
            request_count += 1
            failure_count += 1
            return None


async def worker(session, semaphore):
    """执行单个任务"""
    return await fetch(session, semaphore)


async def main():
    """主协程"""
    global request_count, success_count, failure_count

    # 创建连接池和信号量
    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)

    # 创建CookieJar
    cookie_jar = aiohttp.CookieJar()
    for name, value in cookies.items():
        cookie_jar.update_cookies({name: value})

    start_time = time.time()
    connector = aiohttp.TCPConnector(limit=20, limit_per_host=5) # 全局最大连接数20，单个主机最大5

    # 创建会话
    async with aiohttp.ClientSession(
            connector=connector,
            headers=headers,
            cookie_jar=cookie_jar,
    ) as session:
        # 创建任务列表
        tasks = [asyncio.create_task(worker(session, semaphore)) for _ in range(TOTAL_REQUESTS)]

        # 等待所有任务完成并获取结果
        results = await asyncio.gather(*tasks, return_exceptions=False)

    # 计算耗时
    end_time = time.time()
    total_time = end_time - start_time

    # 打印统计信息
    print("\n" + "=" * 50)
    print(f"总请求次数: {request_count}")
    print(f"成功请求: {success_count}")
    print(f"失败请求: {failure_count}")
    print(f"总耗时: {total_time:.2f}秒")
    print(f"平均每秒请求数: {request_count / total_time:.2f}")
    print(f"实际并发效率: {request_count / total_time / CONCURRENCY_LIMIT:.2f}倍")
    print("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())