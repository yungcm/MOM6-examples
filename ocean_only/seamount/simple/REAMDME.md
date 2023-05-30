### Simple shelf

1. Create a new shelf file "INPUT/shelfX.nc" using make_shelf()

2. Create a new topography file "INPUT/topogX.nc" using make_topography()

2. Do a short run with THICKNESS_CONFIG = "ISOMIP" in MOM_override

3. Make thickness file "INPUT/thickness.nc" using make_thickness_file()

4. Do a proper run with THICKNESS_CONFIG = "thickness_file", also
   + #override THICKNESS_FILE = "thickness.nc"
   + #override REMAP_AFTER_INITIALIZATION = False
   + #override HACK_MODE = True
