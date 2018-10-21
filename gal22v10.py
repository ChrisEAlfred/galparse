#--------------------------------------------------------------------
# Module        :   gal22v10
# Description   :   gal22v10 implementation
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
