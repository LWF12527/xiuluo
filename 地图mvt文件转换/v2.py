import mapbox_vector_tile
import json
import math
from pathlib import Path
import re


def extract_tile_params_from_filename(filename):
    """
    从文件名中提取瓦片参数 (z_x_y.mvt 格式)
    """
    pattern = r'(\d+)_(\d+)_(\d+)\.mvt$'
    match = re.search(pattern, filename)

    if match:
        z = int(match.group(1))
        x = int(match.group(2))
        y = int(match.group(3))
        return z, x, y
    else:
        raise ValueError(f"无法从文件名 '{filename}' 中提取瓦片参数")


def tile_to_lonlat(tile_x, tile_y, zoom):
    """
    将瓦片坐标转换为经纬度（瓦片左上角）
    """
    n = 2.0 ** zoom
    lon_deg = tile_x / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * tile_y / n)))
    lat_deg = math.degrees(lat_rad)
    return lon_deg, lat_deg


def correct_web_mercator_to_wgs84(x, y, zoom, tile_x, tile_y):
    """
    修正的Web墨卡托到WGS84坐标转换
    """
    # 计算瓦片左上角的经纬度
    tile_left, tile_top = tile_to_lonlat(tile_x, tile_y, zoom)
    tile_right, tile_bottom = tile_to_lonlat(tile_x + 1, tile_y + 1, zoom)

    # 瓦片内的相对坐标 (0-4096)
    rel_x = x / 4096.0
    rel_y = y / 4096.0

    # 线性插值计算实际经纬度
    lon = tile_left + rel_x * (tile_right - tile_left)
    lat = tile_top - rel_y * (tile_top - tile_bottom)  # 注意y轴方向

    return lon, lat


def convert_mvt_coordinates(rel_x, rel_y, tile_z, tile_x, tile_y, method='accurate'):
    """
    转换MVT相对坐标为经纬度

    Parameters:
    - method: 'accurate' 使用精确转换, 'simple' 使用简单转换
    """
    if method == 'accurate':
        # 精确转换方法
        return correct_web_mercator_to_wgs84(rel_x, rel_y, tile_z, tile_x, tile_y)
    else:
        # 简单转换方法（之前的方法）
        n = 2.0 ** tile_z
        absolute_x = tile_x + rel_x / 4096.0
        absolute_y = tile_y + rel_y / 4096.0

        lon_deg = absolute_x / n * 360.0 - 180.0
        lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * absolute_y / n)))
        lat_deg = math.degrees(lat_rad)

        return lon_deg, lat_deg


