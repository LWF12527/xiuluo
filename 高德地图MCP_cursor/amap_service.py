import requests
import json
from typing import List, Dict, Optional, Tuple
from config import Config

class AmapService:
    """高德地图API服务类"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or Config.AMAP_KEY
        if not self.api_key or self.api_key == 'your_amap_key_here':
            raise ValueError("请设置有效的高德地图API密钥")
    
    def _make_request(self, url: str, params: Dict) -> Dict:
        """发送API请求"""
        params['key'] = self.api_key
        params['output'] = 'json'
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API请求失败: {e}")
    
    def geocode(self, address: str, city: str = None) -> Optional[Tuple[float, float]]:
        """地理编码：将地址转换为经纬度"""
        params = {
            'address': address,
            'city': city or ''
        }
        
        result = self._make_request(Config.GEOCODING_URL, params)
        
        if result['status'] == '1' and result['geocodes']:
            location = result['geocodes'][0]['location']
            lng, lat = map(float, location.split(','))
            return lng, lat
        
        return None
    
    def reverse_geocode(self, lng: float, lat: float) -> Optional[str]:
        """逆地理编码：将经纬度转换为地址"""
        params = {
            'location': f'{lng},{lat}'
        }
        
        result = self._make_request(Config.REVERSE_GEOCODING_URL, params)
        
        if result['status'] == '1' and result['regeocode']:
            return result['regeocode']['formatted_address']
        
        return None
    
    def text_search(self, keywords: str, city: str = None, citylimit: bool = False) -> List[Dict]:
        """文本搜索POI"""
        params = {
            'keywords': keywords,
            'city': city or '',
            'citylimit': 'true' if citylimit else 'false',
            'page': 1,
            'offset': Config.DEFAULT_PAGE_SIZE
        }
        
        result = self._make_request(Config.TEXT_SEARCH_URL, params)
        
        if result['status'] == '1' and result['pois']:
            return result['pois']
        
        return []
    
    def around_search(self, location: str, keywords: str = '', radius: int = None) -> List[Dict]:
        """周边搜索POI"""
        params = {
            'location': location,
            'keywords': keywords,
            'radius': radius or Config.DEFAULT_RADIUS,
            'page': 1,
            'offset': Config.DEFAULT_PAGE_SIZE
        }
        
        result = self._make_request(Config.AROUND_SEARCH_URL, params)
        
        if result['status'] == '1' and result['pois']:
            return result['pois']
        
        return []
    
    def get_poi_detail(self, poi_id: str) -> Optional[Dict]:
        """获取POI详细信息"""
        params = {
            'id': poi_id
        }
        
        result = self._make_request(Config.DETAIL_SEARCH_URL, params)
        
        if result['status'] == '1' and result['pois']:
            return result['pois'][0]
        
        return None
    
    def search_nearby_places(self, query: str, location: str = None, radius: int = None) -> List[Dict]:
        """搜索附近地点（智能搜索）"""
        # 如果提供了位置，使用周边搜索
        if location:
            return self.around_search(location, query, radius)
        
        # 否则使用文本搜索
        return self.text_search(query)
    
    def get_ip_location(self) -> Optional[Dict]:
        """获取用户IP位置"""
        try:
            # 使用高德地图IP定位API
            params = {
                'key': self.api_key,
                'output': 'json'
            }
            
            result = self._make_request(Config.IP_LOCATION_URL, params)
            
            if result['status'] == '1' and result.get('location'):
                location = result['location']
                lng, lat = map(float, location.split(','))
                return {
                    'type': 'ip',
                    'lng': lng,
                    'lat': lat,
                    'address': result.get('formatted_address', ''),
                    'location_str': location,
                    'city': result.get('city', ''),
                    'province': result.get('province', '')
                }
        except Exception as e:
            print(f"获取IP位置失败: {e}")
        
        return None

    def analyze_location(self, location: str = None) -> Dict:
        """分析位置信息"""
        # 如果没有提供位置，尝试获取IP位置
        if not location:
            ip_location = self.get_ip_location()
            if ip_location:
                return ip_location
            return {
                'type': 'unknown',
                'error': '无法获取位置信息，请手动输入位置'
            }
        
        # 如果是经纬度格式
        if ',' in location and location.count(',') == 1:
            try:
                lng, lat = map(float, location.split(','))
                address = self.reverse_geocode(lng, lat)
                return {
                    'type': 'coordinates',
                    'lng': lng,
                    'lat': lat,
                    'address': address,
                    'location_str': location
                }
            except ValueError:
                pass
        
        # 尝试作为地址进行地理编码
        coords = self.geocode(location)
        if coords:
            lng, lat = coords
            return {
                'type': 'address',
                'lng': lng,
                'lat': lat,
                'address': location,
                'location_str': f'{lng},{lat}'
            }
        
        return {
            'type': 'unknown',
            'location_str': location,
            'error': '无法解析位置信息'
        }
