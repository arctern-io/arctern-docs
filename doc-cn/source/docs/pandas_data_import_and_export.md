# 文件的导入与导出

pandas支持多种数据文件格式导入，例如csv、html、json、orc等数据格式，详细内容可参考[官方文档](https://pandas.pydata.org/pandas-docs/stable/reference/io.html),下面是针对几种数据文件的导入导出例子：

```python
#导入CSV文件，导出为JSON格式
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
>>> df.to_json("/path/to/geos.json")


#导入JSON文件
>>> df = pd.read_json("/path/to/geos.json")
>>> data = pd.Series(df['geos'].values)
>>> rst = arctern.ST_IsSimple(arctern.ST_GeomFromText(data))
>>> print(rst)
0     True
1     True
2    False
3     True
dtype: bool
```