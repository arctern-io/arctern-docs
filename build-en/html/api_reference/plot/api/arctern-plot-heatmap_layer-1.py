import pandas as pd
import numpy as np
import arctern
import matplotlib.pyplot as plt
import io
import base64
# Read from test_data.csv
# Download link: https://raw.githubusercontent.com/arctern-io/arctern-resources/benchmarks/benchmarks/dataset/layer_rendering_test_data/test_data.csv
# Uncomment the lines below to download the test data
# import os
# os.system('wget "https://raw.githubusercontent.com/arctern-io/arctern-resources/benchmarks/benchmarks/dataset/layer_rendering_test_data/test_data.csv"')
df = pd.read_csv(filepath_or_buffer="test_data.csv", dtype={'longitude':np.float64, 'latitude':np.float64, 'color_weights':np.float64, 'size_weights':np.float64, 'region_boundaries':np.object}) # doctest: +SKIP
points = arctern.GeoSeries.point(df['longitude'], df['latitude']) # doctest: +SKIP
# >>>
# Plot heatmap_layer
bbox = [-74.01424568752932, 40.72759334104623, -73.96056823889673, 40.76721122683304]
map_layer = arctern.plot.heatmap_layer(1024, 896, points, df['color_weights'], bounding_box=bbox, coordinate_system='EPSG:4326') # doctest: +SKIP
fig, ax = plt.subplots(figsize=(10, 6), dpi=200) # doctest: +SKIP
f = io.BytesIO(base64.b64decode(map_layer)) # doctest: +SKIP
img = plt.imread(f) # doctest: +SKIP
ax.imshow(img) # doctest: +SKIP
ax.axis('off') # doctest: +SKIP
plt.show() # doctest: +SKIP
