import json

import requests
from lxml import html

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "dnt": "1",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://mobile.pinduoduo.com/index.html?_x_query=%E5%A1%91%E6%96%99%E5%91%A8%E8%BD%AC%E7%AE%B1&refer_page_name=personal&refer_page_id=10001_1762496485483_30aw73nff5&refer_page_sn=10001&item_index=2&count=8&sp=1120&mlist_id=0enpga3g5t&last_goods_id=816442974746&page_id=10002_1762496548751_cah2bpgr0v&is_back=1&bsch_is_search_mall=&bsch_show_active_page=&list_id=b1rzx4lhkl",
    "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}
cookies = {
    # "api_uid": "CisCd2kMUiShBACThuJTAg==",
    # "_nano_fp": "XpmjX5TanpgqlpPxX9_2TR3UQF4T6r1idqB~885K",
    # "webp": "1",
    # "jrpl": "ngLUsTjibLMcnyut1FsCcL9awfKjf6hS",
    "njrpl": "ngLUsTjibLMcnyut1FsCcL9awfKjf6hS",
    # "dilx": "xfzCAXL1SOsNN4vCKtpX1",
    "PDDAccessToken": "5RDL3GWBGOABM6QK3F3YOHMISK6B55LT5DLIDCUEADKJ2HOMK3LA123d1a9",
    # "pdd_user_id": "1876545246161",
    # "pdd_user_uin": "ICAYJDEEP6XEXOZM6ICCDWIX5I_GEXDA",
    # "pdd_vds": "gaLeNNOsEsnwyymOtbQlPmNOONnOomIdOOGloynOiuibblNdNLodiOndbnGu"
}

url = 'https://mobile.pinduoduo.com/goods.html?goods_id=569251152502&_oak_rcto=YWIG4Iuqd5inbC0twb7CTAi4KOA84MY5FzKYUDjBkmkvOA256kam3NSo&_oc_trace_mark=199&_oc_adinfo=eyJzY2VuZV9pZCI6Mn0%3D&_oak_gallery=https%3A%2F%2Fimg.pddpic.com%2Fmms-material-img%2F2023-12-19%2F928b6943-b9c1-44ac-8403-8a8e544f42f8.jpeg&_oak_gallery_token=50c1de4b730e3502d68dd09e011b3319&_oc_refer_ad=1&_oak_search_term=%E5%91%A8%E8%BD%AC%E7%AE%B1&_x_query=%E5%91%A8%E8%BD%AC%E7%AE%B1&refer_page_el_sn=99369&refer_rn=&page_from=23&refer_page_name=search_result&refer_page_id=10015_1762266674760_56qorp6wr8&refer_page_sn=10015&uin=ICAYJDEEP6XEXOZM6ICCDWIX5I_GEXDA'

response = requests.get(url, headers=headers, cookies=cookies)
print(len(response.text))
tree = html.fromstring(response.text)
json_data = tree.xpath('//script[starts-with(normalize-space(text()), "window.rawData=")]/text()')
json_data = json_data[0].strip()[len('window.rawData='):][:-1]
json_data = json.loads(json_data)
skus_list= json_data["store"]["initDataObj"]["goods"]["skus"]
# 或者如果你想要按规格类型分别存储：
i=0
for sku in skus_list:
    i+=1
    sku_id = sku["skuId"]

    # 创建字典存储所有规格
    spec_dict = {}
    for spec in sku["specs"]:
        spec_dict[spec["spec_key"]] = spec["spec_value"]

    # 现在你可以通过键名访问特定规格
    color = spec_dict.get(f"款式")
    size = spec_dict.get("尺寸")
    groupPrice = sku["groupPrice"]

    print(f"{i}: SKU ID: {sku_id}, 颜色: {color}, 尺寸: {size}, 组合价格{groupPrice}")