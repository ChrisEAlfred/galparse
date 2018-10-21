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
    MACROCELL_COUNT = 10
    MACROCELL_OR_TERMS = [
        8, 10, 12, 14, 16, 16, 14 ,12, 10, 8
    ]
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

    def _build_macrocells(self, fuse_data):

        self.macrocells = []
        self.macrocells.append(macrocell.Macrocell('AR',1))

        for macrocell_index in range(self.MACROCELL_COUNT):

            # Assume simple name
            pin_prefix = ''
            pin_name = self.pin_names[21 - macrocell_index]
            pin_suffix = ''

            # Determine the macrocell output mode
            fuse_index = 5808 + 2 * macrocell_index
            if fuse_data[fuse_index+0] == '0' and fuse_data[fuse_index+1] == '0':
                # Active low latched output
                pin_prefix = '!'
                pin_suffix = '.d'
            elif fuse_data[fuse_index+0] == '1' and fuse_data[fuse_index+1] == '0':
                # Active high latched output
                pin_suffix = '.d'
            elif fuse_data[fuse_index+0] == '0' and fuse_data[fuse_index+1] == '1':
                # Active low output
                pin_prefix = '!'
            else:
                # Active high output
                pass
            self.macrocells.append(macrocell.Macrocell(pin_prefix + pin_name+'.oe', 1))
            self.macrocells.append(macrocell.Macrocell(pin_prefix + pin_name + pin_suffix, self.MACROCELL_OR_TERMS[macrocell_index]))

        self.macrocells.append(macrocell.Macrocell('SP',1))


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
            self.fuserow.append( column[1] + self.pin_names[ column[0] ] )

    def print_terms(self, fuse_data):

        """
        Print logic terms
        fuse_data: array of fuses as '0' or '1'
        """

        # Build the macrocells
        self._build_macrocells(fuse_data)

        # Get the device fuse row
        number_of_and_terms = len(self.fuserow)

        # Loop over the macrocells
        fuse_index = 0
        for mc in self.macrocells:

            # Loop over the number of OR terms
            for or_term in range(mc.number_of_or_terms):

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
                            s = '0'
                            break

                    # Include non-fused terms
                    if x == '0': # '0' is NOT fused
                        if index != 0 and terms != 0:
                            s = s + ' & '
                        s = s + self.fuserow[index]
                        terms = terms + 1

                    prev_term = x
                    index = index + 1

                # If there are no terms the value is True ('1')
                if terms == 0:
                    s = '1'

                if or_term == 0:
                    # The first line must be printed
                    s = mc.name + ' = ' + s
                    print(s)
                elif terms != 0 and s != '0':
                    s = ' ' * len(mc.name) + ' # ' + s
                    print(s)

                fuse_index = fuse_index + number_of_and_terms
