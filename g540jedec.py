#--------------------------------------------------------------------
# Module        :   g540jedec
# Description   :   Convert .jed to G540 jed
# Caveats       :
# Author        :   Chris Alfred
# Copyright (c) 2018 Chris Alfred
#--------------------------------------------------------------------

#--------------------------------------------------------------------
# Imports
#--------------------------------------------------------------------

# System
import sys
import time

# local
import jedec
import g540

GAL22V10_FUSES_PER_LINE = 44

#--------------------------------------------------------------------
# Private
#--------------------------------------------------------------------

_fuse_data = []

#--------------------------------------------------------------------
# Public - Main
#--------------------------------------------------------------------

if __name__ == '__main__':

    jedec_file = sys.argv[1]
    jedec_out_file = sys.argv[2]

    # Read in JEDEC
    jedec = jedec.Jedec()
    jedec.debug = True
    jedec.load(jedec_file)

    # Convert to G540 format

    prog = g540.g540()
    prog.build_jedec(jedec_file, jedec.number_of_pins, jedec.fuse_data, jedec.checksum, GAL22V10_FUSES_PER_LINE, jedec_out_file)
