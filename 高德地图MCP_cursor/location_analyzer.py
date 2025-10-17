import pandas as pd
import numpy as np
from typing import List, Dict, Optional, Tuple
from amap_service import AmapService
from nlp_processor import NLPProcessor

class LocationAnalyzer:
    """地点查询和分析器"""
    
    def __init__(self, api_key: str = None):
        self.amap_service = AmapService(api_key)
        self.nlp_processor = NLPProcessor()
    
    def search_places(self, query: str, location: str = None) -> Dict:
        """智能搜索地点"""
        # 解析自然语言查询
        keywords, parsed_location, distance, quantity = self.nlp_processor.parse_location_query(query)
        
        # 确定搜索位置
        search_location = location or parsed_location
        
        # 分析位置信息
        location_info = self.amap_service.analyze_location(search_location) if search_location else None
        
        # 执行搜索
        if search_location and location_info.get('type') != 'unknown':
            # 使用位置进行周边搜索
            places = self.amap_service.around_search(
                location_info['location_str'],
                keywords,
                distance
            )
        else:
            # 使用关键词进行文本搜索
            places = self.amap_service.text_search(keywords)
        
        # 限制返回数量
        if quantity:
            places = places[:quantity]
        
        # 分析结果
        analysis = self._analyze_places(places, location_info)
        
        return {
            'query': query,
            'keywords': keywords,
            'location_info': location_info,
            'places': places,
            'analysis': analysis,
            'total_count': len(places)
        }
    
    def _analyze_places(self, places: List[Dict], location_info: Dict = None) -> Dict:
        """分析地点数据"""
        if not places:
            return {
                'summary': '未找到相关地点',
                'categories': {},
                'distance_stats': {},
                'recommendations': []
            }
        
        # 创建DataFrame便于分析
        df = pd.DataFrame(places)
        
        # 分类统计
        categories = {}
        if 'type' in df.columns:
            category_counts = df['type'].value_counts()
            categories = category_counts.to_dict()
        
        # 距离统计
        distance_stats = {}
        if 'distance' in df.columns:
            distances = pd.to_numeric(df['distance'], errors='coerce')
            distance_stats = {
                'min': float(distances.min()) if not distances.isna().all() else 0,
                'max': float(distances.max()) if not distances.isna().all() else 0,
                'avg': float(distances.mean()) if not distances.isna().all() else 0,
                'median': float(distances.median()) if not distances.isna().all() else 0
            }
        
        # 评分统计
        rating_stats = {}
        if 'rating' in df.columns:
            ratings = pd.to_numeric(df['rating'], errors='coerce')
            rating_stats = {
                'min': float(ratings.min()) if not ratings.isna().all() else 0,
                'max': float(ratings.max()) if not ratings.isna().all() else 0,
                'avg': float(ratings.mean()) if not ratings.isna().all() else 0
            }
        
        # 生成推荐
        recommendations = self._generate_recommendations(df, categories, distance_stats, rating_stats)
        
        # 生成摘要
        summary = self._generate_summary(categories, distance_stats, len(places))
        
        return {
            'summary': summary,
            'categories': categories,
            'distance_stats': distance_stats,
            'rating_stats': rating_stats,
            'recommendations': recommendations
        }
    
    def _generate_recommendations(self, df: pd.DataFrame, categories: Dict, 
                                distance_stats: Dict, rating_stats: Dict) -> List[str]:
        """生成推荐建议"""
        recommendations = []
        
        # 基于数量的推荐
        if len(df) == 0:
            recommendations.append("未找到相关地点，建议扩大搜索范围或调整关键词")
        elif len(df) < 3:
            recommendations.append("找到的地点较少，建议扩大搜索半径或使用更宽泛的关键词")
        elif len(df) > 20:
            recommendations.append("找到的地点较多，建议缩小搜索范围或使用更具体的关键词")
        
        # 基于距离的推荐
        if distance_stats and distance_stats.get('avg', 0) > 2000:
            recommendations.append("大部分地点距离较远，建议选择距离较近的地点")
        
        # 基于评分的推荐
        if rating_stats and rating_stats.get('avg', 0) > 0:
            if rating_stats['avg'] > 4.0:
                recommendations.append("该区域整体评分较高，选择较多")
            elif rating_stats['avg'] < 3.0:
                recommendations.append("该区域整体评分较低，建议谨慎选择")
        
        # 基于类型的推荐
        if categories:
            top_category = max(categories.items(), key=lambda x: x[1])
            recommendations.append(f"该区域{top_category[0]}类地点最多，有{top_category[1]}个选择")
        
        return recommendations
    
    def _generate_summary(self, categories: Dict, distance_stats: Dict, total_count: int) -> str:
        """生成分析摘要"""
        summary_parts = [f"共找到{total_count}个相关地点"]
        
        if categories:
            top_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)[:3]
            category_names = [f"{name}({count}个)" for name, count in top_categories]
            summary_parts.append(f"主要类型：{', '.join(category_names)}")
        
        if distance_stats and distance_stats.get('avg', 0) > 0:
            avg_distance = distance_stats['avg']
            if avg_distance < 1000:
                summary_parts.append(f"平均距离约{avg_distance:.0f}米，位置较近")
            else:
                summary_parts.append(f"平均距离约{avg_distance/1000:.1f}公里")
        
        return "；".join(summary_parts) + "。"
    
    def get_place_details(self, place_id: str) -> Optional[Dict]:
        """获取地点详细信息"""
        return self.amap_service.get_poi_detail(place_id)
    
    def find_nearest_places(self, location: str, place_type: str, count: int = 5) -> List[Dict]:
        """查找最近的地点"""
        location_info = self.amap_service.analyze_location(location)
        if location_info.get('type') == 'unknown':
            return []
        
        places = self.amap_service.around_search(
            location_info['location_str'],
            place_type,
            5000  # 5公里范围内
        )
        
        # 按距离排序
        if places and 'distance' in places[0]:
            places.sort(key=lambda x: float(x.get('distance', 0)))
        
        return places[:count]
    
    def compare_places(self, place_ids: List[str]) -> Dict:
        """比较多个地点"""
        places = []
        for place_id in place_ids:
            place = self.get_place_details(place_id)
            if place:
                places.append(place)
        
        if not places:
            return {'error': '未找到有效的地点信息'}
        
        # 创建比较表格
        comparison_data = []
        for place in places:
            comparison_data.append({
                'name': place.get('name', ''),
                'address': place.get('address', ''),
                'rating': place.get('rating', ''),
                'distance': place.get('distance', ''),
                'tel': place.get('tel', ''),
                'type': place.get('type', '')
            })
        
        return {
            'places': comparison_data,
            'count': len(places)
        }
    
    def get_route_suggestions(self, start_location: str, end_location: str) -> Dict:
        """获取路线建议"""
        # 这里可以集成路线规划API
        # 目前返回基本信息
        start_info = self.amap_service.analyze_location(start_location)
        end_info = self.amap_service.analyze_location(end_location)
        
        return {
            'start': start_info,
            'end': end_info,
            'message': '路线规划功能需要集成高德地图路线规划API'
        }
