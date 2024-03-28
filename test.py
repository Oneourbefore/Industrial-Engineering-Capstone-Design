import matplotlib.pyplot as plt
import cartopy.crs as ccrs

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_extent([124, 132, 33, 43], crs=ccrs.PlateCarree())

ax.plot(127.76, 36.48, 'bo', markersize=10, transform=ccrs.Geodetic())
ax.coastlines()

plt.show()
