# 坐标参考系

本文档介绍 CRS（Coordinate Reference System，坐标参考系），以及如何使用 Arctern 进行坐标系转换。

## 支持的坐标参考系统

Arctern 支持经纬度坐标系、墨卡托投影坐标系等常用的坐标参考系，关于坐标参考系的详细信息请查看 [Spatial Reference](https://spatialreference.org) 网站。

在 Arctern 中，你需要使用 SRID（Spatial Reference System Identifier，空间参考系标识符）格式的字符串来表示某个坐标参考系。例如，使用字符串 "EPSG:4326" 表示经纬度坐标系。

## 转换坐标参考系

在 Arctern 中转换坐标参考系的方法如下：

1. 使用 [`set_crs`](../../api_reference/standalone_api/api/arctern.GeoSeries.set_crs.html) 方法设置几何体的当前使用的坐标参考系。
2. 使用 [`to_crs`](../../api_reference/standalone_api/api/arctern.GeoSeries.to_crs.html) 方法对几何体执行坐标系转换。

以下展示如何使用 Arctern 将几何体对象由经纬度坐标系转换到墨卡托投影坐标系。

### 生成数据集

通过创建 GeoSeries 数据集，你可以批量地对数据集内所有几何体对象进行坐标参考系的转换。

首先，创建 WKT 格式的几何体对象：点 `point`、线 `linestring` 和多边形 `polygon`。然后，创建一个包含这三个几何体对象的 GeoSeries 对象 `geos` 。

```python
>>> from arctern import GeoSeries
>>> point = 'POINT (-73.993003 40.747594)'
>>> linestring = 'LINESTRING (-73.9594166 40.7593773,-73.9593736 40.7593593)'
>>> polygon = 'POLYGON ((-73.97324 40.73747, -73.96524 40.74507, -73.96118 40.75890, -73.95556 40.77654, -73.97324 40.73747))'
>>> geos = GeoSeries([point, linestring, polygon])
>>> geos
0                         POINT (-73.993003 40.747594)
1    LINESTRING (-73.9594166 40.7593773,-73.9593736...
2    POLYGON ((-73.97324 40.73747,-73.96524 40.7450...
dtype: GeoDtype
```

### 设置坐标参考系

使用 GeoSeries 对象的 [`set_crs`](../../api_reference/standalone_api/api/arctern.GeoSeries.set_crs.html) 方法，设置 `geos` 当前所属的坐标参考系。本例使用经纬度坐标系（EPSG:4326）作为初始坐标参考系。

<!-- [set_crs](/path/to/set_crs) -->

```python
>>> geos.set_crs("EPSG:4326")
>>> geos.crs
'EPSG:4326'
```

### 转换坐标

使用 GeoSeries 的 [`to_crs`](../../api_reference/standalone_api/api/arctern.GeoSeries.to_crs.html) 方法，将 `geos` 的坐标参考系统从经纬度坐标系（EPSG:4326）转换为墨卡托投影坐标系（EPSG:3857）。

<!-- [to_crs](/path/to/to_crs) -->

```python
>>> geos = geos.to_crs(crs="EPSG:3857")
>>> geos
0           POINT (-8236863.41622516 4975182.82064036)
1    LINESTRING (-8233124.59527958 4976914.39450424...
2    POLYGON ((-8234663.40912862 4973695.32847375,-...
dtype: GeoDtype
```

### 验证结果

使用 GeoSeries 的 [`crs`](../../api_reference/standalone_api/api/arctern.GeoSeries.crs.html) 属性，查看 `geos` 当前所属的坐标系。由输出结果可知，`geos` 的坐标参考系已成功转换为墨卡托投影坐标系。

```python
>>> geos.crs
'EPSG:3857'
```
