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