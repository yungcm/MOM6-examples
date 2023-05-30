### ISOMIP float

1. Make a symmetric version of the Ocean1 ice shelf in "/INPUT/shelfX.nc" using symmetrize_ocean1()

2. Do a short run with THICKNESS_CONFIG = "ISOMIP"

3. Make thickness file "INPUT/thickness.nc" using make_thickness_file()

4. Do a proper run with THICKNESS_CONFIG = "thickness_file", as well as
   + #override THICKNESS_FILE = "thickness.nc"
   + #override REMAP_AFTER_INITIALIZATION = False
   + #override HACK_MODE = True
