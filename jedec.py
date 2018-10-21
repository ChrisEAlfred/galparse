#--------------------------------------------------------------------
# Module        :   jedec
# Description   :   JEDEC file parsing
# Caveats       :
# Author        :   Chris Alfred
# Copyright (c) Chris Alfred
#
# Notes
#   JEDEC fuses
#       '0' = not fused (i.e. connected)
#       '1' = not fused (i.e. disconnected)
#--------------------------------------------------------------------

#--------------------------------------------------------------------
# Imports
#--------------------------------------------------------------------

#--------------------------------------------------------------------
# Class
#--------------------------------------------------------------------

class Jedec:

    def __init__(self):
        self._header_lines = []
        self.fuse_data = [0] * 0
        self.number_of_pins = 0
        self.number_of_fuses = 0
        self.checksum = '0000'
        self.debug = False

    #----------------------------------------------------------------
    # Private
    #----------------------------------------------------------------

    #----------------------------------------------------------------
    # Public
    #----------------------------------------------------------------

    def load(self, file):

        got_asterisk = False
        in_header = True
        fuse_number = 0
        try:
            fp = open(file, 'r')
            for line in fp:

                # Strip CRLF and trailing spaces
                line = line.rstrip()

                # Remove leading * if present
                if line.startswith('*'):
                    if not got_asterisk:
                        got_asterisk = True
                        in_header = False
                    line = line[1:]

                # Remove trailing * if present
                if line.endswith('*'):
                    got_asterisk = True
                    line = line[:-1]

                words = line.split()

                if in_header:

                    # This is a header line
                    if self.debug:
                        print("Header: " + line)
                    self._header_lines.append(line)

                    if got_asterisk:
                        if self.debug:
                            print("[End of header]")
                        in_header = False


                if not in_header:

                    # Check keywords
                    if words[0].startswith('QP'):
                        # Number of pins
                        self.number_of_pins = int(words[0][2:])
                        if self.debug:
                            print('[Pins {}]'.format(self.number_of_pins))

                    elif words[0].startswith('QF'):
                        # Number of fuses
                        self.number_of_fuses = int(words[0][2:])
                        if self.debug:
                            print('[Fuses {}]'.format(self.number_of_fuses))

                        # Initialise data array to unfused
                        self.fuse_data = ['0'] * self.number_of_fuses

                    elif words[0].startswith('C'):
                        # Checksum
                        self.checksum = words[0][1:]
                        if self.debug:
                            print('[Checksum {}]'.format(self.checksum))

                    elif words[0].startswith('L'):
                        # Fuse index header line
                        fuse_number = int(words[0][1:])
                        if self.debug:
                            print('[Fuse {}]'.format(fuse_number))

                        # There may also be fuse data
                        if len(words) == 2:
                            data = words[1]
                            if self.debug:
                                print('{:04d}: {}'.format(fuse_number, data))

                            # Copy fuse data to array
                            for v in data:
                                self.fuse_data[fuse_number] = v
                                fuse_number = fuse_number + 1


                    elif words[0].startswith('0') or words[0].startswith('1'):
                        # Fuse data on line by self
                        data = words[0]
                        if self.debug:
                            print('{:04d}: {}'.format(fuse_number, data))

                        # Copy fuse data to array
                        for v in data:
                            self.fuse_data[fuse_number] = v
                            fuse_number = fuse_number + 1

                    else:
                        pass

        finally:
            fp.close()
        
        return
