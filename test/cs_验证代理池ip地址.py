import json
import requests


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

def proxy_qgsd():  # 青果代理-全球隧道版本
    tunnel = 'overseas-us.tunnel.qg.net:17814'
    username = "37904CA3"
    password = "5F28FFCEB995"
    proxies = {
        "https": "socks5h://%(user)s:%(pwd)s:A%(area)d@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel, "area": 991900, },
        "http": "socks5h://%(user)s:%(pwd)s:A%(area)d@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel, "area": 991900, }
    }
    return proxies

def html_get():
    headers = {
        "Connection": "close",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "dnt": "1",
        "priority": "u=0, i",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }
    url = 'https://httpbin.org/ip'
    ip_con = requests.get(url=url, headers=headers, proxies=proxy_qgsd())
    return json.loads(ip_con.text)["origin"]


if __name__ == "__main__":
    # 创建空列表存储所有IP
    ip_list = []

    while True:
        ip = html_get()
        print(ip)  # 实时打印当前获取的IP
