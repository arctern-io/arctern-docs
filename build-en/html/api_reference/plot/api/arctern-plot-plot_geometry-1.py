import pandas
import matplotlib.pyplot as plt
import arctern
raw_data = []
raw_data.append('point(0 0)')
raw_data.append('linestring(0 10, 5 5, 10 0)')
raw_data.append('polygon((2 2,2 3,3 3,3 2,2 2))')
raw_data.append("GEOMETRYCOLLECTION("
                "polygon((1 1,1 2,2 2,2 1,1 1)),"
                "linestring(0 1, 5 6, 10 11),"
                "POINT(4 7))")
arr_wkt = pandas.Series(raw_data)
arr_wkb = (arctern.GeoSeries(arr_wkt)).curve_to_line()
df = pandas.DataFrame({'wkb':arr_wkb})
fig, ax = plt.subplots()
arctern.plot.plot_geometry(ax, df,
                           color=['orange', 'green', 'blue', 'red'],
                           marker='^',
                           markersize=100,
                           linewidth=[None, 7, 8, 5],
                           linestyle=[None, 'dashed', 'dashdot', None],
                           edgecolor=[None, None, 'red', None],
                           facecolor=[None, None, 'black', None])
ax.grid()
fig.savefig('/tmp/plot_test.png')
plt.show()
