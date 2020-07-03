# 与 GeoPandas GeoSeries 互相转换

Arctern 可以与 GeoPandas 生态无缝衔接。通过灵活切换 Arctern GeoSeries 与 GeoPandas GeoSeries，你可以提高空间地理信息的处理效率。例如，在大数据量的场景下，GeoPandas 的运行速度不够理想，而 Arctern 对 GeoSeries 的部分功能进行了 GPU 加速。因此，你可以使用 Arctern 的 `to_geopandas` 和 `from_geopandas` 方法把 GeoPandas GeoSeries 转为 Arctern GeoSeries，发挥 Arctern 的运算加速能力。

本文档介绍如何在 Arctern GeoSeries 与 GeoPandas GeoSeries 之间进行转换。

## 构造 Arctern GeoSeries

构造一个 Arctern GeoSeries 对象 `arctern_geoseries`。

```python
>>> import arctern
>>> 
>>> p1 = "POLYGON ((0 0,4 0,4 4,0 4,0 0))"
>>> arctern_geoseries = arctern.GeoSeries([p1])
>>> arctern_geoseries
0    POLYGON ((0 0,4 0,4 4,0 4,0 0))
dtype: GeoDtype
```

## 将 Arctern GeoSeries 转换为 GeoPandas GeoSeries

使用 [`to_geopandas`](../../api_reference/standalone_api/api/arctern.GeoSeries.to_geopandas.html) 方法将 Arctern GeoSeries 转为 GeoPandas GeoSeries。

<!-- link: [to_geopandas](/path/to/to_geopandas) -->

```python
>>> geopandas_geoseries = arctern_geoseries.to_geopandas()
>>> geopandas_geoseries
0    POLYGON ((0.00000 0.00000, 4.00000 0.00000, 4.00000 4.00000, 0.00000 4.00000, 0.00000 0.00000))
dtype: geometry
```

## 将 GeoPandas GeoSeries 转换为 Arctern GeoSeries

使用 [`from_geopandas`](../../api_reference/standalone_api/api/arctern.GeoSeries.from_geopandas.html) 方法将 GeoPandas GeoSeries 转为 Arctern GeoSeries。

<!-- link: [from_geopandas](/path/to/from_geopandas) -->

```python
>>> arctern_geoseries = arctern.GeoSeries.from_geopandas(geopandas_geoseries)
>>> arctern_geoseries
0    POLYGON ((0 0,4 0,4 4,0 4,0 0))
dtype: GeoDtype
```

<!-- ## Arctern GeoSeries 与 GeoPandas GeoSeries 的性能对比

在大数据量的情况下，GeoPandas 的执行速度不够理想，Arctern 实现了对 GeoPandas 部分函数的加速，平均加速比可达到6至七倍，个别函数甚至可以达到十倍之多。

以下给出 is_simple 函数的性能对比测试示例。

### 1. 测试　Arctern GeoSeries 与 GeoPandas GeoSeries 的执行时间

测试在 1000000 行数据量下，Arctern GeoSeries 与 GeoPandas GeoSeries 的表现。

```python
>>> import arctern
>>> import time
>>>
>>> p1 = "POLYGON ((0 0,4 0,4 4,0 4,0 0))"
>>> arctern_geoseries = arctern.GeoSeries([p1] * 1000000)
>>> arctern_start_time = time.time()
>>> arctern_geoseries.is_simple
0         True
1         True
2         True
3         True
4         True
          ...
999995    True
999996    True
999997    True
999998    True
999999    True
Length: 1000000, dtype: bool
>>> arctern_end_time = time.time()
>>>
>>> geopandas_geoseries = arctern_geoseries.to_geopandas()
>>> geopandas_start_time = time.time()
>>> geopandas_geoseries.is_simple
0         True
1         True
2         True
3         True
4         True
          ...
999995    True
999996    True
999997    True
999998    True
999999    True
Length: 1000000, dtype: bool
>>> geopandas_end_time = time.time()
>>> arctern_time = arctern_end_time - arctern_start_time
>>> arctern_time
2.7381417751312256
>>> geopandas_time = geopandas_end_time - geopandas_start_time
>>> geopandas_time
36.56021523475647
```

在运行上面的代码后， Arctern GeoSeries 执行时间为 2.7381417751312256 秒, GeoPandas GeoSeries 执行时间为 36.56021523475647 秒。

### 2. Arctern GeoSeries 与 GeoPandas GeoSeries 性能对比

根据上面的测试结果计算Arctern GeoSeries 对于 GeoPandas GeoSeries 的加速比。

```python
>>> speedup = geopandas_time / arctern_time
>>> speedup
13.352199497779592
```

根据结果可知，Arctern GeoSeries 执行速度是 GeoPandas GeoSeries 的13.35倍。
下面是在 1000000 数据量下，Arctern GeoSeries 与 GeoPandas GeoSeries 的性能对比柱状图。

<img src="GeoSeries10_6.png">

根据柱状图可以看出，在性能上，Arctern 对于 GeoPandas 是很有优势的。 -->