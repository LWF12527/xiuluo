#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
高德地图地点查询应用使用示例
"""

import os
from location_analyzer import LocationAnalyzer

def example_basic_search():
    """基本搜索示例"""
    print("=== 基本搜索示例 ===")
    
    # 初始化分析器
    analyzer = LocationAnalyzer()
    
    # 搜索附近的餐厅
    result = analyzer.search_places("附近的餐厅")
    print(f"找到 {result['total_count']} 个餐厅")
    
    # 显示前3个结果
    for i, place in enumerate(result['places'][:3], 1):
        print(f"{i}. {place.get('name', '未知')} - {place.get('address', '地址未知')}")

def example_location_search():
    """指定位置搜索示例"""
    print("\n=== 指定位置搜索示例 ===")
    
    analyzer = LocationAnalyzer()
    
    # 在北京西站附近搜索酒店
    result = analyzer.search_places("酒店", "北京西站")
    print(f"在北京西站附近找到 {result['total_count']} 个酒店")
    
    # 显示分析结果
    print(f"分析结果: {result['analysis']['summary']}")

def example_distance_search():
    """距离范围搜索示例"""
    print("\n=== 距离范围搜索示例 ===")
    
    analyzer = LocationAnalyzer()
    
    # 搜索500米内的超市
    result = analyzer.search_places("500米内的超市")
    print(f"找到 {result['total_count']} 个超市")
    
    # 显示距离统计
    if result['analysis']['distance_stats']:
        stats = result['analysis']['distance_stats']
        print(f"距离统计: 最近{stats['min']:.0f}米, 最远{stats['max']:.0f}米, 平均{stats['avg']:.0f}米")

def example_coordinate_search():
    """经纬度搜索示例"""
    print("\n=== 经纬度搜索示例 ===")
    
    analyzer = LocationAnalyzer()
    
    # 在天安门广场附近搜索银行
    result = analyzer.search_places("银行", "116.397,39.916")
    print(f"在天安门广场附近找到 {result['total_count']} 个银行")
    
    # 显示推荐建议
    if result['analysis']['recommendations']:
        print("推荐建议:")
        for rec in result['analysis']['recommendations']:
            print(f"  • {rec}")

def example_quantity_search():
    """数量控制搜索示例"""
    print("\n=== 数量控制搜索示例 ===")
    
    analyzer = LocationAnalyzer()
    
    # 搜索几个健身房
    result = analyzer.search_places("找几个健身房")
    print(f"找到 {result['total_count']} 个健身房")
    
    # 显示分类统计
    if result['analysis']['categories']:
        print("分类统计:")
        for category, count in result['analysis']['categories'].items():
            print(f"  {category}: {count}个")

def example_place_details():
    """地点详情查询示例"""
    print("\n=== 地点详情查询示例 ===")
    
    analyzer = LocationAnalyzer()
    
    # 先搜索一个地点
    result = analyzer.search_places("附近的餐厅")
    if result['places']:
        place = result['places'][0]
        place_id = place.get('id')
        
        if place_id:
            # 获取详细信息
            details = analyzer.get_place_details(place_id)
            if details:
                print(f"地点详情: {details.get('name', '未知')}")
                print(f"地址: {details.get('address', '未知')}")
                print(f"电话: {details.get('tel', '未知')}")
                print(f"评分: {details.get('rating', '未知')}")

def example_nearest_places():
    """最近地点查询示例"""
    print("\n=== 最近地点查询示例 ===")
    
    analyzer = LocationAnalyzer()
    
    # 查找最近的5个超市
    places = analyzer.find_nearest_places("116.397,39.916", "超市", 5)
    print(f"找到 {len(places)} 个最近的超市:")
    
    for i, place in enumerate(places, 1):
        distance = place.get('distance', '未知')
        print(f"{i}. {place.get('name', '未知')} - 距离: {distance}米")

def example_compare_places():
    """地点比较示例"""
    print("\n=== 地点比较示例 ===")
    
    analyzer = LocationAnalyzer()
    
    # 先搜索几个地点
    result = analyzer.search_places("附近的餐厅")
    if len(result['places']) >= 2:
        # 获取前两个地点的ID
        place_ids = [place.get('id') for place in result['places'][:2] if place.get('id')]
        
        if place_ids:
            # 比较地点
            comparison = analyzer.compare_places(place_ids)
            print(f"比较 {comparison['count']} 个地点:")
            
            for place in comparison['places']:
                print(f"  {place['name']} - {place['address']} - 评分: {place['rating']}")

def main():
    """运行所有示例"""
    print("🗺️ 高德地图地点查询应用示例")
    print("=" * 50)
    
    # 检查API密钥
    if not os.getenv('AMAP_KEY') or os.getenv('AMAP_KEY') == 'your_amap_key_here':
        print("❌ 请先设置高德地图API密钥！")
        print("设置环境变量: export AMAP_KEY=your_amap_key_here")
        return
    
    try:
        # 运行示例
        example_basic_search()
        example_location_search()
        example_distance_search()
        example_coordinate_search()
        example_quantity_search()
        example_place_details()
        example_nearest_places()
        example_compare_places()
        
        print("\n✅ 所有示例运行完成！")
        
    except Exception as e:
        print(f"❌ 运行示例时出错: {e}")

if __name__ == "__main__":
    main()
