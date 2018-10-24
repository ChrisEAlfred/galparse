#--------------------------------------------------------------------
# Module        :   cupl
# Description   :   CUPL support
# Caveats       :
# Author        :   Chris Alfred
# Copyright (c) Chris Alfred
#--------------------------------------------------------------------

#--------------------------------------------------------------------
# Imports
#--------------------------------------------------------------------

import datetime

# local

#--------------------------------------------------------------------
# Class
#--------------------------------------------------------------------

class Cupl:

    #----------------------------------------------------------------
    # Private
    #----------------------------------------------------------------

    #----------------------------------------------------------------
    # Public
    #----------------------------------------------------------------

    def __init__(self):
        pass

    def create_source(self, pld, fuse_data, name, revision, designer, company, assembly, location):

        # Header

        print('Name         ' + name + ' ;')
        print('Partno       ' + name + ' ;')
        print('Date         ' + datetime.datetime.now().strftime("%d/%m/%Y") + ' ;')
        print('Revision     ' + revision + ' ;')
        print('Designer     ' + designer + ' ;')
        print('Company      ' + company + ' ;')
        print('Assembly     ' + assembly + ' ;')
        print('Location     ' + location + ' ;')
        print('Device       ' + pld.device_name + ' ;')

        print('')

        # Pin list
        print('/*----------------------------------------------------------------------*/')
        print('')
        pin_number = 1
        for pin_name in pld.pin_names:
            print('Pin ' + str(pin_number) + ' = ' + pin_name + ';')
            pin_number = pin_number + 1
            if pin_number == 12:
                pin_number = pin_number + 1
        print('')

        print('/*----------------------------------------------------------------------*/')
        print('')

        pld.print_terms(fuse_data)
