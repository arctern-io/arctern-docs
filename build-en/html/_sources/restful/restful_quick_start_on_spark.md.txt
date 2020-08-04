# Quick Start (PySpark backend)

This article takes the New York taxi dataset as an example and uses PySpark as the data processing backend to illustrate how to import, compute, and display data through Arctern RESTful API.

> **Note:** By default, all sample codes in this section are run in Python 3.7 environment. To run in other Python environments, you need to adapt the code accordingly.

## Configure and start on server side

### Start the server

Start the server before calling Arctern RESTful API. For details, see [start the server](../install/webserver_installation_config.md).

### Prepare data

In the following example, you need to use the New York taxi dataset. This dataset contains the operating records of taxis in New York City in 2009. The meaning of each field is as follows:

| Field                  | Description                      | Type   |
| :-------------------- | :------------------------- | :----- |
| VendorID              | Name of vendor                  | string |
| tpep_pickup_datetime  | Pickup time                   | string |
| tpep_dropoff_datetime | Dropoff time                   | string |
| passenger_count       | Number of passengers                   | long   |
| trip_distance         | Distance of the trip                   | double |
| pickup_longitude      | Longitude of the pickup location              | double |
| pickup_latitude       | Latitude of the pickup location               | double |
| dropoff_longitude     | Longitude of the dropoff location              | double |
| dropoff_latitude      | Latitude of the dropoff location              | double |
| fare_amount           | Fare amount for the trip                   | double |
| tip_amount            | Tip amount                       | double |
| total_amount          | Total charge                     | double |
| buildingid_pickup     | ID of the building at pickup location     | long   |
| buildingid_dropoff    | ID of the building at dropoff location      | long   |
| buildingtext_pickup   | Description of the building at pickup location | string |
| buildingtext_dropoff  | Description of the building at dropoff location | string |

> **Note:** This dataset has 200000 rows. The time format is `yyyy-MM-dd HH:mm::ss XXXXX`, such as "2009-04-12 03:16:33 +00:00".

Download the New York taxi dataset:

```bash
$ wget https://media.githubusercontent.com/media/arctern-io/arctern-resources/benchmarks/benchmarks/dataset/nyc_taxi/0_2M_nyc_taxi_and_building/0_2M_nyc_taxi_and_building.csv
```

Check if the download is successful:

```bash
$ wc -l 0_2M_nyc_taxi_and_building.csv
```

### Install dependent packages

Sample codes in this article call Arctern RESTful API using the `request` library of Python. Run the command below to install `request`:

```bash
$ pip install requests
```

## Call API 

In the following example, assume the IP address is `127.0.0.1` and the RESTful service port is `8080`. If you have specified IP address and service port when starting arctern-server, use your specified IP and service port. 

### Import data

Use the `/loadfile` interface to import the New York taxi dataset and name the corresponding data table `raw_data`.

> **Note:** You need to replace `file_path` in the sample code with the absolute path to the data file.

```python
>>> import requests
>>> import json
>>> 
>>> file_path = "/example/data/0_2M_nyc_taxi_and_building.csv"
>>> payload = {
... "tables": [
...     {
...         "name": "raw_data",
...         "format": "csv",
...         "path": file_path,
...         "options": {
...             "header": "True",
...             "delimiter": ","
...         },
...         "schema": [
...             {"VendorID": "string"},
...             {"tpep_pickup_datetime": "string"},
...             {"tpep_dropoff_datetime": "string"},
...             {"passenger_count": "long"},
...             {"trip_distance": "double"},
...             {"pickup_longitude": "double"},
...             {"pickup_latitude": "double"},
...             {"dropoff_longitude": "double"},
...             {"dropoff_latitude": "double"},
...             {"fare_amount": "double"},
...             {"tip_amount": "double"},
...             {"total_amount": "double"},
...             {"buildingid_pickup": "long"},
...             {"buildingid_dropoff": "long"},
...             {"buildingtext_pickup": "string"},
...             {"buildingtext_dropoff": "string"}
...         ]
...     }
... ]
... }
>>> 
>>> r = requests.post(url="http://127.0.0.1:8080/loadfile", headers={"Content-Type": "application/json"}, data=json.dumps(payload))
>>> r.json()
{
    'code': 200,
    'message': 'load table successfully!',
    'status': 'success'
}
```

### Query information from data table

You have created a data table at backend named `raw_data`. Then, you can use the `/table/schema` interface to query field names and the corresponding data types.

```python
>>> import requests
>>> r = requests.get(url="http://127.0.0.1:8080/table/schema?table=raw_data")
>>> r.json()
{
    "code": 200,
    "schema": [
        {
            "col_name": "VendorID",
            "data_type": "string"
        },
        {
            "col_name": "tpep_pickup_datetime",
            "data_type": "string"
        },
        {
            "col_name": "tpep_dropoff_datetime",
            "data_type": "string"
        },
        {
            "col_name": "passenger_count",
            "data_type": "bigint"
        },
        {
            "col_name": "trip_distance",
            "data_type": "double"
        },
        {
            "col_name": "pickup_longitude",
            "data_type": "double"
        },
        {
            "col_name": "pickup_latitude",
            "data_type": "double"
        },
        {
            "col_name": "dropoff_longitude",
            "data_type": "double"
        },
        {
            "col_name": "dropoff_latitude",
            "data_type": "double"
        },
        {
            "col_name": "fare_amount",
            "data_type": "double"
        },
        {
            "col_name": "tip_amount",
            "data_type": "double"
        },
        {
            "col_name": "total_amount",
            "data_type": "double"
        },
        {
            "col_name": "buildingid_pickup",
            "data_type": "bigint"
        },
        {
            "col_name": "buildingid_dropoff",
            "data_type": "bigint"
        },
        {
            "col_name": "buildingtext_pickup",
            "data_type": "string"
        },
        {
            "col_name": "buildingtext_dropoff",
            "data_type": "string"
        }
    ],
    "status": "success",
    "table": "raw_data"
}
```

