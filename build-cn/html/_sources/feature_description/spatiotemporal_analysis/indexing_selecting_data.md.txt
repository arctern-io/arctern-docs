# 索引和选择数据
本文档介绍 Arctern GeoSeries 如何索引和选择数据。

## 索引和选择数据的方法
Arctern GeoSeries 继承了 pandas Series 索引和选择数据的方法，包括基于标签的索引 [`loc`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html) 和基于整数下标位置的索引 [`iloc`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html)。有关索引和选择数据的详细信息请见 [pandas 文档](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html)。

## 生成测试数据

创建一个 arctern.GeoSeries 对象 `geos`，其中包括三个点（POINT）和一个多边形（POLYGON），并为它们建立索引。另外，以 `geos` 作为输入，创建一个 pandas.DataFrame 对象。

> **注意：** 索引中的 a、b、c、d 对应的行数分别是 0、1、2、3。

```python
>>> from arctern import GeoSeries
>>> import pandas as pd
>>> geos = GeoSeries(["POINT (0 1)","POINT (2 3)","POLYGON ((0 0,0 1,1 1,0 0))", "POINT (0 0)"],index=['a','b','c','d'])
>>> df = pd.DataFrame(geos)
```

## 测试

### 测试 loc 方法

访问 `geos` 的所有数据：
```python
>>> geos.loc[:]    
a                    POINT (0 1)
b                    POINT (2 3)
c    POLYGON ((0 0,0 1,1 1,0 0))
d                    POINT (0 0)
dtype: GeoDtype
```

选取 `geos` 的 `a` 标签所在行到 `c` 标签所在行的数据：
```python
>>> geos.loc['a':'c']
a                    POINT (0 1)
b                    POINT (2 3)
c    POLYGON ((0 0,0 1,1 1,0 0))
dtype: GeoDtype
```

选取 `geos` 的首行到 `c` 标签所在行的数据：

```python
>>> geos.loc[:'c']
a                    POINT (0 1)
b                    POINT (2 3)
c    POLYGON ((0 0,0 1,1 1,0 0))
dtype: GeoDtype
```

### 测试 iloc 方法

选取 `geos` 的 第 1 行到第 3 行数据（不包含第 3 行数据）：
```python
>>> geos.iloc[1:3]
b                    POINT (2 3)
c    POLYGON ((0 0,0 1,1 1,0 0))
dtype: GeoDtype
```

选取 `df` 的 第 1 行到第 3 行数据（不包含第 3 行数据）：
```python
>>> df.iloc[1:3]
                             0
b                  POINT (2 3)
c  POLYGON ((0 0,0 1,1 1,0 0))
```
