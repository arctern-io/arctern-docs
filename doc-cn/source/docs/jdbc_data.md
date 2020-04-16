# JDBC连接

以下例子展示如何利用JDBC来从postgis中导入数据，详细信息请查看[Spark官方文档](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html)。

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

    # Note: JDBC loading and saving can be achieved via either the load/save or jdbc methods
    # Loading data from a JDBC source
    spark.read.format("jdbc") \
              .option("url", "jdbc:postgresql://172.17.0.2:5432/test?user=arcterner&password=arcterner") \
              .option("query", "select st_astext(geos) as geos from simple") \
              .load() \
              .createOrReplaceTempView("simple")
    spark.sql("select ST_IsSimple(ST_GeomFromText(geos)) from simple").show(20,0)

    # Saving data to a JDBC source
    spark.write.format("jdbc") \
               .option("url", "jdbc:postgresql://172.17.0.2:5432/test?user=arcterner&password=arcterner") \
               .option("query", "select st_astext(geos) as geos from simple") \
               .load() \
               .save()

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