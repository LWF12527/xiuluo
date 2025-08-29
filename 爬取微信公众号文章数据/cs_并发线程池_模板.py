import random

import requests
from lxml import html
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import json
from datetime import datetime
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "dnt": "1",
    "if-modified-since": "Fri, 29 Aug 2025 10:10:37 +0800",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}
cookies = {
    "rewardsn": "",
    "wxtokenkey": "777"
}
url = "https://mp.weixin.qq.com/s/Rzpc-gwZmuEiKMNbc4q9bQ"
request_count = 0  # 用于统计请求次数
CONCURRENCY_LIMIT = 10  # 并发限制数量
total_requests = 10000  # 总共要发送的请求数量


def fetch():
    global request_count
    try:
        time.sleep(random.uniform(0.5,1))
        html_text = requests.get(url, headers=headers).text
        len_text = len(html_text)
        print(len_text)
        request_count += 1

        if len_text > 50000:
            return True
        else:
            return False
    except Exception as e:
        print(f"请求出错: {e}")
        return False

def main():
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=CONCURRENCY_LIMIT) as executor:
        futures = [executor.submit(fetch) for _ in range(total_requests)]
        for i, future in enumerate(as_completed(futures), 1):
            result = future.result()
            print(f"结果 {i}: {result}")

    end_time = time.time()
    print(f"\n总请求次数: {request_count}")
    print(f"总耗时: {end_time - start_time:.2f}秒")
    print(f"平均每秒请求数: {request_count / (end_time - start_time):.2f}")


if __name__ == "__main__":
    main()
