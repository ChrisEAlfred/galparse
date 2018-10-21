#--------------------------------------------------------------------
# Module        :   g540
# Description   :   G540 programmer routines
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

class g540:

    def __init__(self):
        pass

    #----------------------------------------------------------------
    # Private
    #----------------------------------------------------------------

    #----------------------------------------------------------------
    # Public
    #----------------------------------------------------------------

    def build_jedec(self, title, number_of_pins, fuse_data, checksum, data_per_line, file):

        try:
            fp = open(file, 'w')

            s = 'TITL:\t' + title + '*\n'
            fp.write(s)

            s = 'QP' + str(number_of_pins) + '*\n'
            fp.write(s)

            s = 'QF' + str(len(fuse_data)) + '*\n'
            fp.write(s)

            s = 'L0000\n'
            fp.write(s)

            line_pos = 0
            for i in range(len(fuse_data)):
                if line_pos == 0:
                    s = ''
                s = s + fuse_data[i]
                line_pos = line_pos + 1
                if line_pos == data_per_line:
                    line_pos = 0
                    if i == len(fuse_data)-1:
                        fp.write(s + '*\n')
                    else:
                        fp.write(s + '\n')
            if line_pos != 0:
                fp.write(s + '*\n')

            s = 'C' + checksum + '*\n'
            fp.write(s)

        finally:
            fp.close()
