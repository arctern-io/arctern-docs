# plot.fishnetmap

绘制渔网图。

**plot.fishnetmap(ax, points, weights, bounding_box,
                  color_gradient=["#0000FF", "#FF0000"],
                  cell_size=4, cell_spacing=1, opacity=1.0,
                  coordinate_system='epsg:3857',
                  aggregation_type='sum',
                  \*\*extra_contextily_params)**
 

参数

- ax(matplotlib.axes.Axes) -- 用来绘制几何体的坐标轴。

- points(GeoSeries(dtype: GeoDtype)) -- 数据点的位置，格式为 WKB。

- weights(Series(dtype: float64|int64)) -- 数据点的颜色权重。

- bounding_box(list) -- 图片对应的地理坐标区域，以 [x_min, y_min, x_max, y_max] 的形式表示一个矩形区域。图片左下角的像素坐标 (0, 0) 对应地理坐标 (x_min, y_min) ，图片右上角的像素坐标 (width, height) 对应地理坐标 (x_max, y_max)。

- color_gradient(list) -- 渔网网格的颜色渐变范围，表示形式为 ["hex_color"] 或 ["hex_color1", "hex_color2"]。当形式为["hex_color"] 时所有网格的颜色相同。当形式为["hex_color1", "hex_color2"] 时网格的颜色由输入数据中一列的值（权重）决定，且颜色在 "hex_color1" ~ "hex_color2" 之间变化。目前仅支持默认值 ["#0000FF", "#FF0000"]。

- cell_size(int) -- 可选参数，表示渔网网格的边长，单位为像素，默认值为 4。

- cell_spacing(int) -- 可选参数，表示渔网网格之间的间隔，单位为像素，默认值为 1。

- opacity(float) -- 可选参数，表示渔网网格的不透明度，范围为 0.0 ~ 1.0，默认值为 1.0。

- coordinate_system(str) -- 可选参数，表示输入数据所属的地理坐标系统，默认值为"EPSG:3857"，当前支持的地理坐标系统请参照 <https://spatialreference.org/>。

- aggregation_type(str) -- 可选参数，表示输入数据到渔网网格权重的聚合方式，默认值为"sum"。

## 示例:

```python
import pandas as pd
import numpy as np
import arctern
import matplotlib.pyplot as plt
# 读取 csv 文件并创建绘图数据
# test_data.csv下载链接: https://raw.githubusercontent.com/arctern-io/arctern-resources/benchmarks/benchmarks/dataset/layer_rendering_test_data/test_data.csv
df = pd.read_csv("/path/to/test_data.csv", dtype={'longitude':np.float64, 'latitude':np.float64, 'color_weights':np.float64, 'size_weights':np.float64, 'region_boundaries':np.object})
points = arctern.GeoSeries.point(df['longitude'], df['latitude'])
# 根据 df['color_weights'] 绘制渔网图
fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
arctern.plot.fishnetmap(ax, points=points,  weights=df['color_weights'], bounding_box=[-74.01424568752932, 40.72759334104623, -73.96056823889673, 40.76721122683304], cell_size=8, cell_spacing=2, opacity=1.0, coordinate_system="EPSG:4326")
plt.show()
```
