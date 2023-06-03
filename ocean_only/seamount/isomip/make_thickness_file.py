import xarray as xr
import netCDF4 as nc

di = '/home/claire/Github-forked/MOM6-examples/ocean_only/seamount/isomip'

IC_FILE = 'MOM_IC.nc'
THICKNESS_FILE = '/INPUT/thickness.nc'

### new thickness file for THICKNESS_CONFIG="thickness_file"
### (depends on MOM6 output in IC_FILE, ie. use after a run)
def make_thickness_file(filename):
    
    print(filename)
    ic = xr.open_dataset(di + '/' + IC_FILE)
    _, nz, ny, nx = ic.h.data.shape

    new_thick = nc.Dataset(filename, "w", format="NETCDF4")
    new_thick.createDimension("nz", nz)
    new_thick.createDimension("ny", ny)
    new_thick.createDimension("nx", nx)
    new_thick.createVariable("h","f8",("nz","ny","nx"))

    new_thick["h"][:,:,:] = ic.h.data
    new_thick.close()

def main():
    make_thickness_file(di + THICKNESS_FILE)

if __name__ == "__main__":
    main()
