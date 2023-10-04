# GeojsonFilter

`GeojsonFilter` is a tool designed to extract features from a provided GeoJSON file that lie within the boundary, and then writes them into a new GeoJSON file.

## Usage

1. First, install the necessary libraries:
```bash
pip install fiona shapely
```

2. Execute the program from the command line as follows:
```bash
python main.py [Path to Input GeoJSON File] [Path to Output GeoJSON File]
```
Example:
```bash
python main.py input.geojson output.geojson
```

## Description

- Takes a GeoJSON file as input.
- Filters out features based on whether they lie within the boundary of Saitama Prefecture.
- Writes the filtered features to a new GeoJSON file.

---

# GeojsonFilter

`GeojsonFilter`は、提供されたGeoJSONファイルから特定の地域に属するフィーチャのみを抽出して、新しいGeoJSONファイルに書き出すツールです。

## 使い方

1. まず、必要なライブラリをインストールします：
```bash
pip install fiona shapely
```

2. コマンドラインから、次のようにプログラムを実行します：
```bash
python main.py [入力GeoJSONファイルパス] [出力GeoJSONファイルパス]
```
例：
```bash
python main.py input.geojson output.geojson
```

## 仕様

- 入力として受け取るGeoJSONファイルは、`Polygon`ジオメトリを持つフィーチャを含むことを想定しています。
- プログラムは、埼玉県の境界と交差するフィーチャのみを新しいGeoJSONファイルに書き出します。

## 注意

現在の埼玉県の境界は簡易的なものを使用しています。実際の使用には、正確な境界データを用意して、プログラム内の`saitama_boundary`変数を更新する必要があります。
