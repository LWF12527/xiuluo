import json
import logging
import random
import re

import requests
from lxml import html

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class BasicMain:
    def __init__(self):
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        ]

    def get_random_user_agent(self):
        return random.choice(self.user_agents)

    def proxy(self):  # 巨量ip国内版——包量
        proxy_url = 'http://v2.api.juliangip.com/dynamic/getips?auth_info=1&auto_white=1&filter=1&num=1&pt=2&result_type=text&split=1&trade_no=1908141527512576&sign=127fe8b1b841e296617fcd765c7af125'
        proxy_str = requests.get(proxy_url).text
        proxy_str_list = proxy_str.split(':')
        proxy_ip = proxy_str_list[0] + ":" + proxy_str_list[1]
        username = proxy_str_list[2]
        password = proxy_str_list[3]
        proxies = {
            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
        }
        return proxies

    def fetch_page(self, url, timeout=10):
        """获取网页内容"""
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "DNT": "1",
            "Referer": "https://hf.58.com/zufang/?PGTID=0d000000-0000-01eb-14df-90ed23d431f4&ClickID=1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }

        try:
            response = requests.get(url, headers=headers, timeout=timeout, proxies=self.proxy())
            # 检测反爬
            if "验证" in response.text or "异常访问" in response.text:
                raise Exception("触发反爬机制")
            return response.text
        except Exception as e:
            logger.error(f"请求失败: {url} - {str(e)}")
            raise

    @staticmethod
    def parse_detail_page(html_content):
        """解析详情页，提取房源信息"""
        tree = html.fromstring(html_content)
        house_list = tree.xpath('//ul[@class="house-list"]/li')
        if not house_list:
            raise Exception("没有找到房源数据！")
        house_detail_list = []
        try:
            max_page_ele = tree.xpath('//li/div[@class="pager"]/a[last()-1]/span/text()')
            max_page = int(max_page_ele[0]) if max_page_ele else 1
            for item in house_list:
                # 提取标题
                title_ele = item.xpath('./div/h2/a/text()')
                title = title_ele[0].strip() if title_ele else ""
                # 没有标题的跳过
                if not title:
                    continue
                # 提取价格
                price_ele = item.xpath('.//div[@class="money"]/b/text()')
                price = float(price_ele[0].strip()) if price_ele else 0.0

                # 提取面积
                area_size_ele = item.xpath('.//div/p[@class="room"]/text()')
                area_size = area_size_ele[0].strip() if area_size_ele else ""
                if area_size:
                    match = re.search(r'(\d+(?:\.\d+)?)\s*(?:㎡)', area_size)
                    area_size = float(match.group(1)) if match else 0.0

                # 提取位置
                location_ele = item.xpath('.//div[@class="des"]/p[@class="infor"]//text()')
                location = "-".join([part.strip() for part in location_ele]) if location_ele else ""

                # 提取图片
                pic_urls_ele = item.xpath('./div/a/img/@lazy_src')
                pic_urls = pic_urls_ele[0] if pic_urls_ele else ''

                # 提取链接
                detail_url_ele = item.xpath('./div/a/@href')
                detail_url = detail_url_ele[0] if detail_url_ele else ''

                house_detail = {
                    "title": title,
                    "price": price,
                    "area_size": area_size,
                    "location": location,
                    "detail_url": detail_url,
                    "pic_urls": json.dumps(pic_urls)  # 图片URL列表转为JSON字符串存储
                }
                print(house_detail)
                house_detail_list.append(house_detail)
            return max_page, house_detail_list
        except Exception as e:
            logger.error(f"解析详情页出错: {str(e)}")
            raise
