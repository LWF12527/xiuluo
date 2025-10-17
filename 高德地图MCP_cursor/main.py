#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
高德地图地点查询应用
支持自然语言查询附近地点并进行分析
"""

import os
import sys
from typing import Dict, List
from location_analyzer import LocationAnalyzer
from nlp_processor import NLPProcessor

class AmapLocationApp:
    """高德地图地点查询应用主类"""
    
    def __init__(self):
        self.analyzer = None
        self.nlp_processor = NLPProcessor()
        self.running = True
        
    def initialize(self):
        """初始化应用"""
        print("高德地图地点查询应用")
        print("=" * 50)
        
        # 检查API密钥
        api_key = os.getenv('AMAP_KEY')
        if not api_key or api_key == 'your_amap_key_here':
            print("请先设置高德地图API密钥！")
            print("1. 复制 env_example.txt 为 .env")
            print("2. 在 .env 文件中设置你的 AMAP_KEY")
            print("3. 或者设置环境变量 AMAP_KEY")
            return False
        
        try:
            self.analyzer = LocationAnalyzer(api_key)
            print("应用初始化成功！")
            return True
        except Exception as e:
            print(f"初始化失败: {e}")
            return False
    
    def run(self):
        """运行应用主循环"""
        if not self.initialize():
            return
        
        self.show_help()
        
        while self.running:
            try:
                user_input = input("\n请输入查询内容 (输入 'help' 查看帮助, 'quit' 退出): ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    self.running = False
                    print("再见！")
                    break
                
                if user_input.lower() == 'help':
                    self.show_help()
                    continue
                
                # 处理查询
                self.process_query(user_input)
                
            except KeyboardInterrupt:
                print("\n再见！")
                break
            except Exception as e:
                print(f"处理查询时出错: {e}")
    
    def process_query(self, query: str):
        """处理用户查询"""
        print(f"\n正在搜索: {query}")
        print("-" * 30)
        
        try:
            # 分析查询意图
            intent = self.nlp_processor.analyze_query_intent(query)
            print(f"查询类型: {intent['type']} (置信度: {intent['confidence']:.2f})")
            
            if intent['suggestions']:
                print("建议:")
                for suggestion in intent['suggestions']:
                    print(f"   • {suggestion}")
            
            # 执行搜索
            result = self.analyzer.search_places(query)
            
            # 显示结果
            self.display_results(result)
            
        except Exception as e:
            print(f"搜索失败: {e}")
    
    def display_results(self, result: Dict):
        """显示搜索结果"""
        if not result['places']:
            print("未找到相关地点")
            return
        
        print(f"\n搜索结果分析:")
        print(f"   {result['analysis']['summary']}")
        
        if result['analysis']['recommendations']:
            print("\n推荐建议:")
            for rec in result['analysis']['recommendations']:
                print(f"   • {rec}")
        
        print(f"\n找到 {result['total_count']} 个地点:")
        print("-" * 50)
        
        for i, place in enumerate(result['places'][:10], 1):  # 只显示前10个
            self.display_place_info(i, place)
        
        if len(result['places']) > 10:
            print(f"... 还有 {len(result['places']) - 10} 个地点")
        
        # 显示分类统计
        if result['analysis']['categories']:
            print(f"\n地点分类统计:")
            for category, count in result['analysis']['categories'].items():
                print(f"   {category}: {count}个")
    
    def display_place_info(self, index: int, place: Dict):
        """显示单个地点信息"""
        name = place.get('name', '未知名称')
        address = place.get('address', '地址未知')
        distance = place.get('distance', '')
        rating = place.get('rating', '')
        tel = place.get('tel', '')
        place_type = place.get('type', '')
        
        print(f"{index:2d}. {name}")
        print(f"    地址: {address}")
        
        if distance:
            dist_km = float(distance) / 1000
            print(f"    距离: {dist_km:.1f}公里")
        
        if rating:
            print(f"    评分: {rating}")
        
        if tel:
            print(f"    电话: {tel}")
        
        if place_type:
            print(f"    类型: {place_type}")
        
        print()
    
    def show_help(self):
        """显示帮助信息"""
        print("\n使用帮助:")
        print("=" * 30)
        print("查询示例:")
        print("   • 附近的餐厅")
        print("   • 500米内的超市")
        print("   • 北京西站的酒店")
        print("   • 116.397,39.916附近的银行")
        print("   • 找几个健身房")
        print("   • 很远的电影院")
        
        print("\n位置格式:")
        print("   • 地址: 北京市朝阳区")
        print("   • 经纬度: 116.397,39.916")
        print("   • 地标: 天安门广场")
        
        print("\n查询类型:")
        print("   • 餐厅、购物、交通、娱乐、住宿")
        print("   • 医疗、教育、银行、其他")
        
        print("\n距离范围:")
        print("   • 很近(500米)、近(1公里)、附近(2公里)")
        print("   • 不远(3公里)、远一点(5公里)、很远(10公里)")
        
        print("\n数量控制:")
        print("   • 几个(3个)、一些(5个)、很多(10个)、全部(20个)")
        
        print("\n命令:")
        print("   • help - 显示帮助")
        print("   • quit/exit/q - 退出程序")
    
    def interactive_search(self):
        """交互式搜索模式"""
        print("\n交互式搜索模式")
        print("=" * 30)
        
        # 获取位置
        location = input("请输入当前位置 (地址或经纬度，回车跳过): ").strip()
        if not location:
            location = None
        
        # 获取查询内容
        query = input("请输入要搜索的内容: ").strip()
        if not query:
            print("查询内容不能为空")
            return
        
        # 执行搜索
        if location:
            result = self.analyzer.search_places(query, location)
        else:
            result = self.analyzer.search_places(query)
        
        # 显示结果
        self.display_results(result)
    
    def batch_search(self, queries: List[str]):
        """批量搜索"""
        print(f"\n批量搜索 {len(queries)} 个查询")
        print("=" * 40)
        
        results = []
        for i, query in enumerate(queries, 1):
            print(f"\n[{i}/{len(queries)}] 搜索: {query}")
            try:
                result = self.analyzer.search_places(query)
                results.append(result)
                print(f"找到 {result['total_count']} 个地点")
            except Exception as e:
                print(f"搜索失败: {e}")
                results.append(None)
        
        return results

def main():
    """主函数"""
    app = AmapLocationApp()
    
    # 检查命令行参数
    if len(sys.argv) > 1:
        if sys.argv[1] == '--help' or sys.argv[1] == '-h':
            app.show_help()
            return
        elif sys.argv[1] == '--interactive' or sys.argv[1] == '-i':
            if app.initialize():
                app.interactive_search()
            return
    
    # 正常运行
    app.run()

if __name__ == "__main__":
    main()
