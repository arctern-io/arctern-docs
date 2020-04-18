# Geometry 数据格式

Arctern 在数据导入导出时支持 [Well Know Text(WKT)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry)  和 [Well Know Binary (WKB)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary) 两种形式的空间几何体数据。


但是 Arctern API 仅支持 WKB 形式的空间几何体数据作为传入和返回参数。如下例所示，如果数据源中使用 WKT 形式的数据，在数据导入后需要调用 `ST_GeomFromText` 函数将数据转换为 WKB 形式；相应的，在数据导出时，也需要调用 `ST_GeomFromText` 函数将数据转换回 WKT形式。数据形式的转换将带来额外的数据开销。因此，建议对空间几何体数据没有可读性要求的用户将数据存储为 WKB 形式。

```Python
>>> import pandas as pd
>>> import arctern
>>> df = pd.read_csv("/path/to/geos.csv",sep='|')
>>> data = pd.Series(df['geos'].values)
>>> rst = arctern.ST_IsSimple(arctern.ST_GeomFromText(data))
>>> print(rst)
0     True
1     True
2    False
3     True
dtype: bool
>>> df.to_csv("/path/to/new_geos.csv")
```
