from tools.structs import staticValues
from tools.encoding import securityEncoding

class CompileDong():
    '''
    Method for compiling all dongle information into formats that we want
    so that we can write the whole thing to a file.
    '''
    def makeWhiteDong(pcbid:str, mcode:str):
        '''
        Function for generating a white eAmusement dongle.

        Here's the white dongle structure:
        - type (1)
        - signing key
        - mcode
        - pcbid
        '''
        # Values
        sign_key_temp = [0]*8
        pcbid_temp = [0]*8

        # Init sign_key_temp with the sign key
        keyasbytes = staticValues.security_key_white.encode('utf-8')
        for index, item in enumerate(sign_key_temp):
            sign_key_temp[index] = item ^ keyasbytes[index]

        # Pack the sign key
        packedsignkey = securityEncoding.encode_8_to_6(sign_key_temp)

        # Encode the given PCBID into binary data
        pcbid_encode = bytes(pcbid, encoding=('utf-8'))

        # Reverse the PCBID
        for index, item in enumerate(pcbid_temp):
            pcbid_temp[index] = item ^ pcbid_encode[index]

        # Pack the mcode
        mcodestr = ""
        for byte in mcode:
            mcodestr = mcodestr+byte
        packed_payload = securityEncoding.encode_8_to_6(mcodestr.encode('utf-8'))
        
        # Generate the signature
        signature = securityEncoding.create_signature(pcbid_temp[::-1], packedsignkey)

        ## Now that we have compiled all of the data, we should go ahead and populate
        ## an array with it, and send it off.
        
        # Generate an array
        whitedong = []

        # Append the PCBID
        for i in pcbid_temp:
            whitedong.append(i)

        # Append the signature
        for i in signature:
            whitedong.append(i)

        # Append the payload
        for i in packed_payload:
            whitedong.append(i)

        # Append 19 empty spaces
        for i in range(19):
            whitedong.append(0x00)

        # Lastly, we need the CRC of the data.
        whitedong.append(securityEncoding.get_CRC8(whitedong[8:]))

        # Send it back to who asked for it
        return whitedong

    def makeBlackDong(key:str, mcode:list, pcbid):
        '''
        Function for generating a black security dongle.

        Here's the proper data structure:
        - type (0)
        - signing key (game specific)
        - mcode (game specific)
        - pcbid
        '''
        # Values
        sign_key_temp = [0]*8
        pcbid_temp = [0]*8

        # Init sign_key_temp with the sign key so we can sign the mcode
        keyasbytes = key.encode('utf-8')
        for index, item in enumerate(sign_key_temp):
            sign_key_temp[index] = item ^ keyasbytes[index]

        # Convert the mcode into a string so we can sign it
        mcodestr = ""
        for code in mcode:
            mcodestr = mcodestr+code

        # Convert the mcode into a byte array
        mcodebit = mcodestr.encode('utf-8')

        # Sign the mcode
        for index, item in enumerate(sign_key_temp):
            sign_key_temp[index] = item ^ mcodebit[index]

        # Pack the sign key
        packedsignkey = securityEncoding.encode_8_to_6(sign_key_temp)

        # Encode the given PCBID into binary data
        pcbid_encode = bytes(pcbid, encoding=('utf-8'))

        # List the PCBID
        for index, item in enumerate(pcbid_temp):
            pcbid_temp[index] = item ^ pcbid_encode[index]

        # Pack the mcode
        packed_payload = securityEncoding.encode_8_to_6(mcodebit)
        
        # Generate the signature
        signature = securityEncoding.create_signature(pcbid_temp[::-1], packedsignkey)

        ## Now that we have compiled all of the data, we should go ahead and populate
        ## an array with it, and send it off.
        
        # Generate an array
        blackdong = []

        # Append the PCBID
        for i in pcbid_temp:
            blackdong.append(i)

        # Append the signature
        for i in signature:
            blackdong.append(i)

        # Append the payload
        for i in packed_payload:
            blackdong.append(i)

        # Append 19 empty spaces
        for i in range(19):
            blackdong.append(0x00)

        # Lastly, add the CRC.
        blackdong.append(securityEncoding.get_CRC8(blackdong[8:]))

        # Send it back to who asked for it
        return blackdong
