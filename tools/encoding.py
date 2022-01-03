import hashlib

from tools.structs import staticValues

class securityEncoding():
    '''
    Class for all of the weird funky encodings.
    Will let you encode and decode security keys.
    '''
    def encode_8_to_6(input:list):
        '''
        Encodes an 8bit array into a 6 bit one.
        '''
        out = [0]*6
        tmp = [0]*8

        # Init the temp with data that was sent
        for i in range(8):
            tmp[i] = (input[i] - 0x20) & 0x3F

        # Start the funky shit
        out[0] = (tmp[0] >> 0) | (tmp[1] << 6)
        out[1] = (tmp[1] >> 2) | (tmp[2] << 4)
        out[2] = (tmp[2] >> 4) | (tmp[3] << 2)

        out[3] = (tmp[4] >> 0) | (tmp[5] << 6)
        out[4] = (tmp[5] >> 2) | (tmp[6] << 4)
        out[5] = (tmp[6] >> 4) | (tmp[7] << 2)

        return out

    def create_signature(pcbid:list, packed_key:list):
        '''
        Creates a signature for the dongle using the reversed 
        PCBID and the packed key.
        '''
        # Create an empty data array
        data = []
        md5 = [0]*16
        buffer = [0]*18

        # Append the pcbid
        for i in pcbid:
            data.append(i)

        # Append the signing key
        for i in packed_key:
            data.append(i)

        # Make the data a proper string for hashlib 
        strdata = ""
        for i in data:
            strdata = strdata + str(i)

        # Create the MD5
        md5hash = hashlib.md5(strdata.encode('utf-8'))
        md5hash = md5hash.digest()
        
        # Add it to the md5 array
        for index, item in enumerate(md5):
            md5[index] = item ^ md5hash[index]

        # Now, we populate the buffer data and scramble the MD5
        for i in range(16):
            buffer[i] = md5[staticValues.scramble_table[i]]

        # Add in the last two bytes, which are static
        buffer[16] = 0xDE
        buffer[17] = 0xAD
        ## And with that, we have a final buffer!

        # Now, we just need to shrink it down to 6 bytes, and then return it!
        output = [0]*6
        for i in range(6):
            output[i] = buffer[i+12] ^ buffer[i+6] ^ buffer[i]
        
        return output