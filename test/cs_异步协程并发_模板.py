import asyncio
import random
import time

import aiohttp

# 配置参数
CONCURRENCY_LIMIT = 5  # 并发限制数量
TOTAL_REQUESTS = 200  # 总共要发送的请求数量
REQUEST_TIMEOUT = 30  # 请求超时时间（秒）

# 全局计数器
request_count = 0
success_count = 0
failure_count = 0

def edge_random_headers(url):
    # 生成随机版本号 (100-120之间的偶数)
    edge_version = random.choice(range(100, 121, 2))
    chrome_version = edge_version - random.randint(0, 10)  # Chrome内核版本通常略低于Edge版本

    headers = {
        "Connection": "close",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "accept-language": random.choice(['zh-CN,zh;q=0.9', 'en-US,en;q=0.9', 'en-GB,en;q=0.9']),
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer":url,
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


def random_headers():
    v4 = random.choice([6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": random.choice(['zh-CN,zh;q=0.9', 'en-US,en;q=0.9', 'en-GB,en;q=0.9']),
        "Connection": "keep-alive",
        "DNT": "1",
        "Referer": "https://www.amazon.com/",
        "Sec-Fetch-Dest": "iframe",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Storage-Access": "none",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "sec-ch-ua": f"\"Not)A;Brand\";v=\"{v4}\", \"Chromium\";v=\"138\", \"Brave\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        str(random.randint(1000000, 9999999)): str(random.randint(1000000, 9999999))
    }
    return headers
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "dnt": "1",
    "priority": "u=0, i",
    "referer": "https://www.bol.com/nl/nl/p/kambukka-elton-geisoleerde-waterfles-600ml-nightfall-met-3-in-1-lid-en-makkelijke-reiniging-drinkfles/9300000170954356/?bltgh=6a854ad0-f73b-4417-a95c-3ab33a99be9f.ProductList_Middle.0.ProductTitle&cid=1756706394704-8742932725322",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}
cookies = {
    "_abck": "27EDAC15B6A99D874E39C6D44ACBABC0~-1~YAAQHE5DF/0AUPOYAQAAKqTNFw6ubL94DiS7cdA62toZrFmeYHBv6bAUkIsWSBAQmPXvLUW1aNBOzbxPaHNIG7llYwVkQ0g+pOrL+Vxi07tTOBikdFGw5ONoReSqUdbyAjNnnPpbalvPZ4DCQmOT/GVMyiVVWxKVSRIT/QvVcjETfWijlv6BFR4nTTgo35ySvgtQ4YFl5j0/DVNIbYEuwjW6s5JEYYhqecG2Qg2hmqQxcb1jD3Vy1szayjG1b5gdJjejLQgX/+UiNIRxHpC8r28ed/I5gl1u4p+lOhf8brl83R2qGGqaF9OEZM/Gzjq7w5Pt9tyYQn+PND6ofYWcuwMbx6YvkERBCkHmDkwNyzVLoBpCfYrvpDsmqbNItkEhg598PHVjQIUMoO/b/yz6fjzXjLn7+PxOjQP8i/kiNKyPDv1BbtdWQ8KWkJ9HtCuLIWpErvs=~-1~-1~-1~~",
    "ak_bmsc": "5F29ED7EA0A115DD54F35730D87BD321~000000000000000000000000000000~YAAQSj0xF4Veyw6ZAQAAPePOFx10SZi8YQHI+xDjR2GDRu8H+NLZL9XE/qp6cSCoyKvSXmTFtDvjlkY+ScIatsSuB/B19FbrvKl8cqg7Y8CC/FxntfSMzrWVsK9b2WcNvanvuJ4WBje1DF/3bWDoBWqtHAtL0w/5gyJcFNcZecs2QRpngKd4Gs8a7pxV/taggv7+UunNPmAU2pCKB8iQBz8Ix+W/xVBJxq3V3NY4wI9Hlzw82x+tvcrd0A5CctTAYojDAX4DO9w3JA9NSajPUKryhfyI6loLFGW4Ogy/tpVoISG9k5eUNC1jK5DljlbGgRudSguVBlXAAXHR1Jr/U2EueP+2Q31gkcVBg7x9q3f2h9aFPSzstzz9/8+ayeQ=",
    "BUI": "e91623f6-9d20-415a-a56a-62e11304daec",
    "XSC": "wYT9xb0mWSPzr4H8ERayJI8ypTY0XnVy",
    "bltgSessionId": "c8b31b21-c355-41bf-a2f1-ed2e019b9725",
    "XSRF-TOKEN": "e1f82f3a-f006-4e80-bd03-6be26311f895",
    "locale": "NL",
    "language": "nl-NL",
    "rl_anonymous_id": "RS_ENC_v3_ImU3ZTRjMGIzLTFjY2YtNDNjOS1hZTE2LWRiNDQwOTY3OWNhMCI%3D",
    "rl_page_init_referrer": "RS_ENC_v3_Imh0dHBzOi8vd3d3LnRhcGQuY24vIg%3D%3D",
    "rl_page_init_referring_domain": "RS_ENC_v3_Ind3dy50YXBkLmNuIg%3D%3D",
    "rl_trait": "RS_ENC_v3_eyJzaG9wQ291bnRyeSI6Im5sIiwic2hvcExhbmd1YWdlIjoibmwiLCJyZWNvZ25pdGlvblR5cGUiOiJhbm9ueW1vdXMiLCJjbGllbnRJZCI6ImU5MTYyM2Y2LTlkMjAtNDE1YS1hNTZhLTYyZTExMzA0ZGFlYyJ9",
    "bolConsentChoices": "source#OFC|version#6|int-tran#true|ext-tran#true|int-beh#true|ext-beh#true",
    "_fbp": "fb.1.1757041076534.237363219229170694",
    "_ga": "GA1.1.1302409001.1757041077",
    "_gcl_au": "1.1.1096073821.1757041077",
    "ga_session_id": "1757041076",
    "ga_client_id": "1302409001.1757041077",
    "sbsd_o": "2F3CEA2AFF0332730E1F49E18B925A8B075A9B5EBDE97A73492E564226EDC858~sK/JcaaKlBZhefjI/qlIVZvc7nHpi4hG/j5LXlWxcuFezTCo7KhSKkFkMNwtXLmlVHntMKWFYtph/+rI9aFOlPmmkLROkB4ieo0gx6CVRiq5SUEjGYgE5h+LlTyWbX+YMOSaIudYlmJvzRsNpiu17sdRdPW9oorsUBfXM9XPuSxN+FKBmhycFoTnwsd48T4eINQK2FaNJk9zKv51JOEW4dITe340AEqGNJHpC1j2y9xc=",
    "bm_lso": "2F3CEA2AFF0332730E1F49E18B925A8B075A9B5EBDE97A73492E564226EDC858~sK/JcaaKlBZhefjI/qlIVZvc7nHpi4hG/j5LXlWxcuFezTCo7KhSKkFkMNwtXLmlVHntMKWFYtph/+rI9aFOlPmmkLROkB4ieo0gx6CVRiq5SUEjGYgE5h+LlTyWbX+YMOSaIudYlmJvzRsNpiu17sdRdPW9oorsUBfXM9XPuSxN+FKBmhycFoTnwsd48T4eINQK2FaNJk9zKv51JOEW4dITe340AEqGNJHpC1j2y9xc=^1757042791111",
    "shopping_session_id": "e6c3aca873daf76d026e5ba10cd299e99301d6802f18e91bc5f4a209040a8b0d",
    "sbsd_c": "4~1~277307388~pllhXQD+N/C84eMSjwr5oeETTgiG17te7btK3X1TD00Mze9lRDpDs86iMRnz7O5JmtQnh9E42zQuv2J/MZqa86DfjDEzz6xIddaaZsfP4yE3kFi3GgoA8BLIVPEfezGTI2LB+rQxXTkojEBpYzMfV2KUTDLrqU3i/qYYPqUUytuXKDJNTTwzaWZrqXUqRY+YFRw3Lluy/a5KzSMt6/9C2u5j9WPj5PeohklEz5UY13KUAwLqN/vhjY7pUYg5wXKQRSjBTDI48mzArhbSSAiaBlvlRbv5wxZC2mq/RAuuolIlWkFboO8UzUyNfnZ5aSJnThHcYcAknUsVkUnLxRncCmPcn8dhR7DkT2egq7KqJvBh+7Yu8sIVp5Uny6k9zqR4q7xKIMz5ovxK4ZOfyPe+8ztoSALkEEKk1xq7UKjfbpifo/XCocV9fpI/Zt4TA6JIONRLfwSHQgmYie/bkHiBt5bKnd0mRzRzOrY7PQ9jS6KTeBnMp36jzChIG2igeWZFiewddH7ZtSoRuVx0qZfGgfwXiip5N0Zjh3p7y/s5lfnJ44m9P6AOdS7gAGr2t0l2EzXoWY2RKTEphojd1Ge0DO+xC+y5oDulVRmaUL4qunZ7ix6KVMXPGPkAnsXFdAwSx2L+47Wfs7atShO8b0uzUXUXlG92y5nQZXG3qHr8BabBGP/lzr32eUR8lMNOPkPIvvF+fDLMkLuM9szjtwut4rTg==",
    "sbsd": "s5OzvPoInUMekE5PGMKxHJBSTlIInUjCyB8ROJ4Dhrx6C6iN9EpCDMra2xI7YcrL/0qO+ZyEyJoQEy60xrQ4pc012vePRWpI1yN+ZQorIF6XiQYeedkpxwQ/2ZTBoD1UK8zZ7oRU11635gxyOIee6i5gfR4CjIGkjLde86sFS+gEj1wJDWZxbXnP3rwjSCkAO9XZod4+dwv/s1DVw4dwa2pjjSHEeiL7zrS0d4oWeTxKGLGpxaRtcez18JPMcdwM9o6JDrpEE/jDomspECdOsY3ST0CRLa97xPJPUYfEwp5+6ZsA14X46xwU6849TkIQw+Gl5Mlepc9nHLaWb7WUSYaJGGa2zgSnY6ryULDQhGaXNbbMEZTJoi/M880KaNhcuACZmnT/19pY1F6jbYjjDM8fNVdTc0P2ByR1mdfPyv+4=",
    "bm_sz": "8C776D7CC5516E21C1DB66EA56A7EFDB~YAAQfhQgFzGkbQ2ZAQAAMVjpFx3pL1AuenK9B6QqDDkccpuRxC8ar8Ur5ubVzIb3yibTyMmqoki7UtNPxGNbOb/cc1TiegTrCNidvpiRl14mupbzgA6Bpt/HmjgtAEs4Tl+S4NYqIEXcf9ivDHp0CBy8wPRGY6aObXDvF93LbPuaS4mMS47Oc6TvYRx4MkLCFyrM/hOLnWuVfpif1rkcU38ml0+gfp5xdrruPDbbYv5ZYUdjMBetx9YtagiuLyEfZAJaHCGcumS8yg8I3PALo5SzQNqrwPzOIZCSyrZtu3NiPqT9iGFnHZxp8nIoMJSlgmbcUF4Mn6H75nf0XwOGRVgWUC6EtZU8tXptpGSsf4lRthH2uA8QYDCUpQ+MoVCKimNqdRDC1gYPt7dll+PtBuXsJTM9Pj2Cei7Nu6tVd471dAqqaLRol3OIF9kOE7HQQ+wkqPeTBDW1mgx5dJtrm6pUyqGfp7MselxbXoSqHBUft0/BtklZOggLCY4YRQ==~3228230~3224632",
    "_uetsid": "1fb1f1908a0411f09ba9dd10b6fc22a8",
    "_uetvid": "1fb1e8908a0411f0bba1bb1df61e1184",
    "_ga_MY1G523SMZ": "GS2.1.s1757041076$o1$g1$t1757042792$j19$l0$h0",
    "__eoi": "ID=e68afa8d0a912969:T=1757041195:RT=1757042793:S=AA-AfjZI_9LoCKiPhNvSNf6J-ebI",
    "P": ".wspc-deployment-74b7bb65b7-r9flq",
    "bm_sv": "E99FBAA6C0AA4CDA1756DE93A0DD804E~YAAQfhQgF6ekbQ2ZAQAAWdnpFx3yg0oKgb7jxF36s0cEbVjUprIqdG1vZ4L+2lB/AaLmw4zMKsTPhp9o/NMuJEcYX0haOh1JwqHIHFdpsyJ+r0PxYQYrMr2Z7JBQgBy2h+RSnpyokdxbS5/e5JhX4edgg1os8qCVzKx79OL9JktM1yP5ezzooMIraFkzwGDhXtxISlNCZkxHawN54pVSg/Azje1Hvnichwot+kxR38gsaX2bbojnsZAstWl92Q==~1",
    "rl_session": "RS_ENC_v3_eyJpZCI6MTc1NzA0MTA2MTUzMSwiZXhwaXJlc0F0IjoxNzU3MDQ0NzE2NjMyLCJ0aW1lb3V0IjoxODAwMDAwLCJhdXRvVHJhY2siOnRydWUsInNlc3Npb25TdGFydCI6ZmFsc2V9"
}


def proxy():  # 快代理 隧道 海外
    # 隧道域名:端口号
    tunnel = "us.h177.kdlfps.com:18866"

    # 用户名密码方式
    username = "f2641409405"
    password = "sb5j81g0"
    proxies = {
        "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
        "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
    }
    return proxies


async def fetch(session, semaphore):
    """异步获取页面内容"""
    global request_count, success_count, failure_count

    async with semaphore:
        try:
            # 随机延迟 (0.5-1秒)
            await asyncio.sleep(random.uniform(0.5, 1))

            # 发送异步请求
            async with session.get(url, timeout=REQUEST_TIMEOUT, proxy=proxy()['http']) as response:
                html_text = await response.text()
                len_text = len(html_text)

                # 更新计数器
                request_count += 1

                # 检查响应长度是否小于10万字节
                if len_text < 100000:
                    failure_count += 1
                    print(f"{request_count} 次:请求失败（长度不足）: {len_text} 字节")
                    return False
                else:
                    success_count += 1
                    print(f"{request_count} 次:请求成功: {len_text} 字节")
                    return True
        except Exception as e:
            # 更新计数器
            request_count += 1
            failure_count += 1
            print(f"请求出错: {e}")
            return False


async def worker(session, semaphore):
    """执行单个任务"""
    return await fetch(session, semaphore)


async def main():
    """主协程"""
    global request_count, success_count, failure_count

    # 创建连接池和信号量
    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)

    start_time = time.time()
    connector = aiohttp.TCPConnector(limit=20, limit_per_host=5)  # 全局最大连接数20，单个主机最大5

    # 创建会话
    async with aiohttp.ClientSession(
            connector=connector,
            headers=headers,
            # cookies=cookies
    ) as session:
        # 创建任务列表
        tasks = [asyncio.create_task(worker(session, semaphore)) for _ in range(TOTAL_REQUESTS)]

        # 等待所有任务完成并获取结果
        results = await asyncio.gather(*tasks, return_exceptions=False)

    # 计算耗时
    end_time = time.time()
    total_time = end_time - start_time

    # 计算成功率
    success_rate = (success_count / request_count) * 100 if request_count > 0 else 0

    # 打印统计信息
    print("\n" + "=" * 50)
    print(f"总请求次数: {request_count}")
    print(f"成功请求: {success_count}")
    print(f"失败请求: {failure_count}")
    print(f"成功率: {success_rate:.2f}%")
    print(f"总耗时: {total_time:.2f}秒")
    print(f"平均每秒请求数: {request_count / total_time:.2f}")
    print(f"实际并发效率: {request_count / total_time / CONCURRENCY_LIMIT:.2f}倍")
    print("=" * 50)


if __name__ == "__main__":
    url = "https://www.bol.com/nl/nl/p/kambukka-elton-geisoleerde-waterfles-600ml-nightfall-met-3-in-1-lid-en-makkelijke-reiniging-drinkfles/9300000170954356/"
    asyncio.run(main())
