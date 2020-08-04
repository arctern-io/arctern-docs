# Icon Map

Draws an icon map according to the relevant drawing parameters and returns the map in Base64 format.

## Request description

- Method: `POST`
- URL: `/icon_viz`
- Headers:
    - `Content-Type: application/json`
- Body: See [Body example](#Body-example).

## Body example

Parameter description:

- `input_data`: Description of input data. Needs to be the names of the defined variables or executable Python statements.
    - `points`: Location of points, which is pandas.Series in WKB format.
- `params`: Drawing parameters.
    - `width`: Width of the image.
    - `height`: Height of the image.
    - `bounding_box`: Geographic extent represented by the rendered image [x_min, y_min, x_max, y_max].
    - `icon_path`: Absolute path to the icon file in PNG format.
    - `coordinate_system`: Coordinate system of the input data. See [World Geodetic System](https://en.wikipedia.org/wiki/World_Geodetic_System) for more information.

### Python backend

A JSON example for the Python backend is as follows:

```json
{
    "input_data": {
        "points": "ST_Point(raw_data.pickup_longitude, raw_data.pickup_latitude)"
    },
    "params": {
        "width": 1024,
        "height": 896,
        "bounding_box": [-75.37976, 40.191296, -71.714099, 41.897445],
        "icon_path": "/path/to/icon.png",
        "coordinate_system": "EPSG:4326"
    }
}
```

### PySpark backend

If you use the PySpark backend, you only need to change the `input_data` in the above example for Python backend to the corresponding SQL query. See the following example:

```
"sql": "select ST_Point(pickup_longitude, pickup_latitude) as point from raw_data"
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

url = "http://localhost:8080/icon_viz"

payload  = {
    "input_data": {
        "points": "ST_Point(raw_data.pickup_longitude, raw_data.pickup_latitude)"
    },
    "params": {
        "width": 1024,
        "height": 896,
        "bounding_box": [-75.37976, 40.191296, -71.714099, 41.897445],
        "icon_path": "/path/to/icon.png",
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
curl --location --request POST 'http://localhost:8080/icon_viz' \
--header 'Content-Type: application/json' \
--data-raw '{
    "input_data": {
        "points": "ST_Point(raw_data.pickup_longitude, raw_data.pickup_latitude)"
    },
    "params": {
        "width": 1024,
        "height": 896,
        "bounding_box": [-75.37976, 40.191296, -71.714099, 41.897445],
        "icon_path": "/path/to/icon.png",
        "coordinate_system": "EPSG:4326"
    }
}'
```

## Response example

```json
{
    "status": "success",
    "code": "200",
    "result": "Base64-encoded icon map data"
}
```
