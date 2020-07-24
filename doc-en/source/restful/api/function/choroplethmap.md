# Choropleth Map

Draws a choropleth map according to the relevant drawing parameters and returns the map in Base64 format.

## Request description

- Method: `POST`
- URL: `/choroplethmap`
- Headers:
    - `Content-Type: application/json`
- Body: See [Body example](#Body-example).

## Body example

Parameter description:

- `input_data`: Description of input data. Needs to be the names of the defined variables or executable Python statements.
    - `region_boundaries`: Location of the contour, which is pandas.Series in WKB format.
    - `weights`: Weight of the contour, which is pandas.Series of float64 type or int64 type.
- `params`: Drawing parameters.
    - `width`: Width of the image.
    - `height`: Height of the image.
    - `bounding_box`: Geographic extent represented by the rendered image [x_min, y_min, x_max, y_max].
    - `coordinate_system`: Coordinate system of the input data. See [World Geodetic System](https://en.wikipedia.org/wiki/World_Geodetic_System) for more information.
    - `color_gradient`: The color gradient range of the contour, that is, the color of the contour is gradient from the left to the right.
    - `color_bound`: Value range of the contour color, used together with `color_gradient`.
    - `opacity`: Opacity of the contour.
    - `aggregation_type`: Aggregation type.

### Python backend

A JSON example for the Python backend is as follows:

```json
{
    "input_data": {
        "region_boundaries": "ST_GeomFromText(raw_data.dropna().buildingtext_pickup)",
        "weights": "raw_data.dropna().fare_amount"
    },
    "params": {
        "width": 1024,
        "height": 896,
        "bounding_box": [-75.37976, 40.191296, -71.714099, 41.897445],
        "coordinate_system": "EPSG:4326",
        "color_gradient": ["#0000FF", "#FF0000"],
        "color_bound": [2.5, 5],
        "opacity": 1,
        "aggregation_type": "sum"
    }
}
```

### PySpark backend

If you use the PySpark backend, you only need to change the `input_data` in the above example for Python backend to the corresponding SQL query. See the following example:

```
"sql": "select ST_GeomFromText(buildingtext_pickup) as polygon, fare_amount as count from raw_data where buildingtext_pickup!=''"
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

url = "http://localhost:8080/choroplethmap"

payload  = {
    "input_data": {
        "region_boundaries": "ST_GeomFromText(raw_data.dropna().buildingtext_pickup)",
        "weights": "raw_data.dropna().fare_amount"
    },
    "params": {
        "width": 1024,
        "height": 896,
        "bounding_box": [-75.37976, 40.191296, -71.714099, 41.897445],
        "coordinate_system": "EPSG:4326",
        "color_gradient": ["#0000FF", "#FF0000"],
        "color_bound": [2.5, 5],
        "opacity": 1,
        "aggregation_type": "mean"
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
curl --location --request POST 'http://localhost:8080/choroplethmap' \
--header 'Content-Type: application/json' \
--data-raw '{
    "input_data": {
        "region_boundaries": "ST_GeomFromText(raw_data.dropna().buildingtext_pickup)",
        "weights": "raw_data.dropna().fare_amount"
    },
    "params": {
        "width": 1024,
        "height": 896,
        "bounding_box": [-75.37976, 40.191296, -71.714099, 41.897445],
        "coordinate_system": "EPSG:4326",
        "color_gradient": ["#0000FF", "#FF0000"],
        "color_bound": [2.5, 5],
        "opacity": 1,
        "aggregation_type": "mean"
    }
}'
```

## Response example

```json
{
    "status": "success",
    "code": "200",
    "result": "Base64-encoded choropleth map data"
}
```