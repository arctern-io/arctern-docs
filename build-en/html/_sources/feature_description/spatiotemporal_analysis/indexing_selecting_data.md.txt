# Indexing and selecting data
This article describes how Arctern GeoSeries index and select data.

## Methods of indexing and selecting data
Arctern GeoSeries inherits the  indexing and data selection methods from pandas Series, including the label-based indexing [`loc`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html) and integer-location based indexing [`iloc`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html). See [pandas documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html) for detailed information about indexing and selecting data.

## Generating test data

1. Create an arctern.GeoSeries object `geos`, which includes three points (POINT) and a polygon (POLYGON), and then index them. 
2. Create a pandas.DataFrame object with `geos` as input.

> **Note:** The row indexes corresponding to a, b, c, and d are 0, 1, 2, and 3.

```python
>>> from arctern import GeoSeries
>>> import pandas as pd
>>> geos = GeoSeries(["POINT (0 1)","POINT (2 3)","POLYGON ((0 0,0 1,1 1,0 0))", "POINT (0 0)"],index=['a','b','c','d'])
>>> df = pd.DataFrame(geos)
```

## Tests

### Testing the loc method

Access all data of `geos`:

```python
>>> geos.loc[:]    
a                    POINT (0 1)
b                    POINT (2 3)
c    POLYGON ((0 0,0 1,1 1,0 0))
d                    POINT (0 0)
dtype: GeoDtype
```

Select the data of `geos` from line `a` to line `c`:

```python
>>> geos.loc['a':'c']
a                    POINT (0 1)
b                    POINT (2 3)
c    POLYGON ((0 0,0 1,1 1,0 0))
dtype: GeoDtype
```

Select the data of `geos` from the first line to line `c`:

```python
>>> geos.loc[:'c']
a                    POINT (0 1)
b                    POINT (2 3)
c    POLYGON ((0 0,0 1,1 1,0 0))
dtype: GeoDtype
```

### Testing the iloc method

Select the data of `geos` from line 1 to line 3 (excluding data in line 3):

```python
>>> geos.iloc[1:3]
b                    POINT (2 3)
c    POLYGON ((0 0,0 1,1 1,0 0))
dtype: GeoDtype
```

Select the data of `df` from line 1 to line 3 (excluding data in line 3):

```python
>>> df.iloc[1:3]
                             0
b                  POINT (2 3)
c  POLYGON ((0 0,0 1,1 1,0 0))
```