def extract_and_convert_all_coordinates(mvt_file_path, output_geojson_path="converted_corrected.geojson", method='accurate'):
    """
    使用修正的坐标转换方法转换MVT文件
    """
    # 从文件名提取瓦片参数
    filename = Path(mvt_file_path).name
    try:
        tile_z, tile_x, tile_y = extract_tile_params_from_filename(filename)
        print(f"✅ 从文件名提取瓦片参数: z={tile_z}, x={tile_x}, y={tile_y}")
    except ValueError as e:
        print(f"❌ {e}")
        return None

    # 计算瓦片边界作为参考
    tile_left, tile_top = tile_to_lonlat(tile_x, tile_y, tile_z)
    tile_right, tile_bottom = tile_to_lonlat(tile_x + 1, tile_y + 1, tile_z)
    print(f"📍 瓦片地理范围:")
    print(f"   左上角: {tile_left:.6f}°E, {tile_top:.6f}°N")
    print(f"   右下角: {tile_right:.6f}°E, {tile_bottom:.6f}°N")

    # 读取MVT文件
    with open(mvt_file_path, 'rb') as f:
        mvt_data = f.read()

    decoded_data = mapbox_vector_tile.decode(mvt_data)

    print(f"\n=== MVT文件坐标转换 ({method}方法) ===")
    print(f"处理文件: {filename}")
    print("=" * 60)

    # 构建包含真实经纬度的GeoJSON
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    total_features = 0
    conversion_errors = 0

    # 遍历所有图层和要素
    for layer_name, layer_info in decoded_data.items():
        print(f"\n📋 图层: {layer_name}")
        layer_features = len(layer_info.get('features', []))
        print(f"   要素数量: {layer_features}")

        for i, feature in enumerate(layer_info.get('features', [])):
            total_features += 1
            properties = feature.get('properties', {})
            geometry = feature['geometry']
            geom_type = geometry['type']

            try:
                # 检查是否包含直接经纬度信息
                has_direct_coords = 'centerX' in properties and 'centerY' in properties

                if has_direct_coords:
                    # 使用直接提供的经纬度
                    longitude = float(properties['centerX'])
                    latitude = float(properties['centerY'])

                    converted_geometry = {
                        "type": "Point",
                        "coordinates": [longitude, latitude]
                    }
                    coord_source = 'direct'

                else:
                    # 转换相对坐标为经纬度
                    if geom_type == 'Point':
                        rel_x, rel_y = geometry['coordinates']
                        lon, lat = convert_mvt_coordinates(rel_x, rel_y, tile_z, tile_x, tile_y, method)

                        converted_geometry = {
                            "type": "Point",
                            "coordinates": [lon, lat]
                        }

                    elif geom_type == 'LineString':
                        converted_coords = []
                        for coord in geometry['coordinates']:
                            rel_x, rel_y = coord
                            lon, lat = convert_mvt_coordinates(rel_x, rel_y, tile_z, tile_x, tile_y, method)
                            converted_coords.append([lon, lat])

                        converted_geometry = {
                            "type": "LineString",
                            "coordinates": converted_coords
                        }

                    elif geom_type == 'Polygon':
                        converted_rings = []
                        for ring in geometry['coordinates']:
                            converted_ring = []
                            for coord in ring:
                                rel_x, rel_y = coord
                                lon, lat = convert_mvt_coordinates(rel_x, rel_y, tile_z, tile_x, tile_y, method)
                                converted_ring.append([lon, lat])
                            converted_rings.append(converted_ring)

                        converted_geometry = {
                            "type": "Polygon",
                            "coordinates": converted_rings
                        }

                    else:
                        print(f"   ⚠️  跳过不支持的几何类型: {geom_type}")
                        continue

                    coord_source = 'converted'

                # 创建GeoJSON要素
                geojson_feature = {
                    "type": "Feature",
                    "geometry": converted_geometry,
                    "properties": properties.copy()
                }

                # 添加元数据
                geojson_feature['properties']['mvt_layer'] = layer_name
                geojson_feature['properties']['coord_source'] = coord_source
                geojson_feature['properties']['original_geometry_type'] = geom_type

                geojson['features'].append(geojson_feature)

            except Exception as e:
                conversion_errors += 1
                print(f"   ❌ 要素 {i + 1} 转换错误: {e}")
                continue

    # 保存为GeoJSON文件
    with open(output_geojson_path, 'w', encoding='utf-8') as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    # 打印统计信息
    print("\n" + "=" * 60)
    print("📊 转换结果统计:")
    print(f"   总要素数量: {total_features}")
    print(f"   转换错误: {conversion_errors}")
    print(f"   成功转换的要素: {len(geojson['features'])}")
    print(f"   生成的GeoJSON文件: {output_geojson_path}")

    # 分析地理范围
    if geojson['features']:
        all_coords = extract_all_coordinates(geojson)
        if all_coords:
            lons = [coord[0] for coord in all_coords]
            lats = [coord[1] for coord in all_coords]
            print(f"\n🌍 转换后地理范围:")
            print(f"   经度: {min(lons):.6f}°E ~ {max(lons):.6f}°E")
            print(f"   纬度: {min(lats):.6f}°N ~ {max(lats):.6f}°N")
            print(f"   中心: {(min(lons) + max(lons)) / 2:.6f}°E, {(min(lats) + max(lats)) / 2:.6f}°N")

    return geojson


def extract_all_coordinates(geojson):
    """从GeoJSON中提取所有坐标点"""
    all_coords = []
    for feature in geojson['features']:
        geom = feature['geometry']
        if geom['type'] == 'Point':
            all_coords.append(geom['coordinates'])
        elif geom['type'] in ['LineString', 'MultiLineString']:
            for coord in geom['coordinates']:
                if isinstance(coord[0], list):  # MultiLineString
                    for sub_coord in coord:
                        all_coords.append(sub_coord)
                else:
                    all_coords.append(coord)
        elif geom['type'] in ['Polygon', 'MultiPolygon']:
            for ring_or_poly in geom['coordinates']:
                for ring in (ring_or_poly if isinstance(ring_or_poly[0][0], list) else [ring_or_poly]):
                    for coord in ring:
                        all_coords.append(coord)
    return all_coords