### SQL query

Use the `/query` interface to create, query, and delete the data table.

#### Create data table

Transform the time information in the `raw_data` data table from string to timestamp, delete fields irrelevant to subsequent operations, and save as a new data table named `nyc_taxi`.

```python
>>> import requests
>>> import json
>>> 
>>> sql = "create table nyc_taxi as (select VendorID, to_timestamp(tpep_pickup_datetime,'yyyy-MM-dd HH:mm:ss XXXXX') as tpep_pickup_datetime, to_timestamp(tpep_dropoff_datetime,'yyyy-MM-dd HH:mm:ss XXXXX') as tpep_dropoff_datetime, passenger_count, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, fare_amount, tip_amount, total_amount, buildingid_pickup, buildingid_dropoff, buildingtext_pickup, buildingtext_dropoff from raw_data where (pickup_longitude between -180 and 180) and (pickup_latitude between -90 and 90) and (dropoff_longitude between -180 and 180) and  (dropoff_latitude between -90 and 90))"
>>> payload = {
... "input_data": {
... "sql": sql
... },
... "collect_result": "0"
... }
>>> 
>>> r = requests.post(url="http://127.0.0.1:8080/query", headers={"Content-Type": "application/json"}, data=json.dumps(payload))
>>> r.json()
{
    'code': 200,
    'message': 'execute sql successfully!',
    'status': 'success'
}
```

#### Query data

Query the number of rows in the `nyc_taxi` data table.

```python
>>> import requests
>>> import json
>>> 
>>> sql = "select count(*) as num_rows from nyc_taxi"
>>> payload = { 
... "input_data":{
...     "sql": sql
... },
... "collect_result": "0"
... }
>>> 
>>> r = requests.post(url="http://127.0.0.1:8080/query", headers={"Content-Type": "application/json"}, data=json.dumps(payload))
>>> r.json()
{
    'code': 200,
    'message': 'execute sql successfully!',
    'result': [
        {'num_rows': 199999}
    ],
    'status': 'success'
}
```

#### Delete data table

Delete the original `raw_data` data table.

> **Note:** `Arctern RESTful` service does not actively delete data tables. Make sure to delete data tables that are no longer used to release server resources.

```python
>>> import requests
>>> import json
>>> 
>>> sql = "drop table if exists raw_data"
>>> payload = {
... "input_data":{
...     "sql": sql
... },
... "collect_result": "0"
... }
>>> 
>>> r = requests.post(url="http://127.0.0.1:8080/query", headers={"Content-Type": "application/json"}, data=json.dumps(payload))
>>> r.json()
{
    'code': 200,
    'message': 'execute sql successfully!',
    'status': 'success'
}
```

### Generate heat map

Use the `/heatmap` interface to generate a heat map based on the passenger's dropoff location and total charge for the trip. Red areas represent high cost while green areas represent low cost. The specific parameters of the heat map are explained in [Heat map RESTful API](./api/function/heatmap.html).

```python
>>> import requests
>>> import json
>>> 
>>> payload = {
... "input_data": {
...     "sql": "SELECT ST_Point (dropoff_longitude, dropoff_latitude) AS point, avg(fare_amount) AS w FROM nyc_taxi GROUP BY point"
... },
... "params": {
...     "width": 512,
...     "height": 448,
...     "bounding_box": [
...         -74.01556543545699,
...         40.69354738164881,
...         -73.9434424136598,
...         40.780921656427836
...     ],
...     "coordinate_system": "EPSG:4326",
...     "map_zoom_level": 10,
...     "aggregation_type": "sum"
... }
... }
>>> 
>>> r = requests.post(url="http://127.0.0.1:8080/heatmap", headers={"Content-Type": "application/json"}, data=json.dumps(payload))
>>> 
>>> import base64
>>> with open("/tmp/heatmap.png", "wb") as f:
...     f.write(base64.b64decode(r.json()['result']))
```

The resulting heat map is as follows:

![Heat map](./img/heatmap_spark.png)

### Delete data table

Use the `query` interface to delete the `nyc_taxi` data table to release server resources.

> **Note:** `Arctern RESTful` service does not actively delete data tables. Make sure to delete data tables that are no longer used to release server resources.

```python
>>> import requests
>>> import json
>>> 
>>> sql = "drop table if exists nyc_taxi"
>>> payload = {
... "input_data": {
...    "sql": sql 
... },
... "collect_result": "0"
... }
>>> 
>>> r = requests.post(url="http://127.0.0.1:8080/query", headers={"Content-Type": "application/json"}, data=json.dumps(payload))
>>> r.json()
{
    'code': 200,
    'message': 'execute sql successfully!',
    'status': 'success' 
}
```