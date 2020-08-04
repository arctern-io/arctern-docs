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
# Plot icon visualization
# Download icon-viz.png :  https://raw.githubusercontent.com/arctern-io/arctern-docs/master/img/icon/icon-viz.png
# Uncomment the line below to download the icon image
# os.system('wget "https://raw.githubusercontent.com/arctern-io/arctern-docs/master/img/icon/icon-viz.png"')
fig, ax = plt.subplots(figsize=(10, 6), dpi=200) # doctest: +SKIP
arctern.plot.iconviz(ax, points, bounding_box=[-74.01424568752932, 40.72759334104623, -73.96056823889673, 40.76721122683304], icon_path='icon-viz.png', coordinate_system='EPSG:4326') # doctest: +SKIP
plt.show() # doctest: +SKIP
