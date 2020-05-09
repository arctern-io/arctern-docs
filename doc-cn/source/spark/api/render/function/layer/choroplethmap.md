# choroplehtmap

绘制一个轮廓图。需要先后调用 vega_choroplethmap 和 choroplemap 两个接口。首先使用 vega_choroplethmap 构建描述轮廓图渲染样式的 VegaChoroplethMap 对象，然后使用 choroplemap 渲染图像。

## vega_choroplethmap 

**arctern.util.vega.vega_choroplethmap(width,height,bounding_box,color_gradient,
color_bound,opacity,coordinate_system,aggregation_type)**

&#x2002; &#x2003; 根据给定的配置参数，构建描述轮廓图渲染样式的 VegaChoroplethMap 对象。

&#x2002; &#x2003; 参数

&#x2002; &#x2003; &#x2002; &#x2003; * width(int) -- 图片宽度，单位为像素个数。

&#x2002; &#x2003; &#x2002; &#x2003; * height(int) -- 图片高度，单位为像素个数。

&#x2002; &#x2003; &#x2002; &#x2003; * bounding_box(list) -- 图片对应的地理坐标区域，以 [x_min, y_min, x_max, y_max] 的形式表示一个矩形区域。图片左下角的像素坐标 (0, 0) 对应地理坐标 (x_min, y_min) ，图片右上角的像素坐标 (width, height) 对应地理坐标 (x_max, y_max)。

&#x2002; &#x2003; &#x2002; &#x2003; * color_gradient(list) -- 轮廓的颜色渐变范围，表示形式为 ["hex_color"] 或 ["hex_color1", "hex_color2"]。当形式为["hex_color"] 时所有轮廓的颜色相同。当形式为["hex_color1", "hex_color2"] 时轮廓的颜色由输入数据中一列的值（权重）决定，且颜色在 "hex_color1" ~ "hex_color2" 之间变化。

&#x2002; &#x2003; &#x2002; &#x2003; * color_bound(list) -- 可选参数，用于描述权重与颜色的对应关系，仅当color_gradient中包含两个颜色值时需要设置，表示形式为 [color_min, color_max]。权重值小于等于 color_min 时点的颜色为"hex_color1"， 权重值大于等于 color_max 时点的颜色为"hex_color2"。

&#x2002; &#x2003; &#x2002; &#x2003; * opacity(float) -- 可选参数，表示轮廓的不透明度，范围为 0.0 ~ 1.0，默认值为 1.0。

&#x2002; &#x2003; &#x2002; &#x2003; * coordinate_system(str) -- 可选参数，表示输入数据所属的地理坐标系统，默认值为"EPSG:3857"，当前支持的地理坐标系统请参照 <https://spatialreference.org/>。

&#x2002; &#x2003; &#x2002; &#x2003; * aggregation_type(str) -- 可选参数，表示输入数据到轮廓权重的聚合方式，默认值为"sum"。


&#x2002; &#x2003; 返回值类型
   
&#x2002; &#x2003; &#x2002; &#x2003; arctern.util.vega.choroplethmap.vega_choroplethmap.VegaChoroplethMap


&#x2002; &#x2003; 返回

&#x2002; &#x2003; &#x2002; &#x2003; 用于描述渲染样式的 VegaChoroplethMap 对象。



## choroplemap

**arctern_pyspark.choroplemap(vega, region_boundaries, weights)**

&#x2002; &#x2003; 绘制轮廓图，权重用于决定轮廓的填充颜色。

&#x2002; &#x2003; 参数

&#x2002; &#x2003; &#x2002; &#x2003; * vega(VegaChoroplethMap) -- VegaChoroplethMap 对象。

&#x2002; &#x2003; &#x2002; &#x2003; * region_boundaries(WKB) -- 所需绘制的多边形轮廓，格式为WKB。

&#x2002; &#x2003; &#x2002; &#x2003; * weights(int|float) -- 轮廓的颜色权重。


&#x2002; &#x2003; 返回值类型
   
&#x2002; &#x2003; &#x2002; &#x2003; bytes


&#x2002; &#x2003; 返回

&#x2002; &#x2003; &#x2002; &#x2003; base64编码的png图片。


### 示例:

  ```python
      >>> from arctern.util import save_png
      >>> from arctern.util.vega import vega_choroplethmap
      >>> from arctern_pyspark import register_funcs
      >>> from arctern_pyspark import choroplethmap
      >>> from pyspark.sql import SparkSession
      >>> 
      >>> spark = SparkSession.builder.appName("Python Arrow-in-Spark example").getOrCreate()
      >>> spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
      >>> 
      >>> # test_data.csv下载链接: https://github.com/zilliztech/arctern-resources/raw/benchmarks/benchmarks/dataset/layer_rendering_test_data/test_data.csv
      >>> table_df = spark.read.format("csv").option("header", True).option("delimiter", ",").schema(
      "longitude double, latitude double, color_weights double, size_weights double, region_boundaries string").load(
      "file:///tmp/test_data.csv").cache()
      >>> table_df.createOrReplaceTempView("test_table")
      >>> 
      >>> register_funcs(spark)
      >>> # df 是包含 2 列数据的 pyspark.Dataframe， 第一列为 WKB 类型的polygons，第二列为轮廓填充颜色的权重
      >>> # 绘制轮廓图，轮廓的填充颜色根据 color_weights 在 "#115f9a" ~ "#d0f400" 之间变化
      >>> df = spark.sql("SELECT ST_GeomFromText(region_boundaries) AS wkb, color_weights AS color FROM test_table WHERE ((region_boundaries !=''))")
      >>> vega = vega_choroplethmap(1922, 1663, bounding_box=[-74.01124953254566,40.73413446570038,-73.96238859103838,40.766161712662296], color_gradient=["#115f9a","#d0f400"], color_bound=[5,18], opacity=1.0, coordinate_system='EPSG:4326', aggregation_type="mean") 
      >>> res = choroplethmap(vega, df)
      >>> save_png(res, '/tmp/choroplethmap.png')
      >>> 
      >>> spark.sql("show tables").show()
      >>> spark.catalog.dropGlobalTempView("test_table")
   ```

渲染结果如下：
![](../../../../../../../img/render/spark/choroplethmap.png)