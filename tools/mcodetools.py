from tools.structs import staticValues, mcodeStructs

class mcodeTools():
    '''
    Set of tools for verifying, making, and other things for mcodes.
    '''
    def makeMcode(game:str, version:str, region:str):
        '''
        Tool to generate an Mcode that the game will enjoy. These are game specific!
        To make a successful mcode, we need the following items.
        - Header
        - The unknown value
        - The game code
        - The region
        - The cabinet
        - The revision
        '''
        # Let's start the mcode as an array.
        # We'll append values to it as we go.
        finalmcode = []

        # Get the static header
        header = staticValues.mcode_header
        finalmcode.append(header)

        version = int(version)
        # Now, for the rest of the values, we need to make sure that
        # we have the correct game. If not, nothing will work!

        # Here, we get the weird unknown value
        if game == staticValues.game_ddr and version == 1:
            unknownval = staticValues.mcode_unknown_q
        elif game == staticValues.game_ddr and version == 2:
            unknownval = staticValues.mcode_unknown_q
        elif game == staticValues.game_ddr and version == 3:
            unknownval = staticValues.mcode_unknown_q
        else:
            raise Exception("Something went wrong trying to get the mcode's 2nd value!")
        finalmcode.append(unknownval)

        # Here, we get the game's 3 character value
        gamemcode = mcodeStructs.getGameMcode(game, version)
        finalmcode.append(gamemcode)

        # Now, Let's get the region.
        trustedregion = mcodeStructs.getMcodeRegion(region)
        finalmcode.append(trustedregion)

        # Now, for the cabinet version. 
        # Most of the time, this will be A.
        # HOWEVER, there are some exceptions,
        # where we don't want it to be A. (GFDM)
        cabinet = staticValues.mcode_cab_a
        plsbeB = {
            staticValues.game_dm:staticValues.mcode_cab_b,
            staticValues.game_gf:staticValues.mcode_cab_b,
        }
        if game in plsbeB:
            cabinet = staticValues.mcode_cab_b
        finalmcode.append(cabinet)

        # Finally, we get the revision.
        # With my current understanding,
        # This will always be A.
        finalmcode.append(staticValues.mcode_rev_a)

        # With that, we're done!
        return finalmcode