# 文件的导入与导出

Arctern 借助 Pandas 的文件读写功能完成数据的导入和导出。Pandas 支持多种数据文件格式，如CSV、HTML、JSON、ORC等，详细内容可参考[官方文档](https://pandas.pydata.org/pandas-docs/stable/reference/io.html),下面是针对 CSV 和JSON 格式数据的导入导出示例：

```python
#导入CSV文件，导出为JSON文件
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
>>> rst = arctern.ST_IsSimple(arctern.ST_GeomFromText(data))
>>> print(rst)
0     True
1     True
2    False
3     True
dtype: bool
>>> df.to_json("/path/to/geos.json")

#导入JSON文件，导出为CSV文件
>>> df = pd.read_json("/path/to/geos.json")
>>> data = pd.Series(df['geos'].values,name='geos')
>>> rst = arctern.ST_IsSimple(arctern.ST_GeomFromText(data))
>>> print(rst)
0     True
1     True
2    False
3     True
dtype: bool
>>> df.to_csv("/path/to/geos.csv")
```