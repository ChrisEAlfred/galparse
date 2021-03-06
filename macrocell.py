#--------------------------------------------------------------------
# Module        :   macrocell
# Description   :   macrocell descriptor
# Caveats       :
# Author        :   Chris Alfred
# Copyright (c) Chris Alfred
#--------------------------------------------------------------------

#--------------------------------------------------------------------
# Imports
#--------------------------------------------------------------------

#--------------------------------------------------------------------
# Class
#--------------------------------------------------------------------

class Macrocell:

    def __init__(self, name, number_of_or_terms, oe = False):
        self.name = name
        self.number_of_or_terms = number_of_or_terms
        self.oe = oe