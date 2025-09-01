import requests


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "dnt": "1",
    "priority": "u=0, i",
    "referer": "https://mp.weixin.qq.com/mp/wappoc_appmsgcaptcha?poc_token=HDkQsWijsufJdF7gt0yPuAMIwijckvLu2BGMvz7G&target_url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzkyODg2NTc1MA%3D%3D%26mid%3D2247486018%26idx%3D1%26sn%3D22352719a62ea115f14219d616e9dab9%26scene%3D0",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}
cookies = {
    "rewardsn": "",
    "wxtokenkey": "777",
    "poc_sid": "HAEQsWijjXng7DGOBN9hLSVMXnRypmehochx1-Yh"
}
url = "https://mp.weixin.qq.com/s"
params = {
    "__biz": "MzkyODg2NTc1MA==",
    "mid": "2247486018",
    "idx": "1",
    "sn": "22352719a62ea115f14219d616e9dab9",
    "scene": "0",
    "poc_token": "HDkQsWijsufJdF7gt0yPuAMIwijckvLu2BGMvz7G"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)