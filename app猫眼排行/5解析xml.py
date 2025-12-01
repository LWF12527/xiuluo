import xml.etree.ElementTree as ET


def extract_cinema_info_from_file(file_path):
    """从文件读取XML并提取电影院信息（修复路径问题）"""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"XML解析错误: {e}")
        return []
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
        return []

    results = []

    # 遍历所有节点，查找resource-id为"com.sankuai.moviepro:id/sc"的节点
    for node in root.iter():
        if node.get('resource-id') == 'com.sankuai.moviepro:id/sc':
            # 提取电影院名称 (在oq节点下的op节点)
            name_node = node.find(".//node[@resource-id='com.sankuai.moviepro:id/op']")
            cinema_name = name_node.text if name_node is not None else ""

            # 提取票房/人次/上座率/城市排名 (在bb7节点下的子节点)
            bb7_node = node.find(".//node[@resource-id='com.sankuai.moviepro:id/bb7']")
            if bb7_node is None:
                continue

            # 提取票房 (qh)
            box_office_node = bb7_node.find(".//node[@resource-id='com.sankuai.moviepro:id/qh']")
            box_office = box_office_node.text if box_office_node is not None else ""

            # 提取观影人次 (qi)
            audience_node = bb7_node.find(".//node[@resource-id='com.sankuai.moviepro:id/qi']")
            audience_count = audience_node.text if audience_node is not None else ""

            # 提取上座率 (qj)
            occupancy_node = bb7_node.find(".//node[@resource-id='com.sankuai.moviepro:id/qj']")
            occupancy_rate = occupancy_node.text if occupancy_node is not None else ""

            # 提取城市排名 (qk)
            city_rank_node = bb7_node.find(".//node[@resource-id='com.sankuai.moviepro:id/qk']")
            city_rank = city_rank_node.text if city_rank_node is not None else ""

            # 只有当有电影院名称时才添加到结果中
            if cinema_name.strip():
                results.append({
                    'name': cinema_name.strip(),
                    'box_office': box_office.strip(),
                    'audience_count': audience_count.strip(),
                    'occupancy_rate': occupancy_rate.strip(),
                    'city_rank': city_rank.strip()
                })

    return results


# 使用示例
if __name__ == "__main__":
    file_path = "1.xml"  # 请确保文件路径正确

    cinema_data = extract_cinema_info_from_file(file_path)

    print(f"找到 {len(cinema_data)} 家电影院的数据：")
    print("=" * 80)

    for i, cinema in enumerate(cinema_data, 1):
        print(f"{i}. 电影院名称: {cinema['name']}")
        print(f"   票房: {cinema['box_office']}")
        print(f"   观影人次: {cinema['audience_count']}")
        print(f"   上座率: {cinema['occupancy_rate']}")
        print(f"   城市排名: {cinema['city_rank']}")
        print("-" * 40)