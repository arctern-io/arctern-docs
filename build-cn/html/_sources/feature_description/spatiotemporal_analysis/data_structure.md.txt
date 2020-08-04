# 数据结构

## GeoSeries

GeoSeries 是一个存储和操作几何体数据集的数组。通过扩展 pandas Series，GeoSeries 在內部存储 WKB 格式的对象，并可以像 pandas Series 那样对所存的元素批量地计算和操作。

### 初始化

GeoSeries 在内部以 WKB 格式存储几何体，接受 WKT 或者 WKB 格式的数据作为输入来初始化 GeoSeries 对象。

#### 从 WKT 格式数据初始化

你可以将多个 WKT 格式的字符串数据放到一个 list、numpy.ndarray 或者 pandas.Series 中，然后传入 GeoSeries 的构造函数即可创建 GeoSeries 对象。

```python
>>> import pandas as pd
>>> data = ['POINT(1 1)', 'POINT(1 3)']
>>> s = arctern.GeoSeries(data)
>>> s
0    POINT (1 1)
1    POINT (1 3)
dtype: GeoDtype
>>> data = pd.Series(data)
>>> s = arctern.GeoSeries(data)
>>> s
0    POINT (1 1)
1    POINT (1 3)
dtype: GeoDtype
```

#### 从 WKB 格式数据初始化

你可以将多个 WKB 格式的字符串数据放到一个 list、numpy.ndarray 或者 pandas.Series 中，然后传入 GeoSeries 的构造函数即可创建 GeoSeries 对象。
```python
>>> data = [b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?',
...        b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x08@']
>>> s = arctern.GeoSeries(data)
>>> s
0    POINT (1 1)
1    POINT (1 3)
dtype: GeoDtype
```

### 方法概览

GeoSeries 实现了对几何体的常见操作（一元操作和二元操作）。

* 对一个 GeoSeries 对象执行一元操作时，Arctern 对该 GeoSeries 对象中存储的所有几何体执行该操作。
* 对两个 GeoSeries 对象执行二元操作时，Arctern 对这两个 GeoSeries 对象中的每个几何体按照索引一对一地执行操作。
* 对一个 GeoSeries 对象和一个几何体（WKB 格式的对象）执行二元操作时，Arctern 将该 GeoSeries 对象中的每一个几何体和这个几何体执行操作。

如果操作的结果是几何体，那么会返回一个新的 GeoSeries 对象，否则返回一个 Pandas Series 对象。

以下列举 GeoSeries 的部分方法，包括了对几何体的度量、关系计算和转换等操作。详细的 API 介绍请见 [API 参考](../../api_reference/standalone_api/geoseries.html)。

#### 几何度量

- **[GeoSeries.is_valid](../../api_reference/standalone_api/api/arctern.GeoSeries.is_valid.html):** 检查 GeoSeries 中的每个几何体是否为有效格式，例如 WKT 和 WKB 格式。
- **[GeoSeries.area](../../api_reference/standalone_api/api/arctern.GeoSeries.area.html):** 计算 GeoSeries 中每个几何体的 2D 笛卡尔（平面）面积。
- **[GeoSeries.distance](../../api_reference/standalone_api/api/arctern.GeoSeries.distance.html):** 对于 GeoSeries 中的每个几何体以及 `other` 中给出的对应几何体，计算它们之间的最小 2D 笛卡尔（平面）距离。
- **[GeoSeries.distance_sphere](../../api_reference/standalone_api/api/arctern.GeoSeries.distance_sphere.html):** 对于 GeoSeries 中的每个几何体以及 `other` 中给出的对应几何体，计算它们之间的最小球面距离。
- **[GeoSeries.hausdorff_distance](../../api_reference/standalone_api/api/arctern.GeoSeries.hausdorff_distance.html):** 对于 GeoSeries 中的每个几何体以及 `other` 中给出的对应几何体，计算它们之间的 Hausdorff 距离。

#### 几何关系计算

- **[GeoSeries.touches](../../api_reference/standalone_api/api/arctern.GeoSeries.touches.html):** 对于 GeoSeries 中的每个几何体以及 `other` 中给出的对应几何体，检测它们是否接触。
- **[GeoSeries.overlaps](../../api_reference/standalone_api/api/arctern.GeoSeries.overlaps.html):** 对于 GeoSeries 中的每个几何体以及 other 中给出的对应几何体，检查第一个几何体是否与另一个几何体空间重叠。
- **[GeoSeries.intersects](../../api_reference/standalone_api/api/arctern.GeoSeries.intersects.html):** 对于 GeoSeries 中的每个几何体以及 other 中给出的对应的几何体，检测它们是否相交。

#### 几何转换

- **[GeoSeries.precision_reduce](../../api_reference/standalone_api/api/arctern.GeoSeries.precision_reduce.html):** 对于 GeoSeries 中每个几何体的坐标，将有效数字的位数减少到给定的数字。
- **[GeoSeries.make_valid](../../api_reference/standalone_api/api/arctern.GeoSeries.make_valid.html):** 在不丢失任何输入顶点的情况下，为 GeoSeries 中的每个几何体创建有效的表示。
- **[GeoSeries.curve_to_line](../../api_reference/standalone_api/api/arctern.GeoSeries.curve_to_line.html):** 将每个几何体中的曲线转换为近似线性表示。

