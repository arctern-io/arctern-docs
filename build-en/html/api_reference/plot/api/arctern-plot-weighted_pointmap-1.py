import pandas as pd
import numpy as np
import arctern
import matplotlib.pyplot as plt
# >>>
# Read from test.csv
# Download link: https://raw.githubusercontent.com/arctern-io/arctern-resources/benchmarks/benchmarks/dataset/layer_rendering_test_data/test_data.csv
# Uncomment the lines below to download the test data
# import os
# os.system('wget "https://raw.githubusercontent.com/arctern-io/arctern-resources/benchmarks/benchmarks/dataset/layer_rendering_test_data/test_data.csv"')
df = pd.read_csv(filepath_or_buffer="test_data.csv", dtype={'longitude':np.float64, 'latitude':np.float64, 'color_weights':np.float64, 'size_weights':np.float64, 'region_boundaries':np.object}) # doctest: +SKIP
points = arctern.GeoSeries.point(df['longitude'], df['latitude']) # doctest: +SKIP
# >>>
# Plot weighted pointmap with variable color and fixed size
fig, ax = plt.subplots(figsize=(10, 6), dpi=200) # doctest: +SKIP
arctern.plot.weighted_pointmap(ax, points, color_weights=df['color_weights'], bounding_box=[-73.99668712186558,40.72972339069935,-73.99045479584949,40.7345193345495], color_gradient=["#115f9a", "#d0f400"], color_bound=[2.5,15], size_bound=[16], opacity=1.0, coordinate_system="EPSG:4326") # doctest: +SKIP
plt.show() # doctest: +SKIP
# >>>
# Plot weighted pointmap with fixed color and variable size
fig, ax = plt.subplots(figsize=(10, 6), dpi=200) # doctest: +SKIP
arctern.plot.weighted_pointmap(ax, points, size_weights=df['size_weights'], bounding_box=[-73.99668712186558,40.72972339069935,-73.99045479584949,40.7345193345495], color_gradient=["#37A2DA"], size_bound=[15, 50], opacity=1.0, coordinate_system="EPSG:4326") # doctest: +SKIP
plt.show() # doctest: +SKIP
# >>>
# Plot weighted pointmap with variable color and size
fig, ax = plt.subplots(figsize=(10, 6), dpi=200) # doctest: +SKIP
arctern.plot.weighted_pointmap(ax, points, color_weights=df['color_weights'], size_weights=df['size_weights'], bounding_box=[-73.99668712186558,40.72972339069935,-73.99045479584949,40.7345193345495], color_gradient=["#115f9a", "#d0f400"], color_bound=[2.5,15], size_bound=[15, 50], opacity=1.0, coordinate_system="EPSG:4326") # doctest: +SKIP
plt.show() # doctest: +SKIP
