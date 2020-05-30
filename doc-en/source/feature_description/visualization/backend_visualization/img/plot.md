生成模拟数据


```python
import pandas as pd

def gen_data(num_rows, bbox):
    import random
    pickup_longitude = [(bbox[2]-bbox[0])*random.random()+bbox[0] for i in range(num_rows)]
    pickup_latitude = [(bbox[3]-bbox[1])*random.random()+bbox[1] for i in range(num_rows)]
    fare_amount = [50*random.random() for i in range(num_rows)]
    total_amount = [100*random.random() for i in range(num_rows)]
    return pd.DataFrame({"pickup_longitude":pickup_longitude,
                         "pickup_latitude":pickup_latitude,
                         "fare_amount":fare_amount,
                         "total_amount":total_amount})
num_rows=200
bbox=[-73.991504, 40.770759, -73.945155, 40.783434]
df=gen_data(num_rows,bbox)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pickup_longitude</th>
      <th>pickup_latitude</th>
      <th>fare_amount</th>
      <th>total_amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-73.989516</td>
      <td>40.777649</td>
      <td>5.758467</td>
      <td>80.374407</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-73.962420</td>
      <td>40.775845</td>
      <td>36.258671</td>
      <td>45.518298</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-73.952623</td>
      <td>40.782159</td>
      <td>9.452726</td>
      <td>59.120986</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-73.973447</td>
      <td>40.772217</td>
      <td>17.017239</td>
      <td>52.121049</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-73.956424</td>
      <td>40.770940</td>
      <td>7.077901</td>
      <td>64.379483</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>195</th>
      <td>-73.967410</td>
      <td>40.782402</td>
      <td>0.023002</td>
      <td>4.605297</td>
    </tr>
    <tr>
      <th>196</th>
      <td>-73.978351</td>
      <td>40.770854</td>
      <td>5.533417</td>
      <td>39.747224</td>
    </tr>
    <tr>
      <th>197</th>
      <td>-73.972745</td>
      <td>40.774258</td>
      <td>16.623822</td>
      <td>79.458689</td>
    </tr>
    <tr>
      <th>198</th>
      <td>-73.964403</td>
      <td>40.781941</td>
      <td>16.241558</td>
      <td>42.934139</td>
    </tr>
    <tr>
      <th>199</th>
      <td>-73.960617</td>
      <td>40.782746</td>
      <td>38.848026</td>
      <td>82.932036</td>
    </tr>
  </tbody>
</table>
<p>200 rows × 4 columns</p>
</div>



安装依赖库
```bash
conda install -c conda-forge matplotlib
conda install -c conda-forge contextily
conda install -c conda-forge pyproj
```

导入绘图需要使用的模块


```python
import arctern
from arctern.util import save_png, vega
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
```

### 绘制透明的点图


```python
# 点的大小为 10，颜色为 #2DEF4A，不透明度为 1
point_vega = vega.vega_pointmap(1024, 
                                384, 
                                bounding_box=bbox, 
                                point_size=10, 
                                point_color="#2DEF4A", 
                                opacity=1, 
                                coordinate_system="EPSG:4326")
png = arctern.point_map_layer(point_vega, 
                              arctern.ST_Point(df.pickup_longitude,df.pickup_latitude))
save_png(png, '/tmp/arctern_pointmap.png')
plt.imshow(mpimg.imread("/tmp/arctern_pointmap.png"))
```




    <matplotlib.image.AxesImage at 0x7f2f45e87350>




![png](output_6_1.png)


### 绘制带背景地图的点图


```python
fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
arctern.plot_pointmap(ax, 
                      arctern.ST_Point(df.pickup_longitude,df.pickup_latitude),
                      bbox,
                      point_size=10,
                      point_color="#2DEF4A",
                      opacity=1,
                      coordinate_system="EPSG:4326")
```


![png](output_8_0.png)


### 绘制带权重的透明点图


```python
point_vega = vega.vega_weighted_pointmap(1024, 
                                    384, 
                                    bounding_box=bbox, 
                                    color_gradient=["#115f9a", "#d0f400"], 
                                    color_bound=[1, 50], 
                                    size_bound=[3, 15], 
                                    opacity=1.0, 
                                    coordinate_system="EPSG:4326")
