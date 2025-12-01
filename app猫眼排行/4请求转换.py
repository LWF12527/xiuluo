import re
from urllib.parse import urlparse, parse_qs


def http_to_requests(http_text):
    """将HTTP请求文本转换为Python requests代码"""

    # 解析请求行
    lines = http_text.strip().split('\n')
    method_line = lines[0]

    # 提取方法和URL
    method_match = re.match(r'^(GET|POST|PUT|DELETE)\s+(.+?)\s+HTTP/', method_line)
    if not method_match:
        raise ValueError("无法解析请求行")

    http_method = method_match.group(1)
    full_url = method_match.group(2)

    # 解析URL和查询参数
    parsed_url = urlparse(full_url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}" if parsed_url.scheme else full_url
    query_params = parse_qs(parsed_url.query)

    # 简化参数值（取第一个值）
    params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}

    # 解析请求头
    headers = {}
    for line in lines[1:]:
        if not line.strip():
            break  # 空行表示头部结束
        if ':' in line:
            key, value = line.split(':', 1)
            headers[key.strip()] = value.strip()

    # 生成Python代码
    code = f"""import requests

url = "{base_url}"
params = {params}
headers = {headers}

response = requests.{http_method.lower()}(
    url=url,
    params=params,
    headers=headers
)

print(f"状态码: {{response.status_code}}")
print("响应内容:")
print(response.text)
"""

    return code


# 使用示例
http_request =\
"""GET https://npro.maoyan.com/api/ncinema/box/cinema/follow.json?type=0&beginDate=20251125&isSplit=0&cityId=0&filterJson=%7B%7D&utm_term=8.12.0&utm_source=xiaomi&utm_medium=android&utm_content=2021BCA31F590CF&movieBundleVersion=8012001&utm_campaign=AmovieproBmovieproCD-1&pushToken=dpsh8407478445097dc81c45d126a8e8f98eatpu&uuid=0000000000000280CD8E870034B1C935885792E216204A176403058303035387&deviceId=2021BCA31F590CF&riskLevel=71&optimusCode=10&language=zh&channelId=40004 HTTP/1.1
Accept-Encoding: gzip
Connection: Keep-Alive
Content-Type: application/json
Host: npro.maoyan.com
M-SHARK-TRACEID: 5310000000000000280CD8E870034B1C935885792E216204A1764030583030353874caf9c176412081619621c9fe
clientType: myPro
mtgsig: {"a0":"3.0","a1":"0a03b816-c295-46cc-ad01-f2a3704ce24f","a3":25,"a4":1764120816,"a5":"BwfRu9vgI5RU9CzYVKA7RoFW0MLbGpyM1n8y/soXG2wuRxsNudgFeAcy8WKIud/urjqIsLDlByDyFDdibz6S/8OKd+Te9bZtwS6ntVUBg5+z2OLJHoC041vn4PA/pr2YnOamGYpM2HaftCdGEJyabgXfv7U48VIxHkh6TnegncnLW9ZlEXvgGX2sb4YzVP9ZtDRpMj/OAlBZCEMfiup4UKS67UAwC/64aK8Bi118Tyn1hL80+gFGqS0lbCRoueQrJZxk8hVilbI7TDoRe9xgkTax9dPPGjXl4NbqXK3+e4KsQujXViodea22XflsLx2SFO6AKNMs89VGnR0rQcUQ6HnhC/UOxXdlu0bTVYamAXV9t918kumnbb0o43VAS/EMwaAGjQC+bvglpo/scqnAvrCLBhupQg==","a6":0,"a7":"8HvQbR9Vh5e0muGqudzLTmN3/2flOFFJCIKIFip8zC4q4c+aLh9z7fbuz5rqeykLYlWgbqI9kygl74RqZ/INUDod+hdkx+EG40/yf81YtA8=","a8":"0e1d7dd3b1b8c9f62dae11157942f554edd5f7d8dd70d8e7b2d837a9","a9":"de0a27d0oVZPIK/OJbEA+dy0cln1EZS0Tc8dfTmvskG5HfdGvqVbVhQXeff5d6X+KibubcBTfiJBWp2npriXvNEi6xLcoDVsUqs0UzhnncLl8raUgnTjYP/llqgNedT2284oM0mYXObQ2diAfXDqEUOdeQgmjYFI1eRMEb9UyGcDiTAb/S5lOrLkDO159O1rzdx6IN8kIMRzXfj973mde04ENNOUR6D8hTmxgGyBXVW23jBP/9fF8pZKZqxlq3mzadydV7LoG2C4l89RqoVhtLVp+kHw7JuLyi7FG9GW9M74dPvW+YT9D1AckRbxdwLR9xFTJzDrWsEmZXt9GSsY/bMUC2GnKbo428uOyuleI8WlFYy7d/thPoXQJxipTWIXDEzgk2z5UErz2Z+B3vzzkqEYuXEnT993XYZ00smAgYjnZ9e9emUXka22vOz++kQdlwpwNfgOo+9bOm4qQZ5XlPPZVdFZlwmRZarEaxcT8t9EDeb/wfubQved+7nqrm9+fOb3s/F9fEOpqtE77SXutOgQeq+S25k72ncD0rBUdLLDIPuqEe9Ce/Q6k5i62A5+gKryvK/zhuKEruBedZ8F51Xsd5IMLHe+Sqf3yep3/q8zyRqT9erl8sB6EXWfzwTonzs93pKkYOE7ZukElGtI5+sDYrsoVBx6W7Db8s4lPcgwSsDghl2rYuHZFMIVcQ/sosnpmu1yp8uCDlF0kZHuk8vu9gvScFiU7aIN/R7HPbdf6nXfZUe9rUUPFEnfSSmJJkaKXqOl+SltaQfqJC48zU/je/5c2ePMvmNa6IEYK17pMGjQeEEc0P8nGnD4RVF5C5QKTDnSkG0HkFLN9wBxX0TBj7m+RMwpeVDPd/C1h4GP5Qa4IJSGI1+mGW9VBfngdpHZGQRT/hsw5qcyLl3Sqf1ngYIo6qJJLe1ai515Ti+cjEc8ny1MGATaeRPEyPUki2LYKKI52JEof6rG0c/zJKC5fLB6kUQQGKkRKVns8YoFA5fC5vk=","a10":"6,96,1.1.1","x0":1,"a2":"d73e4e3faeaa5a576cc5ee17930786b5"}
retrofit_exec_time: 1764120816193
token: b_maoyan_eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3NjQwNjM5NDMsIm5iZiI6MTc2NDA2Mzk0MywiZXhwIjoxNzc5NjE1OTQzLCJkZXZpY2VUeXBlIjoxLCJzYWx0IjoicUplTWFvIiwiaXNUZXN0IjpmYWxzZSwidXNlcklkIjo3Njc5OTkwMDIsInV1aWQiOiIwMDAwMDAwMDAwMDAwMjgwQ0Q4RTg3MDAzNEIxQzkzNTg4NTc5MkUyMTYyMDRBMTc2NDAzMDU4MzAzMDM1Mzg3IiwidmVyc2lvbiI6IjEuNyIsImNoYW5uZWxJZCI6NDAwMDR9.838UGydSwAyppxUxKMrBoVlkLaJiqKqyp4WePomCiNQ
user-agent: Dalvik/2.1.0 (Linux; U; Android 9; 2311DRK48C Build/PQ3A.190605.09261140)
userid: 767999002
yodaReady: native
yodaVersion: 1.18.0.272
"""

# 替换链接为实际域名
http_request = http_request.replace("链接", "https://npro.maoyan.com")

python_code = http_to_requests(http_request)
print(python_code)