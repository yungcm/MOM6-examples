#############################################################
#
# Automates the two-step process of the hack
#
# Files to modify if you change config:
#       inp.txt    (seed file for input.nml)
#       MOM_ov0    (seed file for MOM_override)
#       diag_table (maybe..)
#    
# Careful: thickness file filename is hardcoded in MOM_ovL 
#          and make_thickness_file.py
#
#############################################################
#/bin/bash

sed 's/days = X/days = 0/' < inp.txt > input.nml       # run for 0 days & 1 hour

cat MOM_ov0 MOM_ovS > MOM_override                     # THICKNESS_CONFIG = "ISOMIP"

mpirun -n 2 ../../../build/ocean_only/MOM6

python3 make_thickness_file.py                        # Careful!! thickness filename hardcoded in python script

sed 's/days = X/days = 1/' < inp.txt > input.nml      # run for 1 day and 1 hour

cat MOM_ov0 MOM_ovL > MOM_override                    # THICKNESS_CONFIG = "thickness_file"

mpirun -n 2 ../../../build/ocean_only/MOM6