png = arctern.weighted_point_map_layer(point_vega, 
                                       arctern.ST_Point(df.pickup_longitude,df.pickup_latitude),
                                       color_weights=df.fare_amount, 
                                       size_weights=df.total_amount)
save_png(png, "/tmp/arctern_weighted_pointmap.png")
plt.imshow(mpimg.imread("/tmp/arctern_weighted_pointmap.png"))
```




    <matplotlib.image.AxesImage at 0x7f2f09f6b550>




![png](output_10_1.png)


### 绘制带权重的含背景地图的点图


```python
fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
arctern.plot_weighted_pointmap(ax, 
                       arctern.ST_Point(df.pickup_longitude,df.pickup_latitude), 
                       df.fare_amount, 
                       df.total_amount, 
                       bbox, 
                       color_gradient=["#115f9a", "#d0f400"], 
                       color_bound=[1, 50], 
                       size_bound=[3, 15], 
                       opacity=1.0, 
                       coordinate_system="EPSG:4326")
```


![png](output_12_0.png)


### 绘制透明的热力图


```python
head_vega = vega.vega_heatmap(1024, 
                              384, 
                              bounding_box=bbox, 
                              map_zoom_level=13.0, 
                              coordinate_system="EPSG:4326")
png = arctern.heat_map_layer(head_vega, 
                     arctern.ST_Point(df.pickup_longitude,df.pickup_latitude), 
                     df.fare_amount)
save_png(png, "/tmp/arctern_heatmap.png")
plt.imshow(mpimg.imread("/tmp/arctern_heatmap.png"))
```




    <matplotlib.image.AxesImage at 0x7f2f09e41d50>




![png](output_14_1.png)


### 绘制带背景地图的热力图


```python
fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
arctern.plot_heatmap(ax, 
                     arctern.ST_Point(df.pickup_longitude,df.pickup_latitude), 
                     df.fare_amount, 
                     bbox, 
                     coordinate_system="EPSG:4326")
```


![png](output_16_0.png)


### 绘制透明的轮廓图


```python
p1="POLYGON ((-73.9559920952719 40.7798302112586,-73.9558373836227 40.780041920447,-73.955817052153 40.7800697417696,-73.9561541507251 40.7802120850128,-73.9560310179165 40.780380581462,-73.9559809829928 40.7804490491413,-73.9554245436102 40.780214085171,-73.9552722050953 40.7801497573115,-73.9554553121101 40.7798991968954,-73.9556088484124 40.7796890996611,-73.955620419799 40.7796732651862,-73.9559015149432 40.7797919620232,-73.9559920952719 40.7798302112586))"
p2="POLYGON ((-73.9542329907899 40.7787670145087,-73.9545101860555 40.7783876598084,-73.9546846384315 40.778461320293,-73.9548206058685 40.7785187302746,-73.9549036921298 40.7785538112695,-73.9550251774329 40.7786051054324,-73.9550562469185 40.7786182243649,-73.9549683394669 40.7787385313679,-73.9547798956672 40.778996428053,-73.954779053804 40.7789975803655,-73.9545166590009 40.7788867891633,-73.9544446005066 40.7788563633454,-73.9542329907899 40.7787670145087))"
choropleth_vega = vega.vega_choroplethmap(1024, 
                                          384, 
                                          bounding_box=bbox, 
                                          color_gradient=["#115f9a", "#d0f400"], 
                                          color_bound=[2.5, 5], 
                                          opacity=1.0, 
                                          coordinate_system="EPSG:4326")
png = arctern.choropleth_map_layer(choropleth_vega, 
                                   arctern.ST_GeomFromText(pd.Series([p1,p2])),
                                   pd.Series([50,50]))
