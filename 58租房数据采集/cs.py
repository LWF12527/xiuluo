import requests


def proxy():  # 巨量ip国内版——包量
    proxy_url = 'http://v2.api.juliangip.com/dynamic/getips?auth_info=1&auto_white=1&filter=1&num=1&pt=1&result_type=text&split=1&trade_no=1908141527512576&sign=e0bf8f4983949e1c22b65437e1ec204f'
    proxy_str = requests.get(proxy_url).text
    print(proxy_str)
    proxy_str_list = proxy_str.split(':')
    proxy_ip = proxy_str_list[0] + ":" + proxy_str_list[1]
    username = proxy_str_list[2]
    password = proxy_str_list[3]
    proxies = {
        "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
    }
    return proxies
print(proxy())