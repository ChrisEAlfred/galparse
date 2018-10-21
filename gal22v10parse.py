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

def PrintTerms(pld, fusedata):

    fuse_index = 0

    # Get the device fuse row
    fuserow = pld.fuserow
    number_of_and_terms = len(fuserow)

    # Loop over the macrocells
    for macrocell in pld.macrocells:

        title = macrocell.name
        number_of_or_terms = macrocell.number_of_or_terms

        # Loop over the number of OR terms
        for or_term in range(number_of_or_terms):

            # Get the AND fuse data for this OR term
            data = fusedata[fuse_index:fuse_index+number_of_and_terms]

            # Initialise output line for this data
            s = ''

            # Loop over the OR fuses
            index = 0
            terms = 0
            prev_term = '0'
            for x in data:

                # Two sequential terms X & !X with intact fuses will be 0
                if index & 1 == 1:
                    if x == '0' and prev_term == '0':
                        terms = 0
                        break

                # Include non-fused terms
                if x == '0': # '0' is NOT fused
                    if index != 0 and terms != 0:
                        s = s + ' & '
                    s = s + fuserow[index]
                    terms = terms + 1

                prev_term = x
                index = index + 1

            # If there are no terms the value is False ('0')
            if terms == 0:
                s = '0'

            if or_term == 0:
                # The first line must be printed
                s = title + ' = ' + s
                print(s)
            elif terms != 0:
                s = ' ' * len(title) + ' # ' + s
                print(s)

            fuse_index = fuse_index + number_of_and_terms

#--------------------------------------------------------------------
# Public - Main
#--------------------------------------------------------------------

if __name__ == '__main__':

    jedec_file = sys.argv[1]
    pin_names = sys.argv[2].split(' ')

    # Load the fuse data
    jedec = jedec.Jedec()
    jedec.debug = True
    jedec.load(jedec_file)

    # Our PLD
    pld = gal22v10.Gal22v10(pin_names)

    PrintTerms(pld, jedec.fuse_data)
