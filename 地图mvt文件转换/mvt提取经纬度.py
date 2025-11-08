import mapbox_vector_tile
import json
from pathlib import Path


def extract_and_print_coordinates(mvt_file_path, output_geojson_path="converted.geojson"):
    """
    从MVT文件中提取并打印经纬度坐标，然后生成GeoJSON文件
    """
    # 读取MVT文件
    with open(mvt_file_path, 'rb') as f:
        mvt_data = f.read()

    decoded_data = mapbox_vector_tile.decode(mvt_data)

    print("=== MVT文件经纬度坐标提取 ===")
    print(f"处理文件: {Path(mvt_file_path).name}")
    print("=" * 50)

    # 构建包含真实经纬度的GeoJSON
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    total_features = 0
    features_with_coords = 0

    # 遍历所有图层和要素
    for layer_name, layer_info in decoded_data.items():
        print(f"\n📋 图层: {layer_name}")
        print(f"   要素数量: {len(layer_info.get('features', []))}")

        for i, feature in enumerate(layer_info.get('features', [])):
            total_features += 1
            properties = feature.get('properties', {})
            geometry = feature['geometry']

            # 检查是否包含经纬度信息
            has_coords = 'centerX' in properties and 'centerY' in properties

            if has_coords:
                features_with_coords += 1
                try:
                    # 提取经纬度
                    longitude = float(properties['centerX'])
                    latitude = float(properties['centerY'])

                    # 打印坐标信息
                    print(f"   📍 要素 {i + 1} 的经纬度坐标:")
                    print(f"      经度 (centerX): {longitude}")
                    print(f"      纬度 (centerY): {latitude}")

                    # 打印其他重要属性
                    if 'name' in properties:
                        print(f"      名称: {properties['name']}")
                    if 'icao' in properties:
                        print(f"      ICAO代码: {properties['icao']}")
                    if 'spaceId' in properties:
                        print(f"      空间ID: {properties['spaceId']}")
                    if 'featureId' in properties:
                        print(f"      要素ID: {properties['featureId']}")

                    print("      " + "-" * 30)

                    # 创建点要素（使用提取的经纬度）
                    point_geometry = {
                        "type": "Point",
                        "coordinates": [longitude, latitude]
                    }

                    # 创建GeoJSON要素
                    geojson_feature = {
                        "type": "Feature",
                        "geometry": point_geometry,
                        "properties": properties.copy()
                    }

                    # 添加图层信息
                    geojson_feature['properties']['mvt_layer'] = layer_name
                    geojson['features'].append(geojson_feature)

                except (ValueError, TypeError) as e:
                    print(f"   ⚠️ 坐标转换错误: {e}")
            else:
                # 对于没有centerX/centerY的要素，也添加到GeoJSON但标记为无坐标
                geojson_feature = {
                    "type": "Feature",
                    "geometry": geometry,
                    "properties": properties.copy()
                }
                geojson_feature['properties']['mvt_layer'] = layer_name
                geojson_feature['properties']['has_geographic_coords'] = False
                geojson['features'].append(geojson_feature)

    # 保存为GeoJSON文件
    with open(output_geojson_path, 'w', encoding='utf-8') as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    # 打印统计信息
    print("\n" + "=" * 50)
    print("📊 处理结果统计:")
    print(f"   总要素数量: {total_features}")
    print(f"   包含经纬度坐标的要素: {features_with_coords}")
    print(f"   生成的GeoJSON文件: {output_geojson_path}")

    # 分析地理范围
    if features_with_coords > 0:
        print("\n🌍 地理范围分析:")
        lons = [f['geometry']['coordinates'][0] for f in geojson['features']
                if f['geometry']['type'] == 'Point' and len(f['geometry']['coordinates']) == 2]
        lats = [f['geometry']['coordinates'][1] for f in geojson['features']
                if f['geometry']['type'] == 'Point' and len(f['geometry']['coordinates']) == 2]

        if lons and lats:
            print(f"   经度范围: {min(lons):.6f}°E ~ {max(lons):.6f}°E")
            print(f"   纬度范围: {min(lats):.6f}°N ~ {max(lats):.6f}°N")
            print(f"   中心点: {(min(lons) + max(lons)) / 2:.6f}°E, {(min(lats) + max(lats)) / 2:.6f}°N")

    return geojson


def create_coordinates_summary(geojson_data, output_csv="coordinates_summary.csv"):
    """
    创建坐标摘要CSV文件
    """
    import csv

    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['layer', 'longitude', 'latitude', 'name', 'icao', 'spaceId', 'featureId']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for feature in geojson_data['features']:
            if feature['geometry']['type'] == 'Point':
                lon, lat = feature['geometry']['coordinates']
                row = {
                    'layer': feature['properties'].get('mvt_layer', ''),
                    'longitude': lon,
                    'latitude': lat,
                    'name': feature['properties'].get('name', ''),
                    'icao': feature['properties'].get('icao', ''),
                    'spaceId': feature['properties'].get('spaceId', ''),
                    'featureId': feature['properties'].get('featureId', '')
                }
                writer.writerow(row)

    print(f"   坐标摘要CSV: {output_csv}")


# 主执行函数
if __name__ == "__main__":
    # 请修改为您的MVT文件路径
    mvt_file_path = "./data/1.mvt"  # 修改为实际路径

    try:
        # 提取并打印经纬度坐标，生成GeoJSON
        geojson_data = extract_and_print_coordinates(mvt_file_path)

        # 创建坐标摘要CSV
        create_coordinates_summary(geojson_data)

        print("\n✅ 处理完成！")
        print("🎯 下一步操作建议:")
        print("   1. 用文本编辑器打开 converted.geojson 查看数据")
        print("   2. 用QGIS或其他GIS软件打开 converted.geojson 进行可视化")
        print("   3. 用Excel打开 coordinates_summary.csv 查看坐标摘要")

    except FileNotFoundError:
        print(f"❌ 文件未找到: {mvt_file_path}")
        print("💡 请确保文件路径正确，并修改代码中的 mvt_file_path 变量")
    except Exception as e:
        print(f"❌ 处理过程中出错: {e}")