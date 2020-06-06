# plot_geometry
**plot_geometry(ax, geoms, \*\*style_kwds)**
在 matplotlib 中绘制几何图形。

参数

- ax(matplotlib.axes.Axes) -- 用来绘制几何体的坐标轴。

- geoms(Series(dtype: object)) -- 所需绘制的几何体，格式为 WKB。

- style_kwds : 绘图风格参数设置，包括 `linewidth`, `linestyle`, `edgecolor`,`facecolor`, `color`, `marker`, `markersize`,`alpha`

- linewidth: list(float) -- 线宽(线/多边形)，默认值是 1.0。

- linestyle: list(string) -- 线型(线/多边形)，默认值是 '-'

- edgecolor: list(string) -- 边缘颜色(多边形)，默认值是黑色。

- facecolor: list(string) -- 填充颜色(多边形)，默认值是 'C0'。

- color: list(string) -- 图形颜色(点/线)，默认值是 'C0'。

- marker: string -- 点型(点)，默认值是 'o'。

- markersize: double -- 点大小(点)，默认值是 6.0。

- alpha: double -- 透明度，默认值是 1.0。

## 示例:

```python
import pandas
import matplotlib.pyplot as plt
import arctern
raw_data = []
raw_data.append('point(0 0)')
raw_data.append('linestring(0 10, 5 5, 10 0)')
raw_data.append('polygon((2 2,2 3,3 3,3 2,2 2))')
raw_data.append("GEOMETRYCOLLECTION("
                    "polygon((1 1,1 2,2 2,2 1,1 1)),"
                    "linestring(0 1, 5 6, 10 11),"
                    "POINT(4 7))")
arr_wkt = pandas.Series(raw_data)
arr_wkb = arctern.ST_CurveToLine(arctern.ST_GeomFromText(arr_wkt))
df = pandas.DataFrame({'wkb':arr_wkb})
fig, ax = plt.subplots()
arctern.plot.plot_geometry(ax, df,
                          color=['orange', 'green', 'blue', 'red'],
                          marker='^',
                          markersize=100,
                          linewidth=[None, 7, 8, 5],
                          linestyle=[None, 'dashed', 'dashdot', None],
                          edgecolor=[None, None, 'red', None],
                          facecolor=[None, None, 'black', None])
ax.grid()
fig.savefig('/tmp/plot_test.png')
plt.show()
```
