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
points = arctern.GeoSeries.point(df['longitude'], df['latitude']) # doctest: +SKIP
# >>>
# render fishnet
fig, ax = plt.subplots(figsize=(10, 6), dpi=200) # doctest: +SKIP
arctern.plot.fishnetmap(ax, points=points, weights=df['color_weights'], bounding_box=[-74.01424568752932, 40.72759334104623, -73.96056823889673, 40.76721122683304], cell_size=8, cell_spacing=2, opacity=1.0, coordinate_system="EPSG:4326") # doctest: +SKIP
plt.show() # doctest: +SKIP
