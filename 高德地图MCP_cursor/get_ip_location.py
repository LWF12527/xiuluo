#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
获取用户IP位置
"""

import requests
import json

def get_ip_location():
    """获取用户IP位置"""
    api_key = 'd54a572c1bfb5367a3f03c7bc7e276e9'
    url = 'https://restapi.amap.com/v3/ip'
    
    params = {
        'key': api_key,
        'output': 'json'
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        result = response.json()
        
        print("API响应:", json.dumps(result, ensure_ascii=False, indent=2))
        
        if result['status'] == '1':
            # 高德地图IP定位API返回的是矩形区域，我们需要计算中心点
            if result.get('rectangle'):
                rectangle = result['rectangle']
                # rectangle格式: "lng1,lat1;lng2,lat2"
                coords = rectangle.split(';')
                if len(coords) == 2:
                    lng1, lat1 = map(float, coords[0].split(','))
                    lng2, lat2 = map(float, coords[1].split(','))
                    # 计算中心点
                    center_lng = (lng1 + lng2) / 2
                    center_lat = (lat1 + lat2) / 2
                    location_str = f"{center_lng},{center_lat}"
                    
                    return {
                        'type': 'ip',
                        'lng': center_lng,
                        'lat': center_lat,
                        'address': f"{result.get('province', '')}{result.get('city', '')}",
                        'location_str': location_str,
                        'city': result.get('city', ''),
                        'province': result.get('province', ''),
                        'rectangle': rectangle
                    }
            elif result.get('location'):
                location = result['location']
                lng, lat = map(float, location.split(','))
                return {
                    'type': 'ip',
                    'lng': lng,
                    'lat': lat,
                    'address': f"{result.get('province', '')}{result.get('city', '')}",
                    'location_str': location,
                    'city': result.get('city', ''),
                    'province': result.get('province', '')
                }
        else:
            print(f"API返回错误: {result.get('info', '未知错误')}")
            return None
            
    except Exception as e:
        print(f"请求失败: {e}")
        return None

if __name__ == "__main__":
    print("正在获取您的IP位置...")
    location_info = get_ip_location()
    
    if location_info:
        print(f"\n您的位置信息:")
        print(f"   地址: {location_info.get('address', '未知')}")
        print(f"   城市: {location_info.get('city', '未知')}")
        print(f"   省份: {location_info.get('province', '未知')}")
        print(f"   经纬度: {location_info['location_str']}")
        if location_info.get('rectangle'):
            print(f"   定位区域: {location_info['rectangle']}")
    else:
        print("无法获取位置信息")
