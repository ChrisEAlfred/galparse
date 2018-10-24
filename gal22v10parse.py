#--------------------------------------------------------------------
# Module        :   gal22v10parse
# Description   :   Parse a GAL22V10 JEDEC file
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
import os

# local
import jedec
import gal22v10
import cupl

#--------------------------------------------------------------------
# Private
#--------------------------------------------------------------------

#--------------------------------------------------------------------
# Public - Main
#--------------------------------------------------------------------

if __name__ == '__main__':

    jedec_file = sys.argv[1]
    pin_names = sys.argv[2].split(' ')
    name = sys.argv[3]
    revision = sys.argv[4]
    designer = sys.argv[5]
    company = sys.argv[6]
    assembly = sys.argv[7]
    location = sys.argv[8]

    # Load the fuse data
    jedec = jedec.Jedec()
    jedec.load(jedec_file)

    # Our PLD
    pld = gal22v10.Gal22v10(pin_names)

    # CUPL
    cupl = cupl.Cupl()
    cupl.create_source(pld, jedec.fuse_data, name, revision, designer, company, assembly, location)
