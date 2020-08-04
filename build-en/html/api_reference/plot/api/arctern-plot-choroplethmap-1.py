import pandas as pd
import numpy as np
import arctern
import matplotlib.pyplot as plt
# >>>
# Read from test_data.csv
# Download link: https://raw.githubusercontent.com/arctern-io/arctern-resources/benchmarks/benchmarks/dataset/layer_rendering_test_data/test_data.csv
# Uncomment the lines below to download the test data
# import os
# os.system('wget "https://raw.githubusercontent.com/arctern-io/arctern-resources/benchmarks/benchmarks/dataset/layer_rendering_test_data/test_data.csv"')
df = pd.read_csv(filepath_or_buffer="test_data.csv", dtype={'longitude':np.float64, 'latitude':np.float64, 'color_weights':np.float64, 'size_weights':np.float64, 'region_boundaries':np.object}) # doctest: +SKIP
input = df[pd.notna(df['region_boundaries'])].groupby(['region_boundaries']).mean().reset_index() # doctest: +SKIP
polygon = arctern.GeoSeries(input['region_boundaries']) # doctest: +SKIP
# >>>
# Plot choroplethmap
fig, ax = plt.subplots(figsize=(10, 6), dpi=200) # doctest: +SKIP
arctern.plot.choroplethmap(ax, polygon, input['color_weights'], bounding_box=[-74.01124953254566,40.73413446570038,-73.96238859103838,40.766161712662296], color_gradient=["#115f9a","#d0f400"], color_bound=[5,18], opacity=1.0, coordinate_system='EPSG:4326', aggregation_type="mean") # doctest: +SKIP
plt.show() # doctest: +SKIP
