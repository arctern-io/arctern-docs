# 文件读写

Arctern 继承 pandas 的文件读写接口，支持读写数据类型为 [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry)、[WKB](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary) 以及 [GeoJson](https://geojson.org/) 的文件。关于通过 pandas 读写文件的具体方法可参考 [pandas 官方文档](https://pandas.pydata.org/pandas-docs/stable/reference/io.html)。

## 导入文件

### WKT 和 WKB 格式

本例使用 **wkt_geos.csv** 文件演示如何从文件读取 WKT 和 WKB 数据。此文件主要定义了四个 WKT 格式的几何体对象，包括一个点（POINT）和三个多边形（POLYGON）。文件内容如下：

```
geos
POINT (30 10)
POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))
POLYGON ((1 2, 3 4, 5 6, 1 2))
POLYGON ((1 1, 3 1, 3 3, 1 3, 1 1))
```

首先，使用 pandas 的 [`read_csv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) 方法导入文件并构造 pandas.Series 对象 `data_wkt`：

```python
>>> import pandas as pd
>>> import arctern
>>> 
>>> df = pd.read_csv("</path/to/wkt_geos.csv>",sep='|')
>>> data_wkt = df['geos']
>>> print(data_wkt)
0                                    POINT (30 10)
1    POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))
2                   POLYGON ((1 2, 3 4, 5 6, 1 2))
3              POLYGON ((1 1, 3 1, 3 3, 1 3, 1 1))
Name: geos, dtype: object
```

基于由 WKT 数据组成的 pandas.Series 对象 `data_wkt` 构造 arctern.GeoSeries 对象 `geo_wkt`：

```python
>>> geo_wkt = arctern.GeoSeries(data_wkt)
```

为了演示如何读取 WKB 格式的数据并创建 GeoSeries 对象，我们将之前从  **wkt_geos.csv** 文件中读取并创建的 pandas.Series 对象从 WKT 格式转换为 WKB 格式。具体方法是使用 [`to_wkb`](../../api_reference/standalone_api/api/arctern.GeoSeries.to_wkb.html) 方法从 GeoSeries 对象 `geo_wkt` 得到  WKB 格式的 pandas.Series 对象 `data_wkb`。

然后，基于 WKB 格式的 pandas.Series 对象 `data_wkb` 构造 arctern.GeoSeries 对象 `geo_wkb`：

<!-- [to_wkb](/path/to/to_wkb) -->

```python
>>> data_wkb = geo_wkt.to_wkb()
>>> geo_wkb = arctern.GeoSeries(data_wkb)
```

使用 GeoSeries 的 [`geom_equals`](../../api_reference/standalone_api/api/arctern.GeoSeries.geom_equals.html) 方法比较 `geo_wkt` 和 `geo_wkb` 两个 GeoSeries 对象，发现它们是相同的。这是因为 `geo_wkt` 和 `geo_wkb` 本质上都是由同一数据构造的 GeoSeries 对象。

```pytho
>>> geo_wkt.geom_equals(geo_wkb)
0    True
1    True
2    True
3    True
dtype: bool
```

### GeoJson 格式

本例使用 **geos.json** 文件演示如何从文件读取 GeoJson 数据。此文件主要定义了四个 WKT 格式的几何体对象，包括一个点（POINT）和三个多边形（POLYGON）。文件内容如下：

```
{
    "0":"{ \"type\": \"Point\", \"coordinates\": [ 30.0, 10.0 ] }",
    "1":"{ \"type\": \"Polygon\", \"coordinates\": [ [ [ 30.0, 10.0 ], [ 40.0, 40.0 ], [ 20.0, 40.0 ], [ 10.0, 20.0 ], [ 30.0, 10.0 ] ] ] }",
    "2":"{ \"type\": \"Polygon\", \"coordinates\": [ [ [ 1.0, 2.0 ], [ 3.0, 4.0 ], [ 5.0, 6.0 ], [ 1.0, 2.0 ] ] ] }",
    "3":"{ \"type\": \"Polygon\", \"coordinates\": [ [ [ 1.0, 1.0 ], [ 3.0, 1.0 ], [ 3.0, 3.0 ], [ 1.0, 3.0 ], [ 1.0, 1.0 ] ] ] }"
}
```

首先，使用 pandas 的 [`read_json`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html) 方法导入文件并构造 pandas.Series 对象 `data_json`：

```python
>>> df = pd.read_json("</path/to/geos.json>",orient='index')
>>> data_json = df[0]
>>> print(data_json)
0    { "type": "Point", "coordinates": [ 30.0, 10.0...
1    { "type": "Polygon", "coordinates": [ [ [ 30.0...
2    { "type": "Polygon", "coordinates": [ [ [ 1.0,...
3    { "type": "Polygon", "coordinates": [ [ [ 1.0,...
Name: geos, dtype: object
```

基于由 GeoJson 数据组成的 pandas.Series 对象 `data_json` 构造 arctern.GeoSeries 对象 `geo_json`：

```python
>>> geo_json = arctern.GeoSeries.geom_from_geojson(data_json)
```

使用 GeoSeries 的 [`geom_equals`](../../api_reference/standalone_api/api/arctern.GeoSeries.geom_equals.html) 方法比较 `geo_wkb` 和 `geo_json` 两个 GeoSeries 对象，发现它们是相同的。这是因为 `geo_wkb` 和 `geo_json` 的源文件（**wkt_geos.csv** 和 **geos.json**）中定义的是相同的几何体。

```python
>>> geo_json.geom_equals(geo_wkb)
0    True
1    True
2    True
3    True
dtype: bool
```

## 文件导出

### WKT 格式

首先，使用 GeoSeries 的 [`to_wkt`](../../api_reference/standalone_api/api/arctern.GeoSeries.to_wkt.html) 方法从 GeoSeries 对象得到一个 pandas.Series 对象。然后，使用 pandas.Series 的 [`to_csv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html) 方法将数据保存为 CSV 文件。

<!--  [to_wkt](/path/to/to_wkt)  -->

```python
>>> out_file_data = geo_wkb.to_wkt()
>>> print(out_file_data)
0                                POINT (30 10)
1    POLYGON ((30 10,40 40,20 40,10 20,30 10))
2                  POLYGON ((1 2,3 4,5 6,1 2))
3              POLYGON ((1 1,3 1,3 3,1 3,1 1))
dtype: object
>>> out_file_data.to_csv("</path/to/out_wkt_geos.csv>",index=None,quoting=1)
```

### GeoJson 格式

首先，使用 GeoSeries 的 [`as_geojson`](../../api_reference/standalone_api/api/arctern.GeoSeries.as_geojson.html) 方法从 GeoSeries 对象得到一个 pandas.Series 对象。然后，使用 pandas.Series 的 [`to_json`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html) 方法将数据保存为 JSON 文件。

<!--  [as_geojson](/path/to/as_geojson) -->

```python
>>> out_file_data = geo_wkb.as_geojson()
>>> print (out_file_data)
0    { "type": "Point", "coordinates": [ 30.0, 10.0...
1    { "type": "Polygon", "coordinates": [ [ [ 30.0...
2    { "type": "Polygon", "coordinates": [ [ [ 1.0,...
3    { "type": "Polygon", "coordinates": [ [ [ 1.0,...
dtype: object
>>> out_file_data.to_json("</path/to/out_geos.json>")
```