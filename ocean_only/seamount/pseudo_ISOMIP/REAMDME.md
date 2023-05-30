### Pseudo ISOMIP

1. Create new shelf file "INPUT/shelfX.n" using make_shelf()

2. Do a short run with THICKNESS_CONFIG = "ISOMIP"

3. Make thickness file "INPUT/thickness.nc" using make_thickness_file()

4. Do a proper run with THICKNESS_CONFIG = "thickness_file", as well as
   + #override THICKNESS_FILE = "thickness.nc"
   + #override REMAP_AFTER_INITIALIZATION = False
   + #override HACK_MODE = True
