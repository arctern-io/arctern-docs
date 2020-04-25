# Quick Start

本文以纽约出租车数据集为例，展示如何使用 Arctern 完成数据的导入、运算和展示。

## 数据准备

在 Arctern 运行环境中下载[纽约出租车数据集](https://github.com/zilliztech/arctern-resources/blob/benchmarks/benchmarks/dataset/nyc_taxi/0_2M_nyc_taxi_and_building/0_2M_nyc_taxi_and_building.csv)，该数据集包含2009年纽约市出租车运营记录，各字段的含义如下：

- VendorID: string，运营商名称；
- tpep_pickup_datetime: string，上车时间；
- tpep_dropoff_datetime: string，下车时间；
- passenger_count: long，乘客数量；
- trip_distance: double，行程距离；
- pickup_longitude: double，上车地点-经度；
- pickup_latitude: double，上车地点-纬度；
- dropoff_longitude: double，下车地点-经度；
- dropoff_latitude: double，下车地点-纬度；
- fare_amount: double，行程费用；
- tip_amount: double，小费；
- total_amount: double，总费用；
- buildingid_pickup: long，上车地点所在建筑的id；
- buildingid_dropoff: long，下车地点所在建筑的id；
- buildingtext_pickup: string，上车地点所在建筑的轮廓描述；
- buildingtext_dropoff: string，下车地点所在建筑的轮廓描述。

该数据中时间格式为：`yyyy-MM-dd HH:mm::ss XXXXX`，如`2009-04-12 03:16:33 +00:00`。

## 加载数据

以下通过 Python 交互界面展示 Arctern 的使用方法。根据测试数据各字段的名称和数据类型，构建导入测试数据的 `schema`。

```python
>>> import pandas as pd
>>> nyc_schame={
...     "VendorID":"string",
...     "tpep_pickup_datetime":"string",
...     "tpep_dropoff_datetime":"string",
...     "passenger_count":"int64",
...     "trip_distance":"double",
...     "pickup_longitude":"double",
...     "pickup_latitude":"double",
...     "dropoff_longitude":"double",
...     "dropoff_latitude":"double",
...     "fare_amount":"double",
...     "tip_amount":"double",
...     "total_amount":"double",
...     "buildingid_pickup":"int64",
...     "buildingid_dropoff":"int64",
...     "buildingtext_pickup":"string",
...     "buildingtext_dropoff":"string",
... }
>>> df=pd.read_csv("/tmp/0_2M_nyc_taxi_and_building.csv",
...                dtype=nyc_schame,
...                date_parser=pd.to_datetime,
...                parse_dates=["tpep_pickup_datetime","tpep_dropoff_datetime"])
```

打印数据的前5行，验证数据是否加载成功：

```python
>>> df.head()
  VendorID      tpep_pickup_datetime     tpep_dropoff_datetime  passenger_count  ...  buildingid_pickup  buildingid_dropoff  buildingtext_pickup                               buildingtext_dropoff
0      CMT 2009-04-12 03:16:33+00:00 2009-04-12 03:20:32+00:00                1  ...                  0                   0                 <NA>                                               <NA>
1      VTS 2009-04-14 11:22:00+00:00 2009-04-14 11:38:00+00:00                1  ...                  0              150047                 <NA>  POLYGON ((-73.9833003295812 40.7590607716671,-...
2      CMT 2009-04-15 09:34:58+00:00 2009-04-15 09:49:35+00:00                1  ...                  0                   0                 <NA>                                               <NA>
3      CMT 2009-04-30 18:58:19+00:00 2009-04-30 19:05:27+00:00                1  ...                  0              365034                 <NA>  POLYGON ((-73.9822052908304 40.7588972120254,-...
4      CMT 2009-04-26 13:03:04+00:00 2009-04-26 13:27:54+00:00                1  ...                  0                   0                 <NA>                                               <NA>

[5 rows x 16 columns]
```

## 数据过滤

在指定地理区域（经度范围：-73.991504至-73.945155；纬度范围：40.770759至40.783434）中随机选取`200` 行数据。

```python
>>> pos1=(-73.991504, 40.770759)
>>> pos2=(-73.945155, 40.783434)
>>> limit_num=200
>>> 
>>> pickup_df = df[(df.pickup_longitude>pos1[0]) & (df.pickup_longitude<pos2[0]) & (df.pickup_latitude>pos1[1]) & (df.pickup_latitude<pos2[1])]
>>> pickup_df = pickup_df.head(limit_num)
```

## 使用 Arctern 提供的 GeoSpatial 函数处理数据

导入 `arctern` 模块：

```python
>>> from arctern import *
```

根据经纬度数据创建坐标点数据：

```python
>>> ST_AsText(ST_Point(pickup_df.pickup_longitude, pickup_df.pickup_latitude)).head()
0    POINT (-73.959908 40.776353)
1    POINT (-73.955183 40.773459)
2     POINT (-73.989523 40.77129)
3    POINT (-73.988154 40.774829)
4    POINT (-73.982687 40.771625)
dtype: object
```

将坐标点数据使用的空间坐标系从`EPSG:4326`坐标系转换为到`EPSG:3857`坐标系，更多不同空间坐标系标准的详细信息请查看[维基百科相关页面](https://en.wikipedia.org/wiki/Spatial_reference_system)。

```python
>>> ST_AsText(ST_Transform(ST_Point(pickup_df.pickup_longitude, pickup_df.pickup_latitude),'epsg:4326', 'epsg:3857')).head()
0    POINT (-8233179.29767736 4979409.53917853)
1    POINT (-8232653.31308336 4978984.12438949)
2     POINT (-8236476.0243972 4978665.29594441)
3      POINT (-8236323.6280143 4979185.5105596)
4     POINT (-8235715.04435814 4978714.5380168)
dtype: object
```
可以在[EPSG](http://epsg.io/transform#s_srs=4326&t_srs=3857)网站上验证转换是否正确

![](../../../../img/quickstart/epsg-4326-to-3857-example.png)


## 使用 Arctern 绘制图层

导入绘图需要使用的模块：

```python
>>> from arctern.util import save_png
>>> from arctern.util.vega import vega_pointmap
```

通过 Arctern 提供的绘图函数绘制图层：

```python
>>> vega = vega_pointmap(1024, 384, bounding_box=[pos1[0], pos1[1], pos2[0], pos2[1]], point_size=10, point_color="#2DEF4A", opacity=1, coordinate_system="EPSG:4326")
>>> png = point_map_layer(vega, ST_Point(pickup_df.pickup_longitude, pickup_df.pickup_latitude))
>>> save_png(png, '/tmp/arctern_pointmap_pandas.png')
```


绘图结果如下：

![](../../../../img/quickstart/arctern_pointmap_pandas.png)
