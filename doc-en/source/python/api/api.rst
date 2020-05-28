.. _api:

API
====

.. currentmodule:: arctern

Constructor Functions
---------------------
.. autosummary::
   :toctree: reference/

   ST_Point
   ST_PolygonFromEnvelope
   ST_GeomFromText
   ST_GeomFromGeoJSON
   ST_AsText
   ST_AsGeoJSON


Measurement Functions
---------------------
.. autosummary::
   :toctree: reference/

   ST_DistanceSphere
   ST_Distance
   ST_Area
   ST_Length
   ST_HausdorffDistance

Accessor Functions
------------------
.. autosummary::
   :toctree: reference/

   ST_IsValid
   ST_IsSimple
   ST_GeometryType
   ST_NPoints
   ST_Envelope


Processing Functions
--------------------
.. autosummary::
   :toctree: reference/

   ST_Buffer
   ST_PrecisionReduce
   ST_Intersection
   ST_MakeValid
   ST_SimplifyPreserveTopology
   ST_Centroid
   ST_ConvexHull
   ST_Transform
   ST_CurveToLine

Aggregate Functions
---------------------
.. autosummary::
   :toctree: reference/

   ST_Union_Aggr
   ST_Envelope_Aggr