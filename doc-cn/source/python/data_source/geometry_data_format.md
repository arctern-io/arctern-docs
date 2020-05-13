# Geometry 数据格式

Arctern 在数据导入导出时支持 [Well Know Text (WKT)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) 和 [Well Know Binary (WKB)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary) 两种形式的几何体数据。相对 WKB 而言，WKT 形式的数据更方便人工阅读，但是计算机对其处理的效率相对较低并且占用的存储空间也更大。

目前 Arctern API 仅支持 WKB 形式的几何体数据作为传入和返回参数。如下例所示，如果数据源中使用 WKT 形式的数据，在数据导入后需要调用 `ST_GeomFromText` 函数将数据转换为 WKB 形式；相应的，在数据导出时，也需要调用 `ST_GeomFromText` 函数将数据转换回 WKT 形式。数据形式的转换将带来额外的数据开销。因此，建议对几何体数据没有可读性要求的用户将数据存储为 WKB 形式。

## 样例

WKT 形式数据的导入和导出：

```Python
'''
CSV 文件内容：
geos
POINT (30 10)
POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))
POLYGON ((1 2, 3 4, 5 6, 1 2))
POLYGON ((1 1, 3 1, 3 3, 1 3, 1 1))
'''
>>> import pandas as pd
>>> import arctern
>>> df = pd.read_csv("/path/to/geos.csv",sep='|')
>>> data = pd.Series(df['geos'].values,name='geos')

# 在对数据进行处理之前使用 ST_GeomFromText 将数据转换为 WKB 形式
>>> data = arctern.ST_GeomFromText(data)
>>> valid_data = arctern.ST_MakeValid(data)

# 在将数据导出之前使用 ST_AsText 将数据转换为 WKT 形式
>>> valid_data = arctern.ST_AsText(valid_data)
>>> valid_data = valid_data.rename('geos')
>>> valid_data.to_csv("/path/to/valid_geos.csv",index=None,sep='|')
```

WKB 形式数据的导入和导出：
```Python
'''
CSV 文件内容：
geos
b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00>@\x00\x00\x00\x00\x00\x00$@'
b'\x01\x03\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00>@\x00\x00\x00\x00\x00\x00$@\x00\x00\x00\x00\x00\x00D@\x00\x00\x00\x00\x00\x00D@\x00\x00\x00\x00\x00\x004@\x00\x00\x00\x00\x00\x00D@\x00\x00\x00\x00\x00\x00$@\x00\x00\x00\x00\x00\x004@\x00\x00\x00\x00\x00\x00>@\x00\x00\x00\x00\x00\x00$@'
b'\x01\x03\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@\x00\x00\x00\x00\x00\x00\x14@\x00\x00\x00\x00\x00\x00\x18@\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@'
b'\x01\x03\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?'
'''
>>> import pandas as pd
>>> import arctern
>>> df = pd.read_csv("/path/to/geos.csv",sep='|')
>>> data = pd.Series(df['geos'].values)

# 在对数据处理之前无需对数据进行转换
>>> valid_data = arctern.ST_MakeValid(data)
>>> valid_data = valid_data.rename('geos')
>>> valid_data.to_csv("/path/to/valid_geos.csv",index=None,sep='|')
```