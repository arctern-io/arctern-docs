# 数据导入导出

Arctern为用户提供了python以及pyspark两套接口，在使用python接口时，可以利用pandas对数据进行导入，使用pyspark接口时，可以通过spark导入数据。

## geos.csv文件内容
```
geos
POINT (30 10)
POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))
POLYGON ((1 2, 3 4, 5 6, 1 2))
POLYGON ((1 1, 3 1, 3 3, 1 3, 1 1))
```

## Spark导入数据

详细信息请查看[Spark官方文档](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html)

### 数据文件导入

Spark支持多种数据格式文件导入，以下是针对csv、parquet、json、orc等数据格式文件的导入导出例子。

```python
#CSV文件导入，导出为PARQUET格式
>>> from pyspark.sql import SparkSession
>>> from arctern_pyspark import register_funcs
>>> spark_session = SparkSession.builder.appName("Python Arrow-in-Spark example").getOrCreate()
>>> spark_session.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
>>> register_funcs(spark_session)
>>> df = spark_session.read.format('csv').options(header='true',sep='|').load("/path/to/geos.csv")
>>> df.show(100,0)
+---------------------------------------------+
|geos                                         |
+---------------------------------------------+
|POINT (30 10)                                |
|POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))|
|POLYGON ((1 2, 3 4, 5 6, 1 2))               |
|POLYGON ((1 1, 3 1, 3 3, 1 3, 1 1))          |
+---------------------------------------------+
>>> df.createOrReplaceTempView("simple")
>>> spark_session.sql("select ST_IsSimple(ST_GeomFromText(geos)) from simple").show(100,0)
+----------------------------------+                                            
|ST_IsSimple(ST_GeomFromText(geos))|
+----------------------------------+
|true                              |
|true                              |
|false                             |
|true                              |
+----------------------------------+
>>> df.select("geos").write.save("/path/to/geos.parquet", format="parquet")


#PARQUET文件导入，导出为JSON格式
>>> df = spark_session.read.format('parquet').options(header='true',sep='|').load("/path/to/geos.parquet")
>>> df.show(100,0)
+---------------------------------------------+
|geos                                         |
+---------------------------------------------+
|POINT (30 10)                                |
|POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))|
|POLYGON ((1 2, 3 4, 5 6, 1 2))               |
|POLYGON ((1 1, 3 1, 3 3, 1 3, 1 1))          |
+---------------------------------------------+
>>> df.createOrReplaceTempView("simple")
>>> spark_session.sql("select ST_IsSimple(ST_GeomFromText(geos)) from simple").show(100,0)
+----------------------------------+                                            
|ST_IsSimple(ST_GeomFromText(geos))|
+----------------------------------+
|true                              |
|true                              |
|false                             |
|true                              |
+----------------------------------+
>>> df.select("geos").write.save("/path/to/geos.json", format="json")


# JSON文件导入，导出为ORC格式
>>> df = spark_session.read.format('json').options(header='true',sep='|').load("/path/to/geos.json")
>>> df.show(100,0)
+---------------------------------------------+
|geos                                         |
+---------------------------------------------+
|POINT (30 10)                                |
|POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))|
|POLYGON ((1 2, 3 4, 5 6, 1 2))               |
|POLYGON ((1 1, 3 1, 3 3, 1 3, 1 1))          |
+---------------------------------------------+
>>> df.createOrReplaceTempView("simple")
>>> spark_session.sql("select ST_IsSimple(ST_GeomFromText(geos)) from simple").show(100,0)
+----------------------------------+                                            
|ST_IsSimple(ST_GeomFromText(geos))|
+----------------------------------+
|true                              |
|true                              |
|false                             |
|true                              |
+----------------------------------+
>>> df.write.save("/path/to/geos.orc", format="orc")


# ORC文件导入
>>> df = spark_session.read.format('orc').options(header='true',sep='|').load("/path/to/geos.orc")
>>> df.show(100,0)
+---------------------------------------------+
|geos                                         |
+---------------------------------------------+
|POINT (30 10)                                |
|POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))|
|POLYGON ((1 2, 3 4, 5 6, 1 2))               |
|POLYGON ((1 1, 3 1, 3 3, 1 3, 1 1))          |
+---------------------------------------------+
>>> df.createOrReplaceTempView("simple")
>>> spark_session.sql("select ST_IsSimple(ST_GeomFromText(geos)) from simple").show(100,0)
+----------------------------------+                                            
|ST_IsSimple(ST_GeomFromText(geos))|
+----------------------------------+
|true                              |
|true                              |
|false                             |
|true                              |
+----------------------------------+
```

### JDBC数据导入

以下例子展示如何利用JDBC来从postgis中导入数据。

 配置 | 值
:-----------:|:----------:
IP address |  172.17.0.2
port | 5432
database name | test
user name | acterner
password | acterner

使用如下命令测试能否连接postgis

psql test -h 172.17.0.2  -p 5432 -U arcterner

arctern使用jdbc加载postgis，jdbc_postgis.py示例代码如下:
```python
from pyspark.sql import SparkSession
from arctern_pyspark import register_funcs
if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("polygon test") \
        .getOrCreate()
    spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
    register_funcs(spark)
    spark.read.format("jdbc") \
              .option("url", "jdbc:postgresql://172.17.0.2:5432/test?user=arcterner&password=arcterner") \
              .option("query", "select st_astext(geos) as geos from simple") \
              .load() \
              .createOrReplaceTempView("simple")
    spark.sql("select ST_IsSimple(ST_GeomFromText(geos)) from simple").show(20,0)
    spark.stop()
```
结果如下：
```
+----------------------------------+                                            
|ST_IsSimple(ST_GeomFromText(geos))|
+----------------------------------+
|true                              |
|true                              |
|false                             |
|true                              |
+----------------------------------+
```

从[postgres官网](https://jdbc.postgresql.org/download.html)下载最新的JDBC驱动，这里下载的驱动为postgresql-42.2.11.jar，在提交spark任务时，需要指定jdbc驱动

./bin/spark-submit  --driver-class-path ~/postgresql-42.2.11.jar --jars ~/postgresql-42.2.11.jar ~/query_postgis.py 


## pandas数据导入

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