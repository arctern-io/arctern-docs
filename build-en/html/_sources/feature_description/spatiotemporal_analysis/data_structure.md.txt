# Data structure

## GeoSeries

GeoSeries is an array that stores and manipulates geometric datasets. By extending pandas Series, GeoSeries internally stores objects in WKB format, and can batch calculate and manipulate elements in the GeoSeries like pandas Series does.

### Initializing

GeoSeries internally stores geometry in WKB format and accepts data in WKT or WKB format as input to initialize GeoSeries objects.

#### Initializing from WKT format data

You can put multiple string data in WKT format into a list, numpy.ndarray, or pandas.Series, and then pass them to the GeoSeries constructor to create GeoSeries objects.

```python
>>> import pandas as pd
>>> data = ['POINT(1 1)', 'POINT(1 3)']
>>> s = arctern.GeoSeries(data)
>>> s
0    POINT (1 1)
1    POINT (1 3)
dtype: GeoDtype
>>> data = pd.Series(data)
>>> s = arctern.GeoSeries(data)
>>> s
0    POINT (1 1)
1    POINT (1 3)
dtype: GeoDtype
```

#### Initializing from WKB format data

You can put multiple string data in WKB format into a list, numpy.ndarray, or pandas.Series, and then pass them to the GeoSeries constructor to create GeoSeries objects.
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

GeoSeries implements common operations on geometries (unary operations and binary operations).

* When performing a unary operation on a GeoSeries object, Arctern performs the operation on all the geometries stored in the GeoSeries object.
* When performing binary operations on two GeoSeries objects, Arctern performs one-to-one operations on each geometry in the two GeoSeries objects according to the index.
* When performing a binary operation on a GeoSeries object and a geometry (object in WKB format), Arctern performs an operation on each geometry in the GeoSeries object and this geometry.

If the result of the operation is geometric data, a new GeoSeries object is returned; otherwise a Pandas Series object is returned.

The following lists some of the GeoSeries methods, including operations on geometric measurement, relationship operation, and geometric conversion. For detailed information of APIs, please see [API Reference](../../api_reference/standalone_api/geoseries.html).

#### Geometric measurement  

- **[GeoSeries.is_valid](../../api_reference/standalone_api/api/arctern.GeoSeries.is_valid.html):** Tests whether each geometry in the GeoSeries is in valid format, such as WKT and WKB formats.
- **[GeoSeries.area](../../api_reference/standalone_api/api/arctern.GeoSeries.area.html):** Calculates the 2D Cartesian (planar) area of each geometry in the GeoSeries.
- **[GeoSeries.distance](../../api_reference/standalone_api/api/arctern.GeoSeries.distance.html):** For each geometry in the GeoSeries and the corresponding geometry given in `other`, calculates the minimum 2D Cartesian (planar) distance between them.
- **[GeoSeries.distance_sphere](../../api_reference/standalone_api/api/arctern.GeoSeries.distance_sphere.html):** For each point in the GeoSeries and the corresponding point given in `other`, calculates the minimum spherical distance between them.
- **[GeoSeries.hausdorff_distance](../../api_reference/standalone_api/api/arctern.GeoSeries.hausdorff_distance.html):** For each point in the GeoSeries and the corresponding point given in `other`, calculates the Hausdorff distance between them.

#### Geometric relationship operation

- **[GeoSeries.touches](../../api_reference/standalone_api/api/arctern.GeoSeries.touches.html):** For each geometry in the GeoSeries and the corresponding geometry given in `other`, tests whether the first geometry touches the other.
- **[GeoSeries.overlaps](../../api_reference/standalone_api/api/arctern.GeoSeries.overlaps.html):** For each geometry in the GeoSeries and the corresponding geometry given in `other`, tests whether the first geometry "spatially overlaps" the other.
- **[GeoSeries.intersects](../../api_reference/standalone_api/api/arctern.GeoSeries.intersects.html):** For each geometry in the GeoSeries and the corresponding geometry given in `other`, tests whether they intersect each other.

#### Geometric conversion

- **[GeoSeries.precision_reduce](../../api_reference/standalone_api/api/arctern.GeoSeries.precision_reduce.html):** For the coordinates of each geometry in the GeoSeries, reduces the number of significant digits to the given number.
- **[GeoSeries.make_valid](../../api_reference/standalone_api/api/arctern.GeoSeries.make_valid.html):** Creates a valid representation of each geometry in the GeoSeries without losing any of the input vertices.
- **[GeoSeries.curve_to_line](../../api_reference/standalone_api/api/arctern.GeoSeries.curve_to_line.html):** Converts curves in each geometry to approximate linear representation.


