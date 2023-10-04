import fiona
import sys
from shapely.geometry import shape, Point

def filter_geojson_within_saitama(input_path, output_path):
    # 埼玉県の境界データ (簡易的な境界を仮定; 実際の使用には正確なデータが必要)
    # この部分は、実際の埼玉県の境界のGeoJSONデータに基づいて更新してください。
    saitama_boundary = {
        "type": "Polygon",
        "coordinates": [[
            [138.7853877185277, 35.60366996577088],  # 左下の点
            [139.92796581997092, 35.588036420613264],  # 右下の点
            [139.90873974614857, 36.160004541212984],  # 右上の点
            [138.7853877185277, 36.07791358635634],  # 左上の点
            [138.7853877185277, 35.60366996577088]   # 最初の点に戻る（ポリゴンを閉じる）
        ]]
    }

    saitama_shape = shape(saitama_boundary)

    with fiona.open(input_path, 'r') as source:
        # 入力ファイルのスキーマとCRSをコピー
        schema = source.schema
        crs = source.crs

        # フィルタリングしたフィーチャーを格納するリスト
        filtered_features = []

        for feature in source:
            geom_type = feature['geometry']['type']
            if geom_type == "Polygon":
                polygon = shape(feature['geometry'])
                if polygon.intersects(saitama_shape):  
                    filtered_features.append(feature)
            # PolygonやLineStringなど、他のジオメトリタイプをサポートする場合は、以下に追加してください。

        with fiona.open(output_path, 'w', crs=crs, driver="GeoJSON", schema=schema) as output:
            output.writerecords(filtered_features)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python main.py <input.geojson> <output.geojson>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    filter_geojson_within_saitama(input_path, output_path)
