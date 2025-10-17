# 高德地图地点查询应用

一个基于高德地图API的智能地点查询应用，支持自然语言查询附近地点并提供详细分析。

## 功能特点

- 🗺️ **智能地点搜索**: 支持自然语言查询，自动识别地点类型和距离范围
- 📍 **多种位置格式**: 支持地址、经纬度、地标等多种位置输入方式
- 📊 **详细分析**: 提供地点分类统计、距离分析、评分统计等
- 💡 **智能推荐**: 基于搜索结果提供个性化建议
- 🎯 **交互式界面**: 友好的命令行交互界面

## 安装和使用

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置API密钥

1. 复制 `env_example.txt` 为 `.env`
2. 在 `.env` 文件中设置你的高德地图API密钥：

```
AMAP_KEY=your_amap_key_here
```

或者设置环境变量：

```bash
export AMAP_KEY=your_amap_key_here
```

### 3. 运行应用

```bash
python main.py
```

## 使用示例

### 基本查询

```
🔍 请输入查询内容: 附近的餐厅
```

### 带距离的查询

```
🔍 请输入查询内容: 500米内的超市
```

### 指定位置的查询

```
🔍 请输入查询内容: 北京西站的酒店
```

### 经纬度查询

```
🔍 请输入查询内容: 116.397,39.916附近的银行
```

### 数量控制

```
🔍 请输入查询内容: 找几个健身房
```

## 支持的查询类型

- **餐厅**: 餐厅、饭店、美食、吃饭、用餐等
- **购物**: 商场、超市、购物、商店、市场等
- **交通**: 地铁、公交、车站、机场、火车站等
- **娱乐**: 电影院、KTV、网吧、游戏厅、公园等
- **住宿**: 酒店、宾馆、旅馆、民宿等
- **医疗**: 医院、诊所、药店、卫生所等
- **教育**: 学校、大学、中学、培训机构等
- **银行**: 银行、ATM、取款机等

## 距离范围

- **很近**: 500米
- **近**: 1公里
- **附近**: 2公里
- **不远**: 3公里
- **远一点**: 5公里
- **很远**: 10公里

## 数量控制

- **几个**: 3个
- **一些**: 5个
- **很多**: 10个
- **全部**: 20个

## 项目结构

```
amap_map/
├── main.py                 # 主程序入口
├── config.py              # 配置文件
├── amap_service.py        # 高德地图API服务
├── nlp_processor.py       # 自然语言处理
├── location_analyzer.py   # 地点分析器
├── requirements.txt       # 依赖包
├── env_example.txt        # 环境变量示例
└── README.md             # 说明文档
```

## API说明

### AmapService 类

高德地图API服务类，提供以下方法：

- `geocode(address, city)`: 地理编码
- `reverse_geocode(lng, lat)`: 逆地理编码
- `text_search(keywords, city)`: 文本搜索
- `around_search(location, keywords, radius)`: 周边搜索
- `get_poi_detail(poi_id)`: 获取POI详情

### NLPProcessor 类

自然语言处理类，提供以下方法：

- `extract_location_info(query)`: 提取位置信息
- `parse_location_query(query)`: 解析位置查询
- `generate_search_keywords(query)`: 生成搜索关键词
- `analyze_query_intent(query)`: 分析查询意图

### LocationAnalyzer 类

地点分析器，提供以下方法：

- `search_places(query, location)`: 智能搜索地点
- `get_place_details(place_id)`: 获取地点详情
- `find_nearest_places(location, place_type, count)`: 查找最近地点
- `compare_places(place_ids)`: 比较多个地点

## 命令行参数

- `python main.py`: 正常运行
- `python main.py --help` 或 `python main.py -h`: 显示帮助
- `python main.py --interactive` 或 `python main.py -i`: 交互式搜索模式

## 注意事项

1. 需要有效的高德地图API密钥
2. 确保网络连接正常
3. API有调用频率限制，请合理使用
4. 经纬度格式为：经度,纬度

## 错误处理

应用包含完善的错误处理机制：

- API密钥验证
- 网络请求异常处理
- 数据解析错误处理
- 用户输入验证

## 扩展功能

可以基于现有代码扩展以下功能：

- 路线规划
- 实时交通信息
- 天气信息
- 用户收藏
- 历史记录
- 地图可视化

## 许可证

MIT License
