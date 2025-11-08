import mapbox_vector_tile
import json
import math
from pathlib import Path
import re


def extract_tile_params_from_filename(filename):
    """
    从文件名中提取瓦片参数 (z_x_y.mvt 格式)
    """
    # 使用正则表达式匹配 z_x_y 模式
    pattern = r'(\d+)_(\d+)_(\d+)\.mvt$'
    match = re.search(pattern, filename)

    if match:
        z = int(match.group(1))
        x = int(match.group(2))
        y = int(match.group(3))
        return z, x, y
    else:
        raise ValueError(f"无法从文件名 '{filename}' 中提取瓦片参数")


def convert_relative_to_geographic(rel_x, rel_y, tile_z, tile_x, tile_y, extent=4096):
    """
    将相对坐标转换为真实经纬度
    """
    # 将相对坐标转换为瓦片内的绝对坐标
    absolute_x = tile_x + rel_x / extent
    absolute_y = tile_y + rel_y / extent

    # 将绝对坐标转换为经纬度
    n = 2.0 ** tile_z
    lon_deg = absolute_x / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * absolute_y / n)))
    lat_deg = math.degrees(lat_rad)

    return lon_deg, lat_deg


def extract_and_convert_all_coordinates(mvt_file_path, output_geojson_path="converted_all.geojson"):
    """
    使用文件名中的瓦片参数转换MVT文件中的所有要素为经纬度坐标
    """
    # 从文件名提取瓦片参数
    filename = Path(mvt_file_path).name
    try:
        tile_z, tile_x, tile_y = extract_tile_params_from_filename(filename)
        print(f"✅ 从文件名提取瓦片参数: z={tile_z}, x={tile_x}, y={tile_y}")
    except ValueError as e:
        print(f"❌ {e}")
        return None

    # 读取MVT文件
    with open(mvt_file_path, 'rb') as f:
        mvt_data = f.read()

    decoded_data = mapbox_vector_tile.decode(mvt_data)

    print("=== MVT文件坐标转换 ===")
    print(f"处理文件: {filename}")
    print(f"使用瓦片参数: z={tile_z}, x={tile_x}, y={tile_y}")
    print("=" * 60)

    # 构建包含真实经纬度的GeoJSON
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    total_features = 0
    features_with_direct_coords = 0
    features_with_converted_coords = 0
    conversion_errors = 0

    # 遍历所有图层和要素
    for layer_name, layer_info in decoded_data.items():
        print(f"\n📋 图层: {layer_name}")
        layer_features = len(layer_info.get('features', []))
        print(f"   要素数量: {layer_features}")

        layer_direct = 0
        layer_converted = 0

        for i, feature in enumerate(layer_info.get('features', [])):
            total_features += 1
            properties = feature.get('properties', {})
            geometry = feature['geometry']
            geom_type = geometry['type']

            # 检查是否包含直接经纬度信息
            has_direct_coords = 'centerX' in properties and 'centerY' in properties

            try:
                if has_direct_coords:
                    features_with_direct_coords += 1
                    layer_direct += 1

                    # 使用直接提供的经纬度
                    longitude = float(properties['centerX'])
                    latitude = float(properties['centerY'])

                    # 创建点要素
                    converted_geometry = {
                        "type": "Point",
                        "coordinates": [longitude, latitude]
                    }

                    coord_source = 'direct'

                else:
                    features_with_converted_coords += 1
                    layer_converted += 1

                    # 转换相对坐标为经纬度
                    if geom_type == 'Point':
                        rel_x, rel_y = geometry['coordinates']
                        lon, lat = convert_relative_to_geographic(rel_x, rel_y, tile_z, tile_x, tile_y)

                        converted_geometry = {
                            "type": "Point",
                            "coordinates": [lon, lat]
                        }

                    elif geom_type == 'LineString':
                        converted_coords = []
                        for coord in geometry['coordinates']:
                            rel_x, rel_y = coord
                            lon, lat = convert_relative_to_geographic(rel_x, rel_y, tile_z, tile_x, tile_y)
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
                                lon, lat = convert_relative_to_geographic(rel_x, rel_y, tile_z, tile_x, tile_y)
                                converted_ring.append([lon, lat])
                            converted_rings.append(converted_ring)

                        converted_geometry = {
                            "type": "Polygon",
                            "coordinates": converted_rings
                        }

                    elif geom_type == 'MultiPolygon':
                        converted_polygons = []
                        for polygon in geometry['coordinates']:
                            converted_rings = []
                            for ring in polygon:
                                converted_ring = []
                                for coord in ring:
                                    rel_x, rel_y = coord
                                    lon, lat = convert_relative_to_geographic(rel_x, rel_y, tile_z, tile_x, tile_y)
                                    converted_ring.append([lon, lat])
                                converted_rings.append(converted_ring)
                            converted_polygons.append(converted_rings)

                        converted_geometry = {
                            "type": "MultiPolygon",
                            "coordinates": converted_polygons
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

        print(f"   直接坐标: {layer_direct}, 转换坐标: {layer_converted}")

    # 保存为GeoJSON文件
    with open(output_geojson_path, 'w', encoding='utf-8') as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    # 打印统计信息
    print("\n" + "=" * 60)
    print("📊 转换结果统计:")
    print(f"   总要素数量: {total_features}")
    print(f"   使用直接经纬度的要素: {features_with_direct_coords}")
    print(f"   转换相对坐标的要素: {features_with_converted_coords}")
    print(f"   转换错误: {conversion_errors}")
    print(f"   成功转换的要素: {len(geojson['features'])}")
    print(f"   生成的GeoJSON文件: {output_geojson_path}")

    # 分析地理范围
    if geojson['features']:
        all_coords = extract_all_coordinates(geojson)
        if all_coords:
            lons = [coord[0] for coord in all_coords]
            lats = [coord[1] for coord in all_coords]
            print(f"\n🌍 地理范围:")
            print(f"   经度: {min(lons):.6f}°E ~ {max(lons):.6f}°E")
            print(f"   纬度: {min(lats):.6f}°N ~ {max(lats):.6f}°N")
            print(f"   中心: {(min(lons) + max(lons)) / 2:.6f}°E, {(min(lats) + max(lats)) / 2:.6f}°N")

            # 计算并显示地理范围对应的实际距离
            from geopy.distance import geodesic
            if len(all_coords) >= 2:
                point1 = (lats[0], lons[0])
                point2 = (lats[-1], lons[-1])
                distance = geodesic(point1, point2).meters
                print(f"   对角线距离: {distance:.2f} 米")

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


def create_detailed_summary(geojson_data, output_csv="coordinates_detailed_summary.csv"):
    """
    创建详细的坐标摘要CSV文件
    """
    import csv

    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['layer', 'geometry_type', 'longitude', 'latitude', 'coord_source', 'name', 'icao', 'spaceId', 'featureId']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for feature in geojson_data['features']:
            geom = feature['geometry']
            properties = feature['properties']

            if geom['type'] == 'Point':
                lon, lat = geom['coordinates']
                row = {
                    'layer': properties.get('mvt_layer', ''),
                    'geometry_type': geom['type'],
                    'longitude': lon,
                    'latitude': lat,
                    'coord_source': properties.get('coord_source', 'unknown'),
                    'name': properties.get('name', ''),
                    'icao': properties.get('icao', ''),
                    'spaceId': properties.get('spaceId', ''),
                    'featureId': properties.get('featureId', '')
                }
                writer.writerow(row)
            else:
                # 对于非点要素，取第一个坐标点作为代表
                if geom['type'] == 'LineString' and geom['coordinates']:
                    lon, lat = geom['coordinates'][0]
                elif geom['type'] == 'Polygon' and geom['coordinates'] and geom['coordinates'][0]:
                    lon, lat = geom['coordinates'][0][0]
                else:
                    continue

                row = {
                    'layer': properties.get('mvt_layer', ''),
                    'geometry_type': geom['type'],
                    'longitude': lon,
                    'latitude': lat,
                    'coord_source': properties.get('coord_source', 'unknown'),
                    'name': properties.get('name', ''),
                    'icao': properties.get('icao', ''),
                    'spaceId': properties.get('spaceId', ''),
                    'featureId': properties.get('featureId', '')
                }
                writer.writerow(row)

    print(f"   详细坐标摘要CSV: {output_csv}")


def create_visualization_html(geojson_path, output_html="visualization.html"):
    """
    创建可视化HTML页面
    """
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>MVT数据可视化 - {Path(geojson_path).name}</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
    <style>
        #map {{ height: 700px; }}
        body {{ margin: 0; padding: 20px; font-family: Arial, sans-serif; }}
        .info {{ padding: 10px; background: white; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.2); }}
        .legend {{ line-height: 18px; color: #555; background: white; padding: 10px; border-radius: 5px; }}
        .legend i {{ width: 18px; height: 18px; float: left; margin-right: 8px; opacity: 0.7; }}
    </style>
</head>
<body>
    <h1>MVT数据地理可视化</h1>
    <div id="map"></div>

    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
    <script>
        // 读取GeoJSON数据
        fetch('{Path(geojson_path).name}')
            .then(response => response.json())
            .then(data => {{
                // 计算中心点
                let lons = [];
                let lats = [];

                data.features.forEach(feature => {{
                    if (feature.geometry.type === 'Point') {{
                        lons.push(feature.geometry.coordinates[0]);
                        lats.push(feature.geometry.coordinates[1]);
                    }}
                }});

                const centerLon = lons.reduce((a, b) => a + b, 0) / lons.length;
                const centerLat = lats.reduce((a, b) => a + b, 0) / lats.length;

                // 创建地图
                const map = L.map('map').setView([centerLat, centerLon], 15);

                // 添加地图图层
                L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
                    attribution: '© OpenStreetMap contributors'
                }}).addTo(map);

                // 定义样式函数
                function getStyle(feature) {{
                    const layer = feature.properties.mvt_layer;
                    let color = '#3388ff';

                    if (layer.includes('apron')) color = '#ff7800';
                    if (layer.includes('runway')) color = '#555555';
                    if (layer.includes('vertical')) color = '#e41a1c';
                    if (layer.includes('taxiway')) color = '#ffff33';

                    return {{
                        color: color,
                        weight: 2,
                        opacity: 0.8,
                        fillOpacity: 0.6
                    }};
                }}

                // 添加GeoJSON图层
                L.geoJSON(data, {{
                    pointToLayer: function(feature, latlng) {{
                        return L.circleMarker(latlng, {{
                            radius: 6,
                            fillColor: getStyle(feature).color,
                            color: "#000",
                            weight: 1,
                            opacity: 1,
                            fillOpacity: 0.8
                        }});
                    }},
                    style: getStyle,
                    onEachFeature: function(feature, layer) {{
                        let popupContent = "<b>" + (feature.properties.name || feature.properties.mvt_layer) + "</b><br>";
                        if (feature.properties.icao) {{
                            popupContent += `ICAO: ${{feature.properties.icao}}<br>`;
                        }}
                        if (feature.geometry.type === 'Point') {{
                            popupContent += `经度: ${{feature.geometry.coordinates[0].toFixed(6)}}<br>`;
                            popupContent += `纬度: ${{feature.geometry.coordinates[1].toFixed(6)}}<br>`;
                        }}
                        popupContent += `坐标来源: ${{feature.properties.coord_source}}<br>`;
                        popupContent += `图层: ${{feature.properties.mvt_layer}}`;
                        layer.bindPopup(popupContent);
                    }}
                }}).addTo(map);

                // 添加图例
                const legend = L.control({{position: 'bottomright'}});
                legend.onAdd = function (map) {{
                    const div = L.DomUtil.create('div', 'legend');
                    div.innerHTML = `
                        <h4>图例</h4>
                        <div><i style="background:#ff7800"></i> 停机坪区域</div>
                        <div><i style="background:#555555"></i> 跑道相关</div>
                        <div><i style="background:#e41a1c"></i> 垂直结构</div>
                        <div><i style="background:#ffff33"></i> 滑行道</div>
                        <div><i style="background:#3388ff"></i> 其他</div>
                    `;
                    return div;
                }};
                legend.addTo(map);
            }});
    </script>
</body>
</html>
    """

    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"   可视化页面: {output_html}")


# 主执行函数
if __name__ == "__main__":
    # MVT文件路径 - 确保文件名包含 z_x_y 格式
    mvt_file_path = "./data/12_3337_1773.mvt"  # 修改为实际路径

    try:
        # 转换所有要素为经纬度
        geojson_data = extract_and_convert_all_coordinates(mvt_file_path)

        if geojson_data:
            # 创建详细摘要
            create_detailed_summary(geojson_data)

            # 创建可视化页面
            create_visualization_html("converted_all.geojson")

            print("\n✅ 转换完成！")
            print("🎯 下一步操作:")
            print("   1. 用浏览器打开 visualization.html 查看交互式地图")
            print("   2. 用QGIS打开 converted_all.geojson 进行专业分析")
            print("   3. 检查 coordinates_detailed_summary.csv 查看详细数据")

    except FileNotFoundError:
        print(f"❌ 文件未找到: {mvt_file_path}")
        print("💡 请确保文件路径正确，且文件名包含 z_x_y 格式（如 12_3337_1773.mvt）")
    except Exception as e:
        print(f"❌ 处理过程中出错: {e}")
        import traceback

        traceback.print_exc()