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

# local
import jedec
import gal22v10

#--------------------------------------------------------------------
# Private
#--------------------------------------------------------------------

#--------------------------------------------------------------------
# Public - Main
#--------------------------------------------------------------------

if __name__ == '__main__':

    jedec_file = sys.argv[1]
    pin_names = sys.argv[2].split(' ')

    # Load the fuse data
    jedec = jedec.Jedec()
    jedec.load(jedec_file)

    # Our PLD
    pld = gal22v10.Gal22v10(pin_names)
    pld.print_terms(jedec.fuse_data)
