# Plot methods

This article describes Arctern's plot methods.

## [plot_geometry](../../api_reference/plot/api/arctern.plot.plot_geometry.html)
### Definition

```python
   def plot_geometry(ax, geoms, **style_kwds)
```
### Parameters

* **ax:** An instance of matplotlib.axes._subplots.AxesSubplot. It represents the axes of canvas.
* **geoms:** A collection of geometries to be drawn. It accepts pandas Series, Arctrn GeoSeries, or pandas DataFrame as input. Note that the geometries must be in WKB form.
* **style_kwds:** Parameters that describes the drawing style, including:
  * **linewidth:** Line width of lines or polygons
  * **linestyle:** Line style
  * **edgecolor:** Edge color of polygons
  * **facecolor:** Face color of polygons
  * **color:** Color of points or lines
  * **marker:** Shape of points
  * **markersize:** Size of points
  * **alpha:** Transparency

The following examples show you how to use the [plot_geometry](../../api_reference/plot/api/arctern.plot.plot_geometry.html) method to draw geometric figures.


## Install dependencies
```bash
conda install -c conda-forge descartes
conda install -c conda-forge matplotlib
```

## Generate test data

We use the GeoSeries constructor to create some geometric objects, including points (POINT), lines (LINESTRING), polygons (POLYGON), multiple points (MULTIPOINT), multiple polygons (MULTIPOLYGON), geometry collections (GEOMETRYCOLLECTION), and multiple lines (MULTILINESTRING) . In the next steps, we will demonstrate how to draw these geometric figures.

```python
>>> from arctern import GeoSeries
>>> 
>>> point_s = GeoSeries(["POINT (3 4)"])
>>> linestring_s = GeoSeries(["LINESTRING (0 0,1 1,2 3)"])
>>> polygon_s = GeoSeries(["POLYGON ((0 0,0 1,1.5 2,0 0))"])
>>> multi_point_s = GeoSeries(["MULTIPOINT (3 4,5 5)"])
>>> multi_linestring_s = GeoSeries(["MULTILINESTRING ((0 0,1 1,2 3),(1 0,2 4))"])
>>> multi_polygon_s = GeoSeries(["MULTIPOLYGON (((0 0,0 1,1.5 2,0 0)),((0 0,0 2,1 0,0 0)))"])
>>> geom_collection_s = GeoSeries(["GEOMETRYCOLLECTION("
...                     "polygon((1 1,1 2,2 2,2 1,1 1)),"
...                     "linestring(0 1, 5 6, 10 11),"
...                     "POINT(4 7))"])
>>> geoms = GeoSeries(["MULTILINESTRING ((0 0,1 1,2 3),(1 0,2 4))","POINT (3 4)","POLYGON ((0 0,0 1,1.5 2,0 0))"])
```


## Plot geometric figures

### Point

- **Color:** Blue
- **Transparency:** 0.4
```python
>>> from arctern import plot
>>> import matplotlib.pyplot as plt
>>> fig,ax = plt.subplots()
>>> ax.grid()
>>> plot.plot_geometry(ax,point_s,color=["blue"],alpha=0.4)
>>> plt.show()
```

![](./img/point_s.png)

### Line

- **Color:** Blue
- **Line style:** " -. "
- **Transparency:** 0.4

```python
>>> from arctern import plot
>>> import matplotlib.pyplot as plt
>>> fig,ax = plt.subplots()
>>> ax.grid()
>>> plot.plot_geometry(ax,linestring_s,color=["blue"],linestyle=["-."],alpha=0.4)
>>> plt.show()
```

![](./img/linestring_s.png)

### Polygon

- **Face color:** Green
- **Line width:** 3.0
- **Edge color:** Red
- **Transparency:** 0.4

```python
>>> from arctern import plot
>>> import matplotlib.pyplot as plt
>>> fig,ax = plt.subplots()
>>> ax.grid()
>>> plot.plot_geometry(ax,polygon_s,facecolor=["green"],linewidth=3.0,edgecolor=["red"],alpha=0.4)
>>> plt.show()
```

![](./img/polygon_s.png)

### Multiple points

- **Color:** Blue
- **Marker:** " * "
- **Size:** 40.0
- **Transparency:** 0.4

```python
>>> from arctern import plot
>>> import matplotlib.pyplot as plt
>>> fig,ax = plt.subplots()
>>> ax.grid()
>>> plot.plot_geometry(ax,multi_point_s,color=["blue"],marker="*",markersize=40.0,alpha=0.4)
>>> plt.show()
```

![](./img/multi_point_s.png)

### Multiple lines

- **Color:** Blue
- **Line style:** " -- "
- **Transparency:** 0.4

```python
>>> from arctern import plot
>>> import matplotlib.pyplot as plt
>>> fig,ax = plt.subplots()
>>> ax.grid()
>>> plot.plot_geometry(ax,multi_linestring_s,color=["blue"],linestyle=["--"],alpha=0.4)
>>> plt.show()
```

![](./img/multi_linestring_s.png)

### Multiple polygons

- **Face color:** Blue
- **Transparency:** 0.4

```python
>>> from arctern import plot
>>> import matplotlib.pyplot as plt
>>> fig,ax = plt.subplots()
>>> ax.grid()
>>> plot.plot_geometry(ax,multi_polygon_s,facecolor=["blue"],alpha=0.4)
>>> plt.show()
```

![](./img/multi_polygon_s.png)

### Geometry collection

- **Face Color:** Blue
- **Edge Color:** Red
- **Point and line Color:** Green
- **Transparency:** 0.4

```python
>>> from arctern import plot
>>> import matplotlib.pyplot as plt
>>> fig,ax = plt.subplots()
>>> ax.grid()
>>> plot.plot_geometry(ax,geom_collection_s,facecolor=["blue"],edgecolor=["red"],color=["green"],alpha=0.4)
>>> plt.show()
```

![](./img/geom_collection_s.png)

### Multiple Geometries

- **Multiple lines**
  * **Line style:** " -. " 
  * **Color:** Blue
- **Polygon**
  * **Line style:** " -- "
  * **Face color:** Green 
  * **Edge color**: Red
  * **Marker:** " o "
  * **Transparency:** 0.4

```python
>>> from arctern import plot
>>> import matplotlib.pyplot as plt
>>> fig,ax = plt.subplots()
>>> ax.grid()
>>> plot.plot_geometry(ax,geoms,linestyle=["-.","","--"],marker="o",color=["blue","red","green"],edgecolor=["","","red"],alpha=0.4)
>>> plt.show()
```

![](./img/geoms.png)

### Plot geometries multiple times

- **Line**
   * **Color:** Blue
   * **Line style:** " -. "
   * **Transparency:** 0.4
- **Polygon**
   * **Face color:** Green
   * **Line width:** 3.0
   * **Edge color:** Red
   * **Transparency:** 0.4
- **Geometry collection**
   * **Face color:** Blue
   * **Edge color:** Red
   * **Point and line color:** Green
   * **Transparency:** 0.4

```python
>>> from arctern import plot
>>> import matplotlib.pyplot as plt
>>> fig,ax = plt.subplots()
>>> ax.grid()
>>> plot.plot_geometry(ax,linestring_s,color=["blue"],linestyle=["-."],alpha=0.4)
>>> plot.plot_geometry(ax,polygon_s,facecolor=["green"],linewidth=3.0,edgecolor=["red"],alpha=0.4)
>>> plot.plot_geometry(ax,geom_collection_s,facecolor=["blue"],edgecolor=["red"],color=["green"],alpha=0.4)
>>> plt.show()
```

![](./img/multi_plot.png)
