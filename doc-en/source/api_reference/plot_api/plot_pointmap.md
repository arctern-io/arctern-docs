# plot_pointmap
**plot_pointmap(ax, points, bounding_box, 
                point_size=3, point_color='#115f9a', opacity=1.0,
                coordinate_system='EPSG:3857',
                \*\*extra_contextily_params)**

&#x2002; &#x2003; 直接在matplotlib中绘制点图。

&#x2002; &#x2003; 参数

&#x2002; &#x2003; &#x2002; &#x2003; * ax(matplotlib.axes.Axes) -- 用来绘制几何体的坐标轴。

&#x2002; &#x2003; &#x2002; &#x2003; * points(Series(dtype: object)) -- 所需绘制的点，格式为 WKB。

&#x2002; &#x2003; &#x2002; &#x2003; * bounding_box(list) -- 图片对应的地理坐标区域，以 [x_min, y_min, x_max, y_max] 的形式表示一个矩形区域。图片左下角的像素坐标 (0, 0) 对应地理坐标 (x_min, y_min) ，图片右上角的像素坐标 (width, height) 对应地理坐标 (x_max, y_max)。

&#x2002; &#x2003; &#x2002; &#x2003; * point_size(int) -- 可选参数，表示点的直径，默认值为 3。

&#x2002; &#x2003; &#x2002; &#x2003; * point_color(str) -- 可选参数，表示点的颜色，使用十六进制的颜色编码(Hex Color Code)表示，默认值为"#115f9a"。

&#x2002; &#x2003; &#x2002; &#x2003; * opacity(float) -- 可选参数，表示点的不透明度，范围为 0.0 ~ 1.0，默认值为 1.0。

&#x2002; &#x2003; &#x2002; &#x2003; * coordinate_system(str) -- 可选参数，表示输入数据所属的地理坐标系统，默认值为"EPSG:3857"，当前支持的地理坐标系统请参照 <https://spatialreference.org/>。

&#x2002; &#x2003; &#x2002; &#x2003; * extra_contextily_params(dict) -- 剩余参数, 传递给 contextily.add_basemap, 可用于[更换地图背景, 或修改地图提供商](https://contextily.readthedocs.io/en/latest/providers_deepdive.html).

### 示例:

  ```python
      >>> import pandas as pd
      >>> import numpy as np
      >>> import arctern
      >>> from arctern import plot_pointmap
      >>> import matplotlib as plt
      >>> from arctern.util import save_png
      >>> from arctern.util.vega import vega_pointmap
      >>> 
      >>> # 读取 csv 文件并创建绘图数据
      >>> # test_data.csv下载链接: https://github.com/zilliztech/arctern-resources/raw/benchmarks/benchmarks/dataset/layer_rendering_test_data/test_data.csv
      >>> df = pd.read_csv("/path/to/test_data.csv", dtype={'longitude':np.float64, 'latitude':np.float64, 'color_weights':np.float64, 'size_weights':np.float64, 'region_boundaries':np.object})
      >>> region = arctern.ST_GeomFromText(pd.Series(['POLYGON ((-74.01398981737215 40.71353244267465, -74.01398981737215 40.74480271529791, -73.96979949831308 40.74480271529791, -73.96979949831308 40.71353244267465, -74.01398981737215 40.71353244267465))']))
      >>> d = pd.DataFrame(region).T
      >>> region = region.append([d]*(df.shape[0] - 1))
      >>> in_region = arctern.ST_Within(arctern.ST_Point(df['longitude'], df['latitude']), region[0])
      >>> df['in_region']=in_region
      >>> input1 = df[df.in_region == True].head(10000)
      >>> 
      >>> points = arctern.ST_Point(input1['longitude'], input1['latitude'])
      >>> 
      >>> # 绘制点大小为10，点颜色为#115f9a，点不透明度为0.5的点图
      >>> fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
      >>> plot_pointmap(ax, points, [-74.01398981737215,40.71353244267465,-73.96979949831308,40.74480271529791], point_size=10, point_color='red')
      >>> plt.show()
   ```
