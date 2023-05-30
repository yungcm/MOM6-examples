### ISOMIP float

0. Symmetrize the Ocean1 ice shelf using symmetrize_ocean1()

1. Create new shelf file "INPUT/shelfX.nc" using make_shelf_half_as_massive() based on symmetrized Ocean1

2. Do a short run with THICKNESS_CONFIG = "ISOMIP"

3. Make thickness file "INPUT/thickness.nc" using make_thickness_file()

4. Do a proper run with THICKNESS_CONFIG = "thickness_file", as well as
   + #override THICKNESS_FILE = "thickness.nc"
   + #override REMAP_AFTER_INITIALIZATION = False
   + #override HACK_MODE = True
