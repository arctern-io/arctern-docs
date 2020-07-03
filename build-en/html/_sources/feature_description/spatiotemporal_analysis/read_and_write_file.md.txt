# Reading and writing files

Arctern inherits the file reading and writing interface of pandas and supports reading and writing data types of [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry), [WKB](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary) and [GeoJson](https://geojson.org/) files. For the specific methods of reading and writing files through pandas, please refer to [pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/reference/io.html).

## Importing files

### From WKT and WKB format

We use the **wkt_geos.csv** file to demonstrate how to read WKT and WKB data from files. This file mainly defines four geometric objects in WKT format, including one point (POINT) and three polygons (POLYGON). The content of the file is as follows:

```
geos
POINT (30 10)
POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))
POLYGON ((1 2, 3 4, 5 6, 1 2))
POLYGON ((1 1, 3 1, 3 3, 1 3, 1 1))
```

First, use the [`read_csv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) of pandas method to import the file and construct the pandas.Series object `data_wkt`:

```python
>>> import pandas as pd
>>> import arctern
>>> 
>>> df = pd.read_csv("</path/to/wkt_geos.csv>",sep='|')
>>> data_wkt = df['geos']
>>> print(data_wkt)
0                                    POINT (30 10)
1    POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))
2                   POLYGON ((1 2, 3 4, 5 6, 1 2))
3              POLYGON ((1 1, 3 1, 3 3, 1 3, 1 1))
Name: geos, dtype: object
```

Construct an arctern.GeoSeries object `geo_wkt` based on the pandas.Series object `data_wkt` made up of WKT data:

```python
>>> geo_wkt = arctern.GeoSeries(data_wkt)
```

In order to demonstrate how to read data in WKB format and create GeoSeries objects, we converted the pandas.Series object that was previously read and created from the **wkt_geos.csv** file from WKT format to WKB format. Specifically, we use the [`to_wkb`](../../api_reference/standalone_api/api/arctern.GeoSeries.to_wkb.html) method to get the pandas.Series object `data_wkb` in WKB format from the GeoSeries object `geo_wkt`.

Then, construct the arctern.GeoSeries object `geo_wkb` based on the pandas.Series object `data_wkb` in WKB format:

<!-- [to_wkb](/path/to/to_wkb) -->

```python
>>> data_wkb = geo_wkt.to_wkb()
>>> geo_wkb = arctern.GeoSeries(data_wkb)
```

Use the [`geom_equals`](../../api_reference/standalone_api/api/arctern.GeoSeries.geom_equals.html) method of GeoSeries to compare `geo_wkt` and `geo_wkb`. It turns out that these two GeoSeries objects are the same because they are essentially constructed from the same data.

```pytho
>>> geo_wkt.geom_equals(geo_wkb)
0    True
1    True
2    True
3    True
dtype: bool
```

### From GeoJson format

We use the **geos.json** file to demonstrate how to read GeoJson data from files. This file mainly defines four geometric objects in WKT format, including one point (POINT) and three polygons (POLYGON). The contents of the file are as follows:

```
{
    "0":"{ \"type\": \"Point\", \"coordinates\": [ 30.0, 10.0 ] }",
    "1":"{ \"type\": \"Polygon\", \"coordinates\": [ [ [ 30.0, 10.0 ], [ 40.0, 40.0 ], [ 20.0, 40.0 ], [ 10.0, 20.0 ], [ 30.0, 10.0 ] ] ] }",
    "2":"{ \"type\": \"Polygon\", \"coordinates\": [ [ [ 1.0, 2.0 ], [ 3.0, 4.0 ], [ 5.0, 6.0 ], [ 1.0, 2.0 ] ] ] }",
    "3":"{ \"type\": \"Polygon\", \"coordinates\": [ [ [ 1.0, 1.0 ], [ 3.0, 1.0 ], [ 3.0, 3.0 ], [ 1.0, 3.0 ], [ 1.0, 1.0 ] ] ] }"
}
```

First, use the [`read_json`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html) method of pandas to import the file and construct the pandas.Series object `data_json`:

```python
>>> df = pd.read_json("</path/to/geos.json>",orient='index')
>>> data_json = df[0]
>>> print(data_json)
0    { "type": "Point", "coordinates": [ 30.0, 10.0...
1    { "type": "Polygon", "coordinates": [ [ [ 30.0...
2    { "type": "Polygon", "coordinates": [ [ [ 1.0,...
3    { "type": "Polygon", "coordinates": [ [ [ 1.0,...
Name: geos, dtype: object
```

Construct an arctern.GeoSeries object `geo_json` based on the pandas.Series object `data_json` made up of GeoJson data:

```python
>>> geo_json = arctern.GeoSeries.geom_from_geojson(data_json)
```

Use the [`geom_equals`](../../api_reference/standalone_api/api/arctern.GeoSeries.geom_equals.html) method of GeoSeries to compare `geo_wkb` and `geo_json`. It turns out that these two GeoSeries objects are the same because the source files of `geo_wkb` and `geo_json` (**wkt_geos.csv** and **geos.json**) define the same geometry.

```python
>>> geo_json.geom_equals(geo_wkb)
0    True
1    True
2    True
3    True
dtype: bool
```

## Exporting files

### From WKT format

First, use the [`to_wkt`](../../api_reference/standalone_api/api/arctern.GeoSeries.to_wkt.html) method of GeoSeries to get a pandas.Series object from the GeoSeries object. Then, use the [`to_csv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html) method of pandas.Series to save the data as a CSV file.

<!--  [to_wkt](/path/to/to_wkt)  -->

```python
>>> out_file_data = geo_wkb.to_wkt()
>>> print(out_file_data)
0                                POINT (30 10)
1    POLYGON ((30 10,40 40,20 40,10 20,30 10))
2                  POLYGON ((1 2,3 4,5 6,1 2))
3              POLYGON ((1 1,3 1,3 3,1 3,1 1))
dtype: object
>>> out_file_data.to_csv("</path/to/out_wkt_geos.csv>",index=None,quoting=1)
```

### From GeoJson format

First, use the [`as_geojson`](../../api_reference/standalone_api/api/arctern.GeoSeries.as_geojson.html) method of GeoSeries to get a pandas.Series object from the GeoSeries object. Then, use the [`to_json`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html) method of pandas.Series to save the data as a JSON file.

<!--  [as_geojson](/path/to/as_geojson) -->

```python
>>> out_file_data = geo_wkb.as_geojson()
>>> print (out_file_data)
0    { "type": "Point", "coordinates": [ 30.0, 10.0...
1    { "type": "Polygon", "coordinates": [ [ [ 30.0...
2    { "type": "Polygon", "coordinates": [ [ [ 1.0,...
3    { "type": "Polygon", "coordinates": [ [ [ 1.0,...
dtype: object
>>> out_file_data.to_json("</path/to/out_geos.json>")
```