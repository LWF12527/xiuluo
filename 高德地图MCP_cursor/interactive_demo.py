#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
高德地图地点查询应用 - 交互式演示版本
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
        print("设置环境变量: $env:AMAP_KEY='your_amap_key_here'")
        return
    
    try:
        # 初始化分析器
        analyzer = LocationAnalyzer(api_key)
        print("应用初始化成功！")
        
        print("\n使用说明:")
        print("- 输入查询内容，如：附近的餐厅")
        print("- 输入 'quit' 退出程序")
        print("- 输入 'help' 查看帮助")
        
        while True:
            try:
                # 获取用户输入
                user_input = input("\n请输入查询内容: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("再见！")
                    break
                
                if user_input.lower() == 'help':
                    show_help()
                    continue
                
                # 执行搜索
                print(f"\n正在搜索: {user_input}")
                print("-" * 30)
                
                result = analyzer.search_places(user_input)
                
                # 显示结果
                if not result['places']:
                    print("未找到相关地点")
                    continue
                
                print(f"找到 {result['total_count']} 个地点")
                print(f"分析结果: {result['analysis']['summary']}")
                
                # 显示推荐建议
                if result['analysis']['recommendations']:
                    print("\n推荐建议:")
                    for rec in result['analysis']['recommendations']:
                        print(f"  • {rec}")
                
                # 显示前5个地点
                print(f"\n前5个地点:")
                for i, place in enumerate(result['places'][:5], 1):
                    name = place.get('name', '未知名称')
                    address = place.get('address', '地址未知')
                    distance = place.get('distance', '')
                    rating = place.get('rating', '')
                    
                    print(f"{i}. {name}")
                    print(f"   地址: {address}")
                    if distance:
                        dist_km = float(distance) / 1000
                        print(f"   距离: {dist_km:.1f}公里")
                    if rating:
                        print(f"   评分: {rating}")
                    print()
                
                # 显示分类统计
                if result['analysis']['categories']:
                    print("分类统计:")
                    for category, count in result['analysis']['categories'].items():
                        print(f"  {category}: {count}个")
                
            except KeyboardInterrupt:
                print("\n再见！")
                break
            except Exception as e:
                print(f"搜索失败: {e}")
        
    except Exception as e:
        print(f"初始化失败: {e}")

def show_help():
    """显示帮助信息"""
    print("\n使用帮助:")
    print("=" * 30)
    print("查询示例:")
    print("  • 附近的餐厅")
    print("  • 500米内的超市")
    print("  • 北京西站的酒店")
    print("  • 116.397,39.916附近的银行")
    print("  • 找几个健身房")
    print("  • 很远的电影院")
    
    print("\n位置格式:")
    print("  • 地址: 北京市朝阳区")
    print("  • 经纬度: 116.397,39.916")
    print("  • 地标: 天安门广场")
    
    print("\n查询类型:")
    print("  • 餐厅、购物、交通、娱乐、住宿")
    print("  • 医疗、教育、银行、其他")
    
    print("\n距离范围:")
    print("  • 很近(500米)、近(1公里)、附近(2公里)")
    print("  • 不远(3公里)、远一点(5公里)、很远(10公里)")
    
    print("\n数量控制:")
    print("  • 几个(3个)、一些(5个)、很多(10个)、全部(20个)")

if __name__ == "__main__":
    main()
