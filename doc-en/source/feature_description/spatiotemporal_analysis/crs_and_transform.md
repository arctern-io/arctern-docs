# Coordinate reference system

This article describes what is **Coordinate Reference System (CRS)** and how to use Arctern to transform CRS.

## Supported CRS

Arctern supports common CRS, such as the traditional latitude and longitude coordinate system, and the **Universal Transverse Mercator (UTM)** system. See [Spatial Reference](https://spatialreference.org) for more information about CRS.

Arctern requires you to use a string in **SRID (Spatial Reference System Identifier)** format to represent a coordinate reference system. For example, "EPSG:4326" stands for the latitude and longitude coordinate system.

## Transforming CRS

To transform CRS of a geometry, 

1. use the [`set_crs`](../../api_reference/standalone_api/api/arctern.GeoSeries.set_crs.html) method to set the currently used CRS of the geometry; 
2. use the [`to_crs`](../../api_reference/standalone_api/api/arctern.GeoSeries.to_crs.html) method to perform CRS transformation on the geometry.

The following shows how to use Arctern to transform the coordinates of a geometry from the latitude and longitude coordinate system to the UTM system.

### Generating dataset

By creating a GeoSeries data set, you can batch convert the CRS of all geometries in the dataset.

First, create some geometric objects in WKT format: `point`, `linestring` and `polygon`. 

Then, create a GeoSeries object `geos` that contains the above objects.

```python
>>> from arctern import GeoSeries
>>> point = 'POINT (-73.993003 40.747594)'
>>> linestring = 'LINESTRING (-73.9594166 40.7593773,-73.9593736 40.7593593)'
>>> polygon = 'POLYGON ((-73.97324 40.73747, -73.96524 40.74507, -73.96118 40.75890, -73.95556 40.77654, -73.97324 40.73747))'
>>> geos = GeoSeries([point, linestring, polygon])
>>> geos
0                         POINT (-73.993003 40.747594)
1    LINESTRING (-73.9594166 40.7593773,-73.9593736...
2    POLYGON ((-73.97324 40.73747,-73.96524 40.7450...
dtype: GeoDtype
```

### Setting CRS

The [`set_crs`](../../api_reference/standalone_api/api/arctern.GeoSeries.set_crs.html) method sets the currently used CRS of `geos`. 

In this example, we use the latitude and longitude coordinate system (EPSG:4326) as the initial CRS.

<!-- [set_crs](/path/to/set_crs) -->

```python
>>> geos.set_crs("EPSG:4326")
>>> geos.crs
'EPSG:4326'
```

### Transforming CRS

The [`to_crs`](../../api_reference/standalone_api/api/arctern.GeoSeries.to_crs.html) method transforms the CRS of `geos` from the latitude and longitude coordinate system (EPSG:4326) to the UTM system (EPSG:3857).

<!-- [to_crs](/path/to/to_crs) -->

```python
>>> geos = geos.to_crs(crs="EPSG:3857")
>>> geos
0           POINT (-8236863.41622516 4975182.82064036)
1    LINESTRING (-8233124.59527958 4976914.39450424...
2    POLYGON ((-8234663.40912862 4973695.32847375,-...
dtype: GeoDtype
```

### Result

The [`crs`](../../api_reference/standalone_api/api/arctern.GeoSeries.crs.html) attribute of GeoSeries objects shows the current CRS. The result shows that the CRS of `geos` has been successfully transformed to the UTM system.

```python
>>> geos.crs
'EPSG:3857'
```
