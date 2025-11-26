import requests

url = "https://npro.maoyan.com/api/ncinema/box/cinema/area.json"
params = {
    "shadowId": "0",
    "yxId": "0",
    "cityId": "0",
    "cityTier": "0",
    "provinceCode": "0",
    "type": "0",
    "beginDate": "20251125",
    "sortType": "2",
    "isSplit": "0",
    "sourceType": "7",
    "utm_term": "8.12.0",
    "utm_source": "xiaomi",
    "utm_medium": "android",
    "utm_content": "2021BCA31F590CF",
    "movieBundleVersion": "8012001",
    "utm_campaign": "AmovieproBmovieproCD-1",
    "pushToken": "dpsh8407478445097dc81c45d126a8e8f98eatpu",
    "uuid": "0000000000000280CD8E870034B1C935885792E216204A176403058303035387",
    "deviceId": "2021BCA31F590CF",
    "riskLevel": "71",
    "optimusCode": "10",
    "language": "zh",
    "channelId": "40004"
}

headers = {
    "Accept-Encoding": "gzip",
    "Connection": "Keep-Alive",
    "Content-Type": "application/json",
    "Host": "npro.maoyan.com",
    "M-SHARK-TRACEID": "5310000000000000280CD8E870034B1C935885792E216204A17640305830303538742fb101764062560323db348f",
    "clientType": "myPro",
    "mtgsig": '{"a0":"3.0","a1":"0a03b816-c295-46cc-ad01-f2a3704ce24f","a3":25,"a4":1764062560,"a5":"TlNXpsyZJoSofADtWK05+ZfJdOXLEfO62dck5iLSt68qe6KR19L8lw4fmHNtDzu5PfEFnbaJUhTjLwgE1zmB0pCMFFxYinLH5ClLvdflo1kfYMhy8DAAtCUrGrnUsADNBTxyIXB1t87eZA7bWLWSlAvQrS+Wz45zGStgXF63p8q+CbXtcdiOcicvqv2PukI6kxF+0nbgXK0x2dMvvziqAxJgdcj6riTK87ThYCMeuA+/GY3HIVVes8GZZt2rhP6/WsqMmJXLDH7JA9Qip5n6WOPuduNjRZ+KU9N6kNqGnyvdQzL0UmEQQvq3i/T3O//CvJUF2Mb31Hkv8A2hWFwamLxtNFxnboRroF2bZfV4iEZJjvEKMxXbvaJYqz4VNnFxBuuXOiLg","a6":0,"a7":"C0eR4iXrRUbrFOp9w0bdKyvW5inymsk/HpZi7UOW9kQOMsRASANkM44QQ/Xz25KbtX1W7muSg6QRTH6rMK76etQW8mpcDFRXgPXT4gtl6Ck=","a8":"0e1d7dd3b1b8c9f62dae11157942f554edd5f7d8dd70d8e7b2d837a9","a9":"495597ecuW/3gDHerMrfh7yHTh4xgc9wIoc/EsoNY6vkyfR9V4tcRN43ZFj7rdthtaBcAPohlEGNgTs13WtAw872haj/ikCbPbmnsMxJLkeaoXMcmk8svWUhtBePgVLDOvLQpQWllFY9uR7YKUn1AyWN6l+r2x8fxmjHcfB2cvypbU65fZ+Cz1XGet8bT1juDggklPLcSJPp58nOE6BK8/OJ+KH7MSGFdYZgu9SvWixL4XZq3lef+Bauc+ZstL4Y+SP5Jp/0kaWi9+jIvFdTQr4X4FQaEQvteouvw4rTd5VKhXsYqLsOzA37aWBa4zfJz/P8AvR5Zo0pZWVdmBsD3dQKPOo5fHHTz/4RaBjGnxhygnz7x9hLYoH0sEzt8ZE/9SmaZ+Epg2vFlAFGyio8t3QfkF4JG5L83SoLAV1n7GqpsVZeOPAV/iL3xAdH+a/9SrGfdooBGd3d0CVyqayzUeZj+s7gGNJjqcB/ZIC6o3xMhoCJNmhqXOKFqWyFClEuyxAZtOmlWxMYO3BqGiHALifFRH7XI5ivgVCate34J5EtEniMkTz19+XOfonqZxYy5L0AiMXC86BitrqR3g7hmQKhxfXnni0qVM41Wt78dyKyIMOMi3uVdYkVhKXPZTZkZ6pUU+K1Bjkrgw8GLPIFqMnvL30ALMUlI8XNwekMWGRZ601ZR5R5hzs+YNWrwe2vvwUN/Bfdi6KHyWXxxhQD4mQpnkmC3kAXP5imf2Mk6P2ZRmgZ+vT41ayDMTFnEdUVZpk/7vLqrbn62lniHkhPeKBRr19GhrCRoorM2lMJfxZ7lbTYNMqQLjl9HNatt1F5yNB1TFIeNGXUotxllr/M3r5QIujk2LwS9NYNBTNqVpz/vt3nxyx60VV9BxVhIt0NeMBujrCBedA9r8krSr+POw1h3TiOZf4p4GhN2gEd/rQPwzQNrAYWxCe4x+Js/jbQuvnMNxAz","a10":"6,96,1.1.1","x0":1,"a2":"6798fc3769602fbba4b33f6f5c498b2e"}',
    "retrofit_exec_time": "1764062560318",
    "token": "",
    "user-agent": "Dalvik/2.1.0 (Linux; U; Android 9; 2311DRK48C Build/PQ3A.190605.09261140)",
    "userid": "-1",
    "yodaReady": "native",
    "yodaVersion": "1.18.0.272"
}


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

response = requests.get(url, params=params, headers=headers, proxies=proxy_jlsd())
print(response.text)