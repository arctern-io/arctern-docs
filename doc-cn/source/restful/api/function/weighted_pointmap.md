# 带权点图

根据 SQL 语句以及相关画图参数绘制权重图，将绘图结果以 base64 编码方式返回。

## 请求说明

- HTTP方法: **POST**
- 请求URL: `/weighted_pointmap`
- Headers:
    - `Content-Type: application/json`
- Body:

如果数据处理后台为 python, 则示例 json 如下：

```json
{
    "input_data": {
        "points": "ST_Point(raw_data.pickup_longitude, raw_data.pickup_latitude)",
        "color_weights": "raw_data.fare_amount",
        "size_weights": "raw_data.total_amount"
    },
    "params": {
            "width": 1024,
            "height": 896,
            "bounding_box": [-75.37976, 40.191296, -71.714099, 41.897445],
            "color_gradient": ["#0000FF", "#FF0000"],
            "color_bound": [0, 2],
            "size_bound": [0, 10],
            "opacity": 1.0,
            "coordinate_system": "EPSG:4326"
    }
}
```

若数据处理后台为 pyspark, 则需将 input_data 改为如下内容：
```
"sql": "select ST_Point(col2, col2) as point, col2 as count1, col2 as count2 from table_name"
```

参数说明：

- sql：待执行的 SQL 查询语句，该查询的结果作为绘制带权点图的渲染对象；
- params：绘图参数，具体说明如下，详见 [Arctern-Spark 绘图接口文档](../../../spark/api/render/function/layer/weighted_pointmap.md)：
    - width：图片宽度；
    - height：图片高度；
    - bounding_box：渲染图片所表示的地理范围 [`x_min`, `y_min`, `x_max`, `y_max`]；
    - coordinate_system：输入数据的坐标系统，详见 [World Geodetic System](https://en.wikipedia.org/wiki/World_Geodetic_System)；
    - color_gradient：点的颜色渐变范围，即点的颜色从左边渐变到右边；
    - color_bound：点颜色的取值范围，与 `color_gradient` 配合使用；
    - opacity：点的不透明度；
    - size_bound：点大小的取值范围。

## 请求样例

### Python

本文示例代码使用 Python 的 `requests` 库调用 `Arctern RESTful API`，使用下面的命令安装 `requests`：

```bash
pip install requests
```

调用示例

```python
import requests
import json

url = "http://localhost:8080/weighted_pointmap"

payload = {
    "input_data": {
        "points": "ST_Point(raw_data.pickup_longitude, raw_data.pickup_latitude)",
        "color_weights": "raw_data.fare_amount",
        "size_weights": "raw_data.total_amount"
    },
    "params": {
            "width": 1024,
            "height": 896,
            "bounding_box": [-75.37976, 40.191296, -71.714099, 41.897445],
            "color_gradient": ["#0000FF", "#FF0000"],
            "color_bound": [0, 2],
            "size_bound": [0, 10],
            "opacity": 1.0,
            "coordinate_system": "EPSG:4326"
    }
}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

print(response.text.encode('utf8'))
```

### curl

```bash
curl --location --request POST 'http://localhost:8080/weighted_pointmap' \
--header 'Content-Type: application/json' \
--data-raw '{
    "input_data": {
        "points": "ST_Point(raw_data.pickup_longitude, raw_data.pickup_latitude)",
        "color_weights": "raw_data.fare_amount",
        "size_weights": "raw_data.total_amount"
    },
    "params": {
            "width": 1024,
            "height": 896,
            "bounding_box": [-75.37976, 40.191296, -71.714099, 41.897445],
            "color_gradient": ["#0000FF", "#FF0000"],
            "color_bound": [0, 2],
            "size_bound": [0, 10],
            "opacity": 1.0,
            "coordinate_system": "EPSG:4326"
    }
}'
```

## 响应样例

```json
{
    "status": "success",
    "code": "200",
    "result": "使用 base64 编码后的权重图数据"
}
```
