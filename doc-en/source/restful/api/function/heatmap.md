# Heat Map

Draws a heat map according to the relevant drawing parameters and returns the map in Base64 format.

## Request description

- Method: `POST`
- URL: `/heatmap`
- Headers:
    - `Content-Type: application/json`
- Body: See [Body example](#Body-example).

## Body example

Parameter description:

- `input_data`: Description of input data. Needs to be the names of the defined variables or executable Python statements.
    - `points`: Location of the point, which is pandas.Series in WKB format.
    - `weights`: Heat value, which is pandas.Series of float64 type or int64 type.
- `params`: Drawing parameters.
    - `width`: Width of the image.
    - `height`: Height of the image.
    - `bounding_box`: Geographic extent represented by the rendered image [x_min, y_min, x_max, y_max].
    - `coordinate_system`: Coordinate system of the input data. See [World Geodetic System](https://en.wikipedia.org/wiki/World_Geodetic_System) for more information.
    - `map_zoom_level`: Zoom level of the map, in the range of [1, 15].
    - `aggregation_type`: Aggregation type.

### Python backend

A JSON example for the Python backend is as follows:

```json
{
    "input_data": {
        "points": "ST_Point(raw_data.pickup_longitude, raw_data.pickup_latitude)",
        "weights": "raw_data.fare_amount"
    },
    "params": {
        "width": 1024,
        "height": 896,
        "bounding_box": [-75.37976, 40.191296, -71.714099, 41.897445],
        "coordinate_system": "EPSG:4326",
        "map_zoom_level": 10,
        "aggragation_type": "sum"
    }
}
```

### PySpark backend

If you use the PySpark backend, you only need to change the `input_data` in the above example for Python backend to the corresponding SQL query. See the following example:

```
"sql": "select ST_Point(pickup_longitude, pickup_latitude) as point, fare_amount as weights from raw_data"
```

## Request example

### Python

Examples in this article use Python's `requests` library. Run the following command to install `requests`:

```bash
pip install requests
```

Sample code:

```python
import requests
import json

url = "http://localhost:8080/heatmap"

payload = {
    "input_data": {
        "points": "ST_Point(raw_data.pickup_longitude, raw_data.pickup_latitude)",
        "weights": "raw_data.fare_amount"
    },
    "params": {
        "width": 1024,
        "height": 896,
        "bounding_box": [-75.37976, 40.191296, -71.714099, 41.897445],
        "coordinate_system": "EPSG:4326",
        "map_zoom_level": 10,
        "aggregation_type": "sum"
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
curl --location --request POST 'http://localhost:8080/heatmap' \
--header 'Content-Type: application/json' \
--data-raw '{
    "input_data": {
        "points": "ST_Point(raw_data.pickup_longitude, raw_data.pickup_latitude)",
        "weights": "raw_data.fare_amount"
    },
    "params": {
        "width": 1024,
        "height": 896,
        "bounding_box": [-75.37976, 40.191296, -71.714099, 41.897445],
        "coordinate_system": "EPSG:4326",
        "map_zoom_level": 10,
        "aggregation_type": "sum"
    }
}'
```

## Response example

```json
{
    "status": "success",
    "code": "200",
    "result": "Base64-encoded heat map data"
}
```
