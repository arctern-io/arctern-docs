# Import and Export of Files

Arctern RESTful service uses Spark's file reading and writing functions to realize the import and export of data. Spark supports the import of multiple types of data format files. The following are examples of importing and exporting data format files such as CSV, PARQUET, JSON, ORC. For more supported file formats, see [Spark's Official Docs](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html).

```python
>>> # Import CSV files and export PARQUET files
'''
CSV file content:
geos
POINT (30 10)
POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))
POLYGON ((1 2, 3 4, 5 6, 1 2))
POLYGON ((1 1, 3 1, 3 3, 1 3, 1 1))
'''
>>> from pyspark.sql import SparkSession
>>> from arctern_pyspark import register_funcs
>>> 
>>> # Create SparkSession and configure it
>>> spark_session = SparkSession.builder.appName("Python Arrow-in-Spark example").getOrCreate()
>>> spark_session.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
>>> 
>>> # 注册 Arctern-Spark 提供的函数
>>> register_funcs(spark_session)
>>> 
>>> # Data import
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
>>> 
>>> # 为导入数据创建数据表 ‘simple’ 并对其进行处理
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
>>> 
>>> # 数据导出
>>> df.select("geos").write.save("/path/to/geos.parquet", format="parquet")
>>> 
>>> # 导入 PARQUET 文件，导出 JSON 文件
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
>>>
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
>>> 
>>> df.select("geos").write.save("/path/to/geos.json", format="json")
>>> 
>>> # 导入 JSON 文件，导出 ORC 文件
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
>>> 
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
>>> 
>>> df.write.save("/path/to/geos.orc", format="orc")
>>> 
>>> # 导入 ORC 文件，导出 CSV 文件
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
>>> 
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
>>> 
>>> df.select("geos").write.save("/path/to/geos.csv", format="csv")
```