save_png(png, "/tmp/arctern_choroplethmap.png")
plt.imshow(mpimg.imread("/tmp/arctern_choroplethmap.png"))
```




    <matplotlib.image.AxesImage at 0x7f2f09d97ed0>




![png](output_18_1.png)


### 绘制带背景地图的轮廓图


```python
p1="POLYGON ((-73.9559920952719 40.7798302112586,-73.9558373836227 40.780041920447,-73.955817052153 40.7800697417696,-73.9561541507251 40.7802120850128,-73.9560310179165 40.780380581462,-73.9559809829928 40.7804490491413,-73.9554245436102 40.780214085171,-73.9552722050953 40.7801497573115,-73.9554553121101 40.7798991968954,-73.9556088484124 40.7796890996611,-73.955620419799 40.7796732651862,-73.9559015149432 40.7797919620232,-73.9559920952719 40.7798302112586))"
p2="POLYGON ((-73.9542329907899 40.7787670145087,-73.9545101860555 40.7783876598084,-73.9546846384315 40.778461320293,-73.9548206058685 40.7785187302746,-73.9549036921298 40.7785538112695,-73.9550251774329 40.7786051054324,-73.9550562469185 40.7786182243649,-73.9549683394669 40.7787385313679,-73.9547798956672 40.778996428053,-73.954779053804 40.7789975803655,-73.9545166590009 40.7788867891633,-73.9544446005066 40.7788563633454,-73.9542329907899 40.7787670145087))"
fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
arctern.plot_choroplethmap(ax, 
                           arctern.ST_GeomFromText(pd.Series([p1,p2])),
                           pd.Series([50,50]),
                           bbox, 
                           color_gradient=["#115f9a", "#d0f400"], 
                           color_bound=[2.5, 5], 
                           opacity=1.0, 
                           coordinate_system="EPSG:4326")
```


![png](output_20_0.png)


### 绘制透明的图标图

下载图标
```bash
wget https://raw.githubusercontent.com/zilliztech/arctern-docs/master/img/icon/arctern-icon-small.png -o /tmp/arctern-logo.png
```


```python
icon_vega = vega.vega_icon(1024, 
                           384, 
                           bounding_box=bbox, 
                           icon_path="/tmp/arctern-logo.png", 
                           coordinate_system="EPSG:4326")
png = arctern.icon_viz_layer(icon_vega,
                             arctern.ST_Point(df.pickup_longitude,df.pickup_latitude))
save_png(png, "/tmp/arctern_iconviz.png")
plt.imshow(mpimg.imread("/tmp/arctern_iconviz.png"))
```




    <matplotlib.image.AxesImage at 0x7f2f09cf2e50>




![png](output_22_1.png)


### 绘制带背景地图的图标图

下载图标
```bash
wget https://raw.githubusercontent.com/zilliztech/arctern-docs/master/img/icon/arctern-icon-small.png -o /tmp/arctern-logo.png
```


```python
fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
arctern.plot_iconviz(ax, 
                     arctern.ST_Point(df.pickup_longitude,df.pickup_latitude),  
                     icon_path="/tmp/arctern-logo.png", 
                     bounding_box=bbox,
                     coordinate_system="EPSG:4326")
```


![png](output_24_0.png)


### 绘制透明渔网图


```python
fish_vega = vega.vega_fishnetmap(1024, 
                                 384, 
                                 bounding_box=bbox, 
                                 cell_size=8, 
                                 cell_spacing=1, 
                                 opacity=1.0, 
                                 coordinate_system="EPSG:4326")
png = arctern.fishnet_map_layer(fish_vega,
                                arctern.ST_Point(df.pickup_longitude,df.pickup_latitude), 
                                df.fare_amount)
save_png(png, "/tmp/arctern_fishnetmap.png")
plt.imshow(mpimg.imread("/tmp/arctern_fishnetmap.png"))
```




    <matplotlib.image.AxesImage at 0x7f2f09784fd0>




![png](output_26_1.png)


### 绘制带背景地图的渔网图


```python
fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
arctern.plot_fishnetmap(ax, 
                        arctern.ST_Point(df.pickup_longitude,df.pickup_latitude), 
                        df.fare_amount, 
                        bbox, 
                        cell_size=8, 
                        cell_spacing=1, 
                        opacity=1.0, 
                        coordinate_system="EPSG:4326")
```


![png](output_28_0.png)

