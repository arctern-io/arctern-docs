# 使用 Arctern 分析空间数据

完成 [Arctern 的安装部署](./installation.md) 之后，本文档引导你使用 Arctern 分析帝国大厦附近的道路信息。

### 安装 Jupyter 和 Kepler.Gl

在后续步骤中，你需要使用 Jupyter Notebook 运行代码，以及使用 Kepler.Gl 进行空间数据可视化。请按照以下步骤安装 Jupyter 和 Kepler.Gl：

进入 Conda 环境：

```bash
$ conda activate arctern_env
```

安装 Jupyter 和 Kepler.Gl：

```bash
$ conda install -c conda-forge jupyterlab
$ pip install keplergl
```

## 运行 Jupyter Notebook

在 Conda 环境中运行 Jupyter Notebook，它将在你的默认浏览器中打开一个页面。

```bash
$ jupyter-notebook
```

点击页面右上角的 **New &gt; Python3** 以新建一个 Notebook。

## 运行 Arctern

### 使用 Arctern 分析道路信息

> **注意：** 以下操作均在新建的 Notebook 中运行。

导入 `arctern`、`keplergl` 以及其他的相关库：


```python
>>> from keplergl import KeplerGl
>>> import pandas as pd
>>> import arctern
```

以帝国大厦附近的两条道路为分析对象，创建 [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) 格式的 LINESTRING 对象（`road1`、`road2`）以表示这两条道路。

```python
>>> # road1 道路两端的经纬度坐标分别是 (-73.996324, 40.753388)、(-73.972088, 40.743215)
>>> # road2 道路两端的经纬度坐标分别是 (-73.989555, 40.741531)、(-73.973952, 40.762962)
>>> road1 = 'LINESTRING (-73.996324 40.753388, -73.972088 40.743215)'
>>> road2 = 'LINESTRING (-73.989555 40.741531, -73.973952 40.762962)'
```

使用 `arctern.ST_Intersects` 方法检查 `road1` 与 `road2` 是否相交。

* 若返回 *True*，则相交；
* 若返回 *False*，则不相交。

```python
>>> arctern.ST_Intersects(arctern.ST_GeomFromText(road1), arctern.ST_GeomFromText(road2))
0    True
dtype: bool
```

### 使用 Kepler.Gl 绘制地图

使用 Kepler.Gl 在地图上绘制 `road1` 和 `road2`，观察这两条路是否相交：

```python
>>> KeplerGl(height=600,data={"road1": pd.DataFrame(data={"road1":[road1]}),
                          "road2": pd.DataFrame(data={"raod2":[road2]})})
```

![](../../../img/quick_start/crossed_road.png)

你还可以点击 Kepler.Gl 界面右上角的 **&gt;** 按钮以展开侧边栏，在其中设置每条路线的颜色和线宽。

![](../../../img/quick_start/kepler_set_witth.png)