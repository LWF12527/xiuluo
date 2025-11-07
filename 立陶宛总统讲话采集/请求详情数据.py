headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "dnt": "1",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"141.0.7390.123\"",
    "sec-ch-ua-full-version-list": "\"Google Chrome\";v=\"141.0.7390.123\", \"Not?A_Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"141.0.7390.123\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"15.0.0\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}
cookies = {
    "cf_clearance": ".454lTl.YlxNS6pkuFA1e6abDmivKKhUudjdjyQC7xA-1762412532-1.2.1.1-HS5ZFSxWwncE1PffXAOlAva4pLT.68S7EteJsqgRntqA0BytzYgG8h7d9WUrGceugntTIixVtWoF2YBJ6ZibF70XT4UdHhhLI_8_e4b.vjIKNQBvX8p6fUmTn2Fx6pa7a31sUNSQZAnFTcKpfr5O6dAtWfaJ8b0.PaAX73KETFsqsBJESJYe8YEftBT0CBTwsHtmpmmpcn67agGEHC6BaIhMvgOJ.or_TUoHISIU318"
}

# 页面增量-请求-获取文章链接-获取下一页链接--请求-获取文章链接
add_url_list1_map = {
    "https://archyvas.lrp.lt/adamkus/sarasas15ee.html?nuo=1&kat=4&search=": "LT",
    "https://archyvas.lrp.lt/adamkus/en/sarasasdd13.html?nuo=1&kat=12&search=": "EN",
    "https://archyvas.lrp.lt/paksas/sarasas8710.html?kat=4": "LT",
    "https://archyvas.lrp.lt/paksas/en/sarasasdd13.html?nuo=1&kat=12&search=": "EN"
}

# 关键词增量年份--请求后-提取每年-请求-提取每个文章链接
add_url_list2_map = {
    "https://grybauskaite.lrp.lt/en/activities/speeches/6590/2009-11": "EN",
    "https://grybauskaite.lrp.lt/lt/prezidentes-veikla/kalbos/6588/2023-06": "LT"
}
# 页面增量2-同1
add_url_list2_map = {'https://archyvas.lrp.lt/adamkus3/en/activities/speeches/p15.html': "LT"}

# 处理add_url_list1_map

