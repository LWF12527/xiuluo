import random

from fake_useragent import UserAgent

# 随机请求头
User_Agent = UserAgent().random


def random_headers_enhance():
    v1 = random.randint(557, 600)
    v2 = random.randrange(110, 160, 2)
    v3 = 36 or random.randrange(6, 50, 2)  # 常见36
    v4 = random.choice([6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])
    headers = {
        "sec-ch-ua": f"\"Not=A?Brand\";v=\"{v4}\", \"Chromium\";v=\"{v2}\", \"Google Chrome\";v=\"{v2}\"",
        "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/{v1}.{v3} (KHTML, like Gecko) Chrome/{v2}.0.0.0 Safari/{v1}.{v3}"
    }
    headers = {
        "accept": "text/html,application/xhtml+xml;q=0.3,application/xml;q=0.9,image/avif,image/webp;q=0.2,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "device-memory": "8",
        "downlink": "1.4",
        "dpr": "1",
        "ect": "4g",
        "priority": "u=0, i",
        "rtt": "400",
        "sec-ch-device-memory": "8",
        "sec-ch-dpr": "1",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-ch-ua-platform-version": "\"15.0.0\"",
        "sec-ch-viewport-width": "1920",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "viewport-width": "1920",
        **headers
    }
    return headers


def cf_random_headers(self, url):
    # 随机生成设备像素比 (常见范围0.5-3.0，保留两位小数)
    dpr = round(random.uniform(0.5, 3.0), 2)
    # 随机生成网络下行速度 (0.5-100 Mbps，保留两位小数)
    downlink = round(random.uniform(0.5, 100.0), 2)
    v4 = random.choice([6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])
    headers_or = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "dnt": "1",
        "priority": "u=0, i",
        "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
        "sec-ch-ua-arch": "\"x86\"",
        "sec-ch-ua-bitness": "\"64\"",
        "sec-ch-ua-full-version": "\"140.0.7339.208\"",
        "sec-ch-ua-full-version-list": "\"Chromium\";v=\"140.0.7339.208\", \"Not=A?Brand\";v=\"24.0.0.0\", \"Google Chrome\";v=\"140.0.7339.208\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": "\"\"",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-ch-ua-platform-version": "\"15.0.0\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
    }
    headers = {
        "apollographql-client-name": "spartacux-b2c",
        "apollographql-client-version": "1.0",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Connection": "close",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "sec-gpc": "1",
        "upgrade-insecure-requests": "1",
        **headers_or,
        f"x-rand{random.randint(100, 999)}": str(random.randint(1000000, 9999999)),
        "sec-ch-ua": f"\"Not)A;Brand\";v=\"{v4}\", \"Chromium\";v=\"138\", \"Brave\";v=\"138\"",
        "accept-language": random.choice(['zh-CN,zh;q=0.9', 'en-US,en;q=0.9', 'en-GB,en;q=0.9']),
        "downlink": str(downlink),  # 动态下行速度
        "dpr": str(dpr),  # 动态设备像素比
        "referer": url,
        "user-agent": UserAgent().random,
    }
    return headers


def edge_random_headers(url):
    # 生成随机版本号 (100-120之间的偶数)
    edge_version = random.choice(range(100, 121, 2))
    chrome_version = edge_version - random.randint(0, 10)  # Chrome内核版本通常略低于Edge版本
    dpr = round(random.uniform(0.5, 3.0), 2)

    # 随机生成网络下行速度 (0.5-100 Mbps，保留两位小数)
    downlink = round(random.uniform(0.5, 100.0), 2)
    headers = {
        "Connection": "close",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "accept-language": random.choice(['zh-CN,zh;q=0.9', 'en-US,en;q=0.9', 'en-GB,en;q=0.9']),
        "cache-control": "max-age=0",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "downlink": str(downlink),  # 动态下行速度
        "referer": url,
        "dpr": str(dpr),  # 动态设备像素比
        "sec-ch-ua": f"\"Microsoft Edge\";v=\"{edge_version}\", \"Chromium\";v=\"{chrome_version}\", \"Not?A_Brand\";v=\"8\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "sec-gpc": "1",
        "upgrade-insecure-requests": "1",
        "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36 Edg/{edge_version}.0.0.0",
        # 随机生成的自定义头
        str(random.randint(1000000, 9999999)): str(random.randint(1000000, 9999999))
    }
    return headers


def us_random_headers(url):
    # 随机生成设备像素比 (常见范围0.5-3.0，保留两位小数)
    dpr = round(random.uniform(0.5, 3.0), 2)

    # 随机生成网络下行速度 (0.5-100 Mbps，保留两位小数)
    downlink = round(random.uniform(0.5, 100.0), 2)
    # us不更新浏览器版本，成功率90
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": random.choice(['zh-CN,zh;q=0.9', 'en-US,en;q=0.9', 'en-GB,en;q=0.9']),
        "cache-control": "max-age=0",
        "dnt": "1",
        "downlink": str(downlink),  # 动态下行速度
        "referer": url,
        "dpr": str(dpr),  # 动态设备像素比
        "priority": "u=0, i",
        "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
        # 添加随机噪声头防止指纹固定
        f"x-rand{random.randint(100, 999)}": str(random.randint(1000000, 9999999))
    }
    return headers
