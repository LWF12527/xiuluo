#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
高德地图地点查询应用 - 简化演示版本
"""

import os
import sys
from location_analyzer import LocationAnalyzer

def main():
    """主函数"""
    print("高德地图地点查询应用")
    print("=" * 50)
    
    # 检查API密钥
    api_key = os.getenv('AMAP_KEY')
    if not api_key or api_key == 'your_amap_key_here':
        print("请先设置高德地图API密钥！")
        print("设置环境变量: set AMAP_KEY=your_amap_key_here")
        return
    
    try:
        # 初始化分析器
        analyzer = LocationAnalyzer(api_key)
        print("应用初始化成功！")
        
        # 演示查询
        print("\n演示查询:")
        print("1. 搜索附近的餐厅")
        result1 = analyzer.search_places("附近的餐厅")
        print(f"   找到 {result1['total_count']} 个餐厅")
        
        print("\n2. 搜索500米内的超市")
        result2 = analyzer.search_places("500米内的超市")
        print(f"   找到 {result2['total_count']} 个超市")
        
        print("\n3. 搜索北京西站的酒店")
        result3 = analyzer.search_places("酒店", "北京西站")
        print(f"   找到 {result3['total_count']} 个酒店")
        
        # 显示第一个结果
        if result1['places']:
            place = result1['places'][0]
            print(f"\n第一个餐厅:")
            print(f"   名称: {place.get('name', '未知')}")
            print(f"   地址: {place.get('address', '未知')}")
            print(f"   距离: {place.get('distance', '未知')}米")
            print(f"   评分: {place.get('rating', '未知')}")
        
        print("\n演示完成！")
        
    except Exception as e:
        print(f"初始化失败: {e}")

if __name__ == "__main__":
    main()
