from tools.structs import staticValues

class CompileDong():
    '''
    Method for compiling all dongle information into formats that we want
    so that we can write the whole thing to a file.
    '''
    def makeWhiteDong(pcbid:str):
        '''
        Function for generating a white eAmusement dongle.
        Doesn't need an mcode.

        Here's the white dongle structure:
        - type (1)
        - signing key
        - pcbid
        '''
        # Create an empty dongle
        whitedong = []

        # Append the type
        whitedong.append(staticValues.key_type_white)

        # Add the signing key
        whitedong.append(staticValues.security_key_white)

        # Add the PCBID
        whitedong.append(pcbid)

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
        # Start with an empty array
        blackdong = []

        # Write the dongle type
        blackdong.append(staticValues.key_type_black)

        # Write the signing key
        blackdong.append(key)

        # Write the mcode
        for code in mcode:
            blackdong.append(code)
        
        # Write the PCBID
        blackdong.append(pcbid)

        # Send it back to who asked for it
        return blackdong
