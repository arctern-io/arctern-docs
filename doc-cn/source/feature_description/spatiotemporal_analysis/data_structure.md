# 数据结构

## GeoSeries

GeoSeries 是一个存储和操作几何体数据集的数组。通过扩展 pandas Series，GeoSeries 在內部存储 WKB 格式的对象，并可以像 pandas Series 那样对所存的元素批量地计算和操作。

### 初始化

GeoSeries 在内部以 WKB 格式存储几何体，接受 WKT 或者 WKB 格式的数据作为输入来初始化 GeoSeries 对象。

#### 从 WKT 格式数据初始化

你可以将多个 WKT 格式的字符串数据放到一个 list、numpy.ndarray 或者 pandas.Series 中，然后传入 GeoSeries 的构造函数即可创建 GeoSeries 对象。

```python
>>> data = ['POINT(1 1)', 'POINT(1 3)']
>>> s = arctern.GeoSeries(data)
>>> s
0    POINT (1 1)
1    POINT (1 3)
dtype: GeoDtype
>>> data = pandas.Series(data)
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

以下列举 GeoSeries 的部分方法，包括了对几何体的度量、关系计算和转换等操作。详细的接口介绍请见 [API 参考](api_link)。

#### 几何度量

- **GeoSeries.is_valid:** 判断 GeoSeries 对象中的每个几何体是否有效。
- **GeoSeries.area:** 计算 GeoSeries 对象中每个几何体的面积。
- **GeoSeries.distance:** 对于 GeoSeries 对象中的每个几何体，创建一个与它的最远距离不大于 `distance` 的几何体。
- **GeoSeries.distance_sphere:** 对于 GeoSeries 对象中的每个几何体，根据经纬度坐标计算地球表面两点之间的最短球面距离。该方法使用 SRID 定义的地球和半径。
- **GeoSeries.hausdorff_distance:** 对于 GeoSeries 对象中的每个几何体，判断它与 `other` 对象中相同位置的几何体之间的 Hausdorff 距离。此距离用于度量两个几何体之间的相似度。

#### 几何关系计算

- **GeoSeries.touches:** 对于 GeoSeries 对象中的每个几何体，判断它是否与 `other` 对象中相同位置的几何体相邻。“相邻”表示两个几何体在边界上有共同的点。
- **GeoSeries.overlaps:** 对于 GeoSeries 对象中的每个几何体，判断它是否与 `other` 对象中相同位置的几何体重叠。“重叠”表示两个几何体相交且不互相包含。
- **GeoSeries.intersects:** 对于 GeoSeries 对象中的每个几何体，判断它是否与 `other` 对象中相同位置的几何体存在交集。

#### 几何转换

- **GeoSeries.precision_reduce:** 对于 GeoSeries 对象中的每个几何体，根据指定的有效数字位数 `precision` 创建降低坐标精度后的几何体。
- **GeoSeries.make_valid:** 对于 GeoSeries 对象中的每个几何体，根据它创建一个新的有效的几何体。在构造新几何体过程中，不会删除原始几何体的任何顶点。如果原始几何体本来就是有效的，则直接返回原始几何体。
- **GeoSeries.curve_to_line:** 对于 GeoSeries 对象中的每个几何体，计算它的近似表示。近似表示的方法是将每个几何图形中的曲线转换为近似线性表示。

