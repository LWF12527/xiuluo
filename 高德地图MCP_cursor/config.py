import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Config:
    # 高德地图API配置
    AMAP_KEY = os.getenv('AMAP_KEY', 'your_amap_key_here')
    AMAP_BASE_URL = 'https://restapi.amap.com/v3'
    
    # API端点
    GEOCODING_URL = f'{AMAP_BASE_URL}/geocode/geo'
    REVERSE_GEOCODING_URL = f'{AMAP_BASE_URL}/geocode/regeo'
    TEXT_SEARCH_URL = f'{AMAP_BASE_URL}/place/text'
    AROUND_SEARCH_URL = f'{AMAP_BASE_URL}/place/around'
    DETAIL_SEARCH_URL = f'{AMAP_BASE_URL}/place/detail'
    IP_LOCATION_URL = f'{AMAP_BASE_URL}/ip'
    
    # 默认搜索参数
    DEFAULT_RADIUS = 3000  # 默认搜索半径3公里
    DEFAULT_PAGE_SIZE = 20  # 默认每页返回数量
