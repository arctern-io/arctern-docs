# Data structure

## GeoSeries

GeoSeries is an array that stores and manipulates geometric datasets. By extending pandas Series, GeoSeries internally stores objects in WKB format, and can batch calculate and operate on the stored elements like pandas Series.

### Initializing

GeoSeries internally stores geometry in WKB format and accepts data in WKT or WKB format as input to initialize GeoSeries objects.

#### Initializing from WKT format data

You can put multiple string data in WKT format into a list, numpy.ndarray, or pandas.Series, and then pass in the GeoSeries constructor to create GeoSeries objects.

```python
>>> data = ['POINT(1 1)', 'POINT(1 3)']
>>> s = arctern.GeoSeries(data)
>>> s
0    POINT (1 1)
1    POINT (1 3)
dtype: GeoDtype
>>> data = pandas.Series(data)
>>> s = arctern.GeoSeries(data)
>>> s
0    POINT (1 1)
1    POINT (1 3)
dtype: GeoDtype
```

#### Initializing from WKB format data

You can put multiple string data in WKB format into a list, numpy.ndarray, or pandas.Series, and then pass the GeoSeries constructor to create GeoSeries objects.
```python
>>> data = [b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?',
...        b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x08@']
>>> s = arctern.GeoSeries(data)
>>> s
0    POINT (1 1)
1    POINT (1 3)
dtype: GeoDtype
```

### Method overview

GeoSeries implements common operations on geometry (unary operations and binary operations).

* When performing a unary operation on a GeoSeries object, Arctern performs the operation on all the geometry stored in the GeoSeries object.
* When performing binary operations on two GeoSeries objects, Arctern performs one-to-one operations on each of the geometries in the two GeoSeries objects according to the index.
* When performing a binary operation on a GeoSeries object and a geometry (object in WKB format), Arctern performs an operation on each geometry in the GeoSeries object and this geometry.

If the result of the operation is geometry, a new GeoSeries object is returned, otherwise a Pandas Series object is returned.

The following lists some of the GeoSeries methods, including operations on geometry measurement, relationship calculation, and conversion. For detailed interface introduction, please see [API Reference](api_link).

#### Geometric measurement  

- **GeoSeries.is_valid：** Check whether each geometry in the GeoSeries object is valid.
- **GeoSeries.area：** Calculate the area of each geometry in a GeoSeries object.
- **GeoSeries.distance：** For each geometry in the GeoSeries object, create a geometry with the maximum distance not greater than `distance`.
- **GeoSeries.distance_sphere：** For each geometry in the GeoSeries object, the minimum distance between two points on the earth's surface is calculated based on the latitude and longitude coordinates. This method uses the earth and radius defined by the SRID.
- **GeoSeries.hausdorff_distance：** For each geometry in the GeoSeries object, check the Hausdorff distance between it and the geometry at the same position in the `other` object. This distance is to measure the similarity between two geometries.

#### Geometric relationship operation

- **GeoSeries.touches：** For each geometry in the GeoSeries object, check whether it touches the geometry at the same position in the `other` object. "touches" means that two geometries have a common point on the boundary.
- **GeoSeries.overlaps：** For each geometry in the GeoSeries object, check whether it overlaps the geometry at the same position in the `other` object. "overlaps" means that the two geometries cross and do not contain each other.
- **GeoSeries.intersects：** For each geometry in the GeoSeries object, check whether it intersects with the geometry at the same position in the `other` object.

#### Geometric conversion

- **GeoSeries.precision_reduce：** For each geometry in the GeoSeries object, the geometry with reduced coordinate accuracy is created according to the specified valid digits number `precision`.
- **GeoSeries.make_valid：** For each geometry in the GeoSeries object, create a new valid geometry based on it. During the construction of the new geometry, no vertices of the original geometry are deleted. If the original geometry is already valid, then return the original geometry directly.
- **GeoSeries.curve_to_line：** For each geometry in the GeoSeries object, calculate its approximate representation. The approximate representation method is to convert the curve in each geometric figure into an approximate linear representation.


