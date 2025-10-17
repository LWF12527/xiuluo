#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
获取用户真实位置并搜索附近景点
"""

import os
import sys
from location_analyzer import LocationAnalyzer

def main():
    """主函数"""
    print("正在获取您的位置信息...")
    print("=" * 50)
    
    # 检查API密钥
    api_key = os.getenv('AMAP_KEY')
    if not api_key or api_key == 'your_amap_key_here':
        print("请先设置高德地图API密钥！")
        print("设置环境变量: $env:AMAP_KEY='your_amap_key_here'")
        return
    
    try:
        # 初始化分析器
        analyzer = LocationAnalyzer(api_key)
        
        # 获取用户位置
        location_info = analyzer.amap_service.analyze_location()
        
        if location_info.get('type') == 'unknown':
            print("无法自动获取您的位置，请手动输入位置信息")
            location = input("请输入您的位置（地址或经纬度）: ").strip()
            if location:
                location_info = analyzer.amap_service.analyze_location(location)
            else:
                print("未输入位置信息，程序退出")
                return
        
        print(f"📍 您的位置: {location_info.get('address', '未知')}")
        if location_info.get('city'):
            print(f"🏙️ 城市: {location_info['city']}")
        if location_info.get('province'):
            print(f"🗺️ 省份: {location_info['province']}")
        
        print(f"\n正在搜索5公里内的景点、景区、公园...")
        print("-" * 50)
        
        # 搜索景点
        search_keywords = ['景点', '景区', '公园', '爬山', '风景', '山', '湖', '广场']
        all_places = []
        
        for keyword in search_keywords:
            print(f"搜索关键词: {keyword}")
            places = analyzer.amap_service.around_search(
                location_info['location_str'], 
                keyword, 
                5000  # 5公里
            )
            all_places.extend(places)
            print(f"找到 {len(places)} 个地点")
        
        # 去重
        unique_places = []
        seen_ids = set()
        for place in all_places:
            if place['id'] not in seen_ids:
                unique_places.append(place)
                seen_ids.add(place['id'])
        
        print(f"\n🎯 总共找到 {len(unique_places)} 个不重复的地点")
        print("=" * 50)
        
        # 按类型分类显示
        categories = {}
        for place in unique_places:
            place_type = place.get('type', '其他')
            if place_type not in categories:
                categories[place_type] = []
            categories[place_type].append(place)
        
        # 显示结果
        for category, places in categories.items():
            print(f"\n🏷️ {category} ({len(places)}个):")
            print("-" * 30)
            
            for i, place in enumerate(places[:5], 1):  # 每个类别最多显示5个
                name = place.get('name', '未知名称')
                address = place.get('address', '地址未知')
                distance = place.get('distance', '')
                
                print(f"{i}. {name}")
                print(f"   地址: {address}")
                if distance:
                    dist_km = float(distance) / 1000
                    print(f"   距离: {dist_km:.1f}公里")
                print()
            
            if len(places) > 5:
                print(f"   ... 还有 {len(places) - 5} 个地点")
        
        # 推荐最佳地点
        print("\n🌟 推荐地点:")
        print("=" * 30)
        
        # 按距离排序，推荐最近的几个
        sorted_places = sorted(unique_places, key=lambda x: float(x.get('distance', 999999)))
        
        for i, place in enumerate(sorted_places[:10], 1):
            name = place.get('name', '未知名称')
            address = place.get('address', '地址未知')
            distance = place.get('distance', '')
            place_type = place.get('type', '')
            
            print(f"{i:2d}. {name}")
            print(f"    地址: {address}")
            if distance:
                dist_km = float(distance) / 1000
                print(f"    距离: {dist_km:.1f}公里")
            if place_type:
                print(f"    类型: {place_type}")
            print()
        
    except Exception as e:
        print(f"程序运行出错: {e}")

if __name__ == "__main__":
    main()
