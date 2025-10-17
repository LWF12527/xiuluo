import re
import jieba
from typing import Dict, List, Tuple, Optional

class NLPProcessor:
    """自然语言处理模块"""
    
    def __init__(self):
        # 地点关键词
        self.location_keywords = {
            '餐厅': ['餐厅', '饭店', '美食', '吃饭', '用餐', '食堂', '餐馆', '酒楼', '火锅', '烧烤', '快餐'],
            '购物': ['商场', '超市', '购物', '商店', '市场', '购物中心', '百货', '便利店', '药店'],
            '交通': ['地铁', '公交', '车站', '机场', '火车站', '停车场', '加油站', '洗车'],
            '娱乐': ['电影院', 'KTV', '网吧', '游戏厅', '游乐场', '公园', '广场', '健身房', '游泳馆'],
            '住宿': ['酒店', '宾馆', '旅馆', '民宿', '招待所', '住宿'],
            '医疗': ['医院', '诊所', '药店', '卫生所', '体检中心', '牙科', '眼科'],
            '教育': ['学校', '大学', '中学', '小学', '幼儿园', '培训机构', '图书馆', '书店'],
            '银行': ['银行', 'ATM', '取款机', '金融', '投资'],
            '其他': ['厕所', '洗手间', '银行', '邮局', '政府', '派出所', '消防站']
        }
        
        # 距离关键词
        self.distance_keywords = {
            '很近': 500,
            '近': 1000,
            '附近': 2000,
            '不远': 3000,
            '远一点': 5000,
            '很远': 10000
        }
        
        # 数量关键词
        self.quantity_keywords = {
            '几个': 3,
            '一些': 5,
            '很多': 10,
            '全部': 20
        }
    
    def extract_location_info(self, query: str) -> Dict:
        """从自然语言查询中提取位置信息"""
        result = {
            'keywords': [],
            'location_type': None,
            'distance': None,
            'quantity': None,
            'original_query': query
        }
        
        # 分词
        words = list(jieba.cut(query))
        
        # 提取地点类型关键词
        for category, keywords in self.location_keywords.items():
            for keyword in keywords:
                if keyword in query:
                    result['keywords'].append(keyword)
                    if not result['location_type']:
                        result['location_type'] = category
                    break
        
        # 提取距离信息
        for distance_word, radius in self.distance_keywords.items():
            if distance_word in query:
                result['distance'] = radius
                break
        
        # 提取数量信息
        for quantity_word, count in self.quantity_keywords.items():
            if quantity_word in query:
                result['quantity'] = count
                break
        
        # 如果没有找到具体类型，尝试从关键词中推断
        if not result['location_type']:
            result['location_type'] = self._infer_location_type(query)
        
        return result
    
    def _infer_location_type(self, query: str) -> str:
        """从查询中推断地点类型"""
        # 简单的关键词匹配
        if any(word in query for word in ['吃', '饭', '菜', '餐']):
            return '餐厅'
        elif any(word in query for word in ['买', '购', '商', '店']):
            return '购物'
        elif any(word in query for word in ['车', '站', '交通', '路']):
            return '交通'
        elif any(word in query for word in ['玩', '乐', '娱', '看']):
            return '娱乐'
        elif any(word in query for word in ['住', '宿', '房']):
            return '住宿'
        elif any(word in query for word in ['医', '药', '病', '健康']):
            return '医疗'
        elif any(word in query for word in ['学', '书', '教', '培训']):
            return '教育'
        else:
            return '其他'
    
    def parse_location_query(self, query: str) -> Tuple[str, Optional[str], Optional[int], Optional[int]]:
        """解析位置查询，返回(关键词, 位置, 距离, 数量)"""
        info = self.extract_location_info(query)
        
        # 提取位置信息（经纬度或地址）
        location = self._extract_location_from_query(query)
        
        return (
            ' '.join(info['keywords']) or query,
            location,
            info['distance'],
            info['quantity']
        )
    
    def _extract_location_from_query(self, query: str) -> Optional[str]:
        """从查询中提取位置信息"""
        # 匹配经纬度格式 (经度,纬度)
        coord_pattern = r'(\d+\.?\d*),\s*(\d+\.?\d*)'
        coord_match = re.search(coord_pattern, query)
        if coord_match:
            return f"{coord_match.group(1)},{coord_match.group(2)}"
        
        # 匹配地址关键词
        address_keywords = ['在', '附近', '周围', '边上', '旁边']
        for keyword in address_keywords:
            if keyword in query:
                # 尝试提取地址
                parts = query.split(keyword)
                if len(parts) > 1:
                    address = parts[0].strip()
                    if len(address) > 2:  # 避免太短的地址
                        return address
        
        return None
    
    def generate_search_keywords(self, query: str) -> List[str]:
        """生成搜索关键词列表"""
        info = self.extract_location_info(query)
        
        keywords = []
        
        # 添加原始关键词
        if info['keywords']:
            keywords.extend(info['keywords'])
        
        # 添加类型相关关键词
        if info['location_type']:
            keywords.extend(self.location_keywords.get(info['location_type'], []))
        
        # 如果没有找到关键词，使用原始查询
        if not keywords:
            keywords = [query]
        
        return keywords[:5]  # 限制关键词数量
    
    def analyze_query_intent(self, query: str) -> Dict:
        """分析查询意图"""
        intent = {
            'type': 'search',
            'confidence': 0.0,
            'suggestions': []
        }
        
        # 分析查询类型
        if any(word in query for word in ['找', '搜索', '查找', '附近', '周围']):
            intent['type'] = 'search'
            intent['confidence'] = 0.8
        elif any(word in query for word in ['怎么去', '路线', '导航', '怎么走']):
            intent['type'] = 'navigation'
            intent['confidence'] = 0.9
        elif any(word in query for word in ['多远', '距离', '多近']):
            intent['type'] = 'distance'
            intent['confidence'] = 0.7
        else:
            intent['type'] = 'search'
            intent['confidence'] = 0.5
        
        # 生成建议
        if intent['confidence'] < 0.6:
            intent['suggestions'] = [
                "请提供更具体的地点类型，如'附近的餐厅'",
                "可以指定距离范围，如'500米内的超市'",
                "或者直接提供地址或经纬度"
            ]
        
        return intent
