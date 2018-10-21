#--------------------------------------------------------------------
# Module        :   gal22v10
# Description   :   gal22v10 PLD implementation
# Caveats       :
# Author        :   Chris Alfred
# Copyright (c) Chris Alfred
#--------------------------------------------------------------------

#--------------------------------------------------------------------
# Imports
#--------------------------------------------------------------------

# local
import macrocell

#--------------------------------------------------------------------
# Class
#--------------------------------------------------------------------

class Gal22v10:

    IO_COUNT = 22
    FUSEROW_MAPPING = [
        # Pin name index    Name prefix
        (0,                 ''),
        (0,                 '!'),
        (21,                ''),
        (21,                '!'),
        (1,                 ''),
        (1,                 '!'),
        (20,                ''),
        (20,                '!'),
        (2,                 ''),
        (2,                 '!'),
        (19,                ''),
        (19,                '!'),
        (3,                 ''),
        (3,                 '!'),
        (18,                ''),
        (18,                '!'),
        (4,                 ''),
        (4,                 '!'),
        (17,                ''),
        (17,                '!'),
        (5,                 ''),
        (5,                 '!'),
        (16,                ''),
        (16,                '!'),
        (6,                 ''),
        (6,                 '!'),
        (15,                ''),
        (15,                '!'),
        (7,                 ''),
        (7,                 '!'),
        (14,                ''),
        (14,                '!'),
        (8,                 ''),
        (8,                 '!'),
        (13,                ''),
        (13,                '!'),
        (9,                 ''),
        (9,                 '!'),
        (12,                ''),
        (12,                '!'),
        (10,                 ''),
        (10,                 '!'),
        (11,                 ''),
        (11,                 '!'),
    ]

    #----------------------------------------------------------------
    # Private
    #----------------------------------------------------------------

    #----------------------------------------------------------------
    # Public
    #----------------------------------------------------------------

    def __init__(self, pin_names):

        # Assign the pin names
        if len(pin_names) != self.IO_COUNT:
            raise ValueError('Incorrect number of pins')
        self.pin_names = pin_names

        # Assign fuse row
        self.fuserow = []
        for column in self.FUSEROW_MAPPING:
            self.fuserow.append( column[1] + pin_names[ column[0] ] )

        # Assign macrocells
        self.macrocells = []
        self.macrocells.append(macrocell.Macrocell('AR',1))
        self.macrocells.append(macrocell.Macrocell(pin_names[21]+'_oe',1))
        self.macrocells.append(macrocell.Macrocell(pin_names[21],8))
        self.macrocells.append(macrocell.Macrocell(pin_names[20]+'_oe',1))
        self.macrocells.append(macrocell.Macrocell(pin_names[20],10))
        self.macrocells.append(macrocell.Macrocell(pin_names[19]+'_oe',1))
        self.macrocells.append(macrocell.Macrocell(pin_names[19],12))
        self.macrocells.append(macrocell.Macrocell(pin_names[18]+'_oe',1))
        self.macrocells.append(macrocell.Macrocell(pin_names[18],14))
        self.macrocells.append(macrocell.Macrocell(pin_names[17]+'_oe',1))
        self.macrocells.append(macrocell.Macrocell(pin_names[17],16))
        self.macrocells.append(macrocell.Macrocell(pin_names[16]+'_oe',1))
        self.macrocells.append(macrocell.Macrocell(pin_names[16],16))
        self.macrocells.append(macrocell.Macrocell(pin_names[15]+'_oe',1))
        self.macrocells.append(macrocell.Macrocell(pin_names[15],14))
        self.macrocells.append(macrocell.Macrocell(pin_names[14]+'_oe',1))
        self.macrocells.append(macrocell.Macrocell(pin_names[14],12))
        self.macrocells.append(macrocell.Macrocell(pin_names[13]+'_oe',1))
        self.macrocells.append(macrocell.Macrocell(pin_names[13],10))
        self.macrocells.append(macrocell.Macrocell(pin_names[12]+'_oe',1))
        self.macrocells.append(macrocell.Macrocell(pin_names[12],8))
        self.macrocells.append(macrocell.Macrocell('SP',1))

    def print_terms(self, fuse_data):

        """
        Print logic terms
        fuse_data: array of fuses as '0' or '1'
        """

        fuse_index = 0

        # Get the device fuse row
        fuserow = self.fuserow
        number_of_and_terms = len(fuserow)

        # Loop over the macrocells
        for macrocell in self.macrocells:

            title = macrocell.name
            number_of_or_terms = macrocell.number_of_or_terms

            # Loop over the number of OR terms
            for or_term in range(number_of_or_terms):

                # Get the AND fuse data for this OR term
                data = fuse_data[fuse_index:fuse_index+number_of_and_terms]

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
