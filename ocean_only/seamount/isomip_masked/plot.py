import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
import xarray as xr

di = '/home/claire/Github-forked/MOM6-examples/ocean_only/seamount/isomip_masked'

IC_FILE = 'MOM_IC.nc'
SHELF_IC_FILE = 'MOM_Shelf_IC.nc'
PROG_FILE = 'prog.nc'

ic = xr.open_dataset(di + "/"+ IC_FILE)
ms = xr.open_dataset(di + "/" + SHELF_IC_FILE)
prog = xr.open_dataset(di + "/" + PROG_FILE) # need this as land mask info not in ic or ms

LY, LX = ic.h.data[0].shape[1], ic.h.data[0].shape[2]
YY= np.arange(0, LY, 1)
XX = np.arange(0, LX, 1)
XX, YY = np.meshgrid(XX, YY)

fig, axes = plt.subplots(subplot_kw={"projection": "3d"})

eta = ic.eta[0].data[0]
bathyT = eta - np.sum(ic.h[0].data, axis=0)

mask = np.isnan(prog.h[0][0].data)
eta[mask]=np.nan
bathyT[mask]=np.nan

axes.plot_surface(XX, YY, eta)
axes.plot_surface(XX, YY, bathyT)

plt.show()

