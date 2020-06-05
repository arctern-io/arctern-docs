# plot_choropleth_map

**plot_choropleth_map(ax, region_boundaries, weights, bounding_box,
                      color_gradient, color_bound=None, opacity=1.0,
                      coordinate_system='EPSG:3857',
                      \*\*extra_contextily_params)**

&#x2002; &#x2003; 直接在matplotlib中绘制点图。

&#x2002; &#x2003; 参数

&#x2002; &#x2003; &#x2002; &#x2003; * ax(matplotlib.axes.Axes) -- 用来绘制几何体的坐标轴。

&#x2002; &#x2003; &#x2002; &#x2003; * region_boundaries(Series(dtype: object)) -- 所需绘制的多边形轮廓，格式为WKB。

&#x2002; &#x2003; &#x2002; &#x2003; * weights(Series(dtype: float64|int64)) -- 轮廓的颜色权重。

&#x2002; &#x2003; &#x2002; &#x2003; * bounding_box(list) -- 图片对应的地理坐标区域，以 [x_min, y_min, x_max, y_max] 的形式表示一个矩形区域。图片左下角的像素坐标 (0, 0) 对应地理坐标 (x_min, y_min) ，图片右上角的像素坐标 (width, height) 对应地理坐标 (x_max, y_max)。

&#x2002; &#x2003; &#x2002; &#x2003; * color_gradient(list) -- 轮廓的颜色渐变范围，表示形式为 ["hex_color"] 或 ["hex_color1", "hex_color2"]。当形式为["hex_color"] 时所有轮廓的颜色相同。当形式为["hex_color1", "hex_color2"] 时轮廓的颜色由输入数据中一列的值（权重）决定，且颜色在 "hex_color1" ~ "hex_color2" 之间变化。

&#x2002; &#x2003; &#x2002; &#x2003; * color_bound(list) -- 可选参数，用于描述权重与颜色的对应关系，仅当color_gradient中包含两个颜色值时需要设置，表示形式为 [color_min, color_max]。权重值小于等于 color_min 时轮廓的颜色为"hex_color1"， 权重值大于等于 color_max 时轮廓的颜色为"hex_color2"。

&#x2002; &#x2003; &#x2002; &#x2003; * opacity(float) -- 可选参数，表示轮廓的不透明度，范围为 0.0 ~ 1.0，默认值为 1.0。

&#x2002; &#x2003; &#x2002; &#x2003; * coordinate_system(str) -- 可选参数，表示输入数据所属的地理坐标系统，默认值为"EPSG:3857"，当前支持的地理坐标系统请参照 <https://spatialreference.org/>。

&#x2002; &#x2003; &#x2002; &#x2003; * aggregation_type(str) -- 可选参数，表示输入数据到轮廓权重的聚合方式，默认值为"sum"。

&#x2002; &#x2003; &#x2002; &#x2003; * extra_contextily_params(dict) -- 剩余参数, 传递给 contextily.add_basemap, 可用于[更换地图背景, 或修改地图提供商](https://contextily.readthedocs.io/en/latest/providers_deepdive.html).




### 示例:

  ```python
      >>> import pandas as pd
      >>> import numpy as np
      >>> import arctern
      >>> from arctern.util import save_png
      >>> from arctern.util.vega import vega_choroplethmap
      >>> 
      >>> # 读取 csv 文件并创建绘图数据
      >>> # test_data.csv下载链接: https://github.com/zilliztech/arctern-resources/raw/benchmarks/benchmarks/dataset/layer_rendering_test_data/test_data.csv
      >>> df = pd.read_csv("/path/to/test_data.csv", dtype={'longitude':np.float64, 'latitude':np.float64, 'color_weights':np.float64, 'size_weights':np.float64, 'region_boundaries':np.object})
      >>> input1 = df[pd.notna(df['region_boundaries'])].groupby(['region_boundaries']).mean().reset_index()
      >>> polygon = arctern.ST_GeomFromText(input1['region_boundaries'])
      >>> 
      >>> # 绘制轮廓图，轮廓的填充颜色根据 input1['color_weights'] 在 "#115f9a" ~ "#d0f400" 之间变化
      >>> fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
      >>> plot_choropleth_map(ax, polygon, input1['color_weights'], bounding_box=[-74.01124953254566,40.73413446570038,-73.96238859103838,40.766161712662296], color_gradient=["#115f9a","#d0f400"], color_bound=[5,18], opacity=1.0, coordinate_system='EPSG:4326', aggregation_type="mean")
      >>> plt.show()
   ```