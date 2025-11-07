from loguru import logger
import random
import time

from curl_cffi import requests

headers_bd = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "available-dictionary": ":yCnTUKDfai/aI/v0z57OAWSOx3Q2lJCwtVwKeSVG3i8=:",
    "cache-control": "no-cache",
    "dnt": "1",
    "downlink": "10",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://www.google.com/",
    "rtt": "50",
    "sec-ch-prefers-color-scheme": "light",
    "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-form-factors": "\"Desktop\"",
    "sec-ch-ua-full-version": "\"141.0.7390.123\"",
    "sec-ch-ua-full-version-list": "\"Google Chrome\";v=\"141.0.7390.123\", \"Not?A_Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"141.0.7390.123\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"15.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    "x-browser-channel": "stable",
    "x-browser-copyright": "Copyright 2025 Google LLC. All rights reserved.",
    "x-browser-validation": "AGaxImjg97xQkd0h3geRTArJi8Y=",
    "x-browser-year": "2025",
    "x-client-data": "CKW1yQEIkLbJAQiktskBCKmdygEIo43LAQiTocsBCLCkywEIhaDNAQjLi88BCI6OzwEI7I7PAQilj88BCPeQzwEInpHPAQj7ks8BCJmTzwEIh5XPARjp5M4BGLKGzwEYpYfPARiYiM8BGJeTzwE="
}
def cf_random_headers(url):
    # 随机生成设备像素比 (常见范围0.5-3.0，保留两位小数)
    dpr = round(random.uniform(0.5, 3.0), 2)
    # 随机生成网络下行速度 (0.5-100 Mbps，保留两位小数)
    downlink = round(random.uniform(0.5, 100.0), 2)

    v4 = random.choice([6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    headers = {
        **headers_bd,
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "accept-language": random.choice(['zh-CN,zh;q=0.9', 'en-US,en;q=0.9', 'en-GB,en;q=0.9']),
        "downlink": str(downlink),  # 动态下行速度
        "dpr": str(dpr),  # 动态设备像素比
        "referer": url,
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "sec-ch-ua": f"\"Not)A;Brand\";v=\"{v4}\", \"Chromium\";v=\"138\", \"Brave\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "sec-gpc": "1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        f"x-rand{random.randint(100, 999)}": str(random.randint(1000000, 9999999))
    }
    return headers


def proxy_qgsd():  # 青果代理-全球隧道版本
    tunnel = 'overseas-us.tunnel.qg.net:17814'
    username = "37904CA3"
    password = "5F28FFCEB995"
    proxies = {
        "https": "socks5h://%(user)s:%(pwd)s:A%(area)d@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel, "area": 991900, }
    }
    return proxies


def proxy_jlsd():  # 巨量ip隧道版本
    tunnel = 't101.juliangip.cc:10630'
    # 用户名密码方式
    username = "15817443553"
    password = "Egd12jja"
    proxies = {
        "http": "socks5h://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
        "https": "socks5h://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
    }
    return proxies


# 导入其可支持的浏览器版本指纹，chrome136最稳定
supported_browser_versions = ['chrome136', 'edge101', 'safari184', 'safari184_ios', 'safari260', 'chrome131_android', 'firefox135', 'tor145']
count = 0
while True:
    try:
        count += 1
        time.sleep(random.uniform(0.5, 1))
        url = f"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%8C%97%E4%BA%AC%2B%E5%A4%A9%E6%B4%A5%2B%E7%A7%91%E6%8A%80%2B%E8%80%83%E5%AF%9F&tbs=cdr%3A1%2Ccd_min%3A2024%2Ccd_max%3A2025?{(random.randint(1000000, 9999999))}={(random.randint(1000000, 9999999))}"
        print(url)
        logger.info(1)
        response = requests.get(url=url, headers=headers_bd, impersonate=random.choice(supported_browser_versions), verify=False, timeout=60)
        logger.info(2)
        print(len(response.text), count)
    except Exception as e:
        print(str(e))
        pass