def compare_coordinate_methods(mvt_file_path):
    """
    比较不同坐标转换方法的结果
    """
    print("=== 坐标转换方法比较 ===")

    # 从文件名提取瓦片参数
    filename = Path(mvt_file_path).name
    tile_z, tile_x, tile_y = extract_tile_params_from_filename(filename)

    # 计算瓦片边界
    tile_left, tile_top = tile_to_lonlat(tile_x, tile_y, tile_z)
    tile_right, tile_bottom = tile_to_lonlat(tile_x + 1, tile_y + 1, tile_z)

    print(f"瓦片 {tile_z}/{tile_x}/{tile_y} 的地理范围:")
    print(f"  左上角: {tile_left:.6f}°E, {tile_top:.6f}°N")
    print(f"  右下角: {tile_right:.6f}°E, {tile_bottom:.6f}°N")

    # 测试几个关键点的转换
    test_points = [
        (0, 0),  # 左上角
        (2048, 2048),  # 中心点
        (4096, 4096)  # 右下角
    ]

    print("\n坐标转换结果比较:")
    print("相对坐标 | 简单方法 | 精确方法")
    print("-" * 50)

    for rel_x, rel_y in test_points:
        lon_simple, lat_simple = convert_mvt_coordinates(rel_x, rel_y, tile_z, tile_x, tile_y, 'simple')
        lon_accurate, lat_accurate = convert_mvt_coordinates(rel_x, rel_y, tile_z, tile_x, tile_y, 'accurate')

        print(f"({rel_x}, {rel_y}) | {lon_simple:.6f}°E, {lat_simple:.6f}°N | {lon_accurate:.6f}°E, {lat_accurate:.6f}°N")

    # 计算两种方法的差异
    center_simple = convert_mvt_coordinates(2048, 2048, tile_z, tile_x, tile_y, 'simple')
    center_accurate = convert_mvt_coordinates(2048, 2048, tile_z, tile_x, tile_y, 'accurate')

    diff_lon = abs(center_simple[0] - center_accurate[0]) * 111000  # 转换为米 (1度≈111km)
    diff_lat = abs(center_simple[1] - center_accurate[1]) * 111000

    print(f"\n📍 中心点转换差异:")
    print(f"   经度差异: {diff_lon:.2f} 米")
    print(f"   纬度差异: {diff_lat:.2f} 米")
    print(f"   总距离差异: {math.sqrt(diff_lon ** 2 + diff_lat ** 2):.2f} 米")


# 主执行函数
if __name__ == "__main__":
    # MVT文件路径
    mvt_file_path = "./data/12_3337_1773.mvt"

    try:
        # 首先比较不同转换方法
        compare_coordinate_methods(mvt_file_path)

        print("\n" + "=" * 60)
        print("请选择转换方法:")
        print("1. 简单方法 (之前的方法)")
        print("2. 精确方法 (推荐)")

        choice = input("请输入选择 (1 或 2): ").strip()

        if choice == "1":
            method = 'simple'
            output_file = "converted_simple.geojson"
        else:
            method = 'accurate'
            output_file = "converted_accurate.geojson"

        # 执行转换
        geojson_data = extract_and_convert_all_coordinates(
            mvt_file_path,
            output_geojson_path=output_file,
            method=method
        )

        if geojson_data:
            print(f"\n✅ 转换完成！使用方法: {method}")
            print("🎯 下一步:")
            print("   1. 在GIS软件中打开生成的GeoJSON文件")
            print("   2. 检查是否与真实地理位置对齐")
            print("   3. 如果仍有偏移，可能需要调整坐标转换参数")

            # 提供验证建议
            print("\n💡 验证建议:")
            print("   1. 在OpenStreetMap中查看瓦片 12/3337/1773 的位置")
            print("   2. 比较转换后的数据是否与该位置对齐")
            print("   3. 如果偏移较大，可能需要使用专业的GIS工具进行校准")

    except FileNotFoundError:
        print(f"❌ 文件未找到: {mvt_file_path}")
    except Exception as e:
        print(f"❌ 处理过程中出错: {e}")
        import traceback

        traceback.print_exc()