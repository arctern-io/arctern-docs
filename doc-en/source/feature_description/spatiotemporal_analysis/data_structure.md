# Data structure

## GeoSeries

GeoSeries is an array that stores and manipulates geometric datasets. By extending pandas Series, GeoSeries stores objects in WKB format internally, and calculates and operates on the stored batch elements like pandas Series.

### initialization

GeoSeries internally stores geometry in WKB format and accepts data in WKT or WKB format as input to initialize GeoSeries objects.

#### Initialization from WKT format data

You can put multiple string data in WKT format into a list, numpy.ndarray or pandas.Series, and then pass it to the GeoSeries constructor to create GeoSeries objects.

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

#### Initialization from WKB format data

You can put multiple string data in WKB format into a list, numpy.ndarray or pandas.Series, and then pass it to the GeoSeries constructor to create GeoSeries objects.

```python
>>> data = [b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?',
...        b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x08@']
>>> s = arctern.GeoSeries(data)
>>> s
0    POINT (1 1)
1    POINT (1 3)
dtype: GeoDtype
```

### Method overview

GeoSeries implements common operations on geometry, including unary operations and binary operations.

* When implementing a unary operation on a GeoSeries object, Arctern performs the operation on all the geometry stored in the GeoSeries object.
* When implementing binary operations on two GeoSeries objects, Arctern performs one-to-one operations on each of the geometries in the two GeoSeries objects by index.
* When implementing a binary operation on a GeoSeries object and a geometry (in WKB format), Arctern performs an operation on each geometry in the GeoSeries object and this geometry.

If the result of the operation is geometry, a new GeoSeries object is returned, otherwise a Pandas Series object is returned.

The following sections list some methods of GeoSeries, involving the measurement, relationship calculation and conversion of geometries. For detailed interface introduction, please see [API Reference](api_link).

#### Geometric measurement

- **GeoSeries.is_valid:** 判断 GeoSeries 对象中的每个几何体是否有效。
- **GeoSeries.area:** 计算 GeoSeries 对象中每个几何体的面积。
- **GeoSeries.distance:** 对于 GeoSeries 对象中的每个几何体，创建一个与它的最远距离不大于 `distance` 的几何体。
- **GeoSeries.distance_sphere:** 对于 GeoSeries 对象中的每个几何体，根据经纬度坐标计算地球表面两点之间的最短球面距离。该方法使用 SRID 定义的地球和半径。
- **GeoSeries.hausdorff_distance:** 对于 GeoSeries 对象中的每个几何体，判断它与 `other` 对象中相同位置的几何体之间的 Hausdorff 距离。此距离用于度量两个几何体之间的相似度。

#### Geometric relationship

- **GeoSeries.touches:** 对于 GeoSeries 对象中的每个几何体，判断它是否与 `other` 对象中相同位置的几何体相邻。“相邻”表示两个几何体在边界上有共同的点。
- **GeoSeries.overlaps:** 对于 GeoSeries 对象中的每个几何体，判断它是否与 `other` 对象中相同位置的几何体重叠。“重叠”表示两个几何体相交且不互相包含。
- **GeoSeries.intersects:** 对于 GeoSeries 对象中的每个几何体，判断它是否与 `other` 对象中相同位置的几何体存在交集。

#### Geometric conversion

- **GeoSeries.precision_reduce:** 对于 GeoSeries 对象中的每个几何体，根据指定的有效数字位数 `precision` 创建降低坐标精度后的几何体。
- **GeoSeries.make_valid:** 对于 GeoSeries 对象中的每个几何体，根据它创建一个新的有效的几何体。在构造新几何体过程中，不会删除原始几何体的任何顶点。如果原始几何体本来就是有效的，则直接返回原始几何体。
- **GeoSeries.curve_to_line:** 对于 GeoSeries 对象中的每个几何体，计算它的近似表示。近似表示的方法是将每个几何图形中的曲线转换为近似线性表示。

