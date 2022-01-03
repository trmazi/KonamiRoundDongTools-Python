class staticValues():
    '''
    List of static values that should be hardcoded
    '''
    key_type_black = 0
    key_type_white = 1

    security_key_white = 'E-AMUSE3'
    security_key_black_ps2 = 'GENTAKAH'
    security_key_black_ddr_x = '573PROJE'
    security_key_black_jube_gfdm = 'UDONHRKI'

    # supported games
    game_ddr = 'ddr'
    game_dm = 'dm'
    game_gf = 'gf'
    game_jb = 'jb'

    # security header
    mcode_header = 'G'
    
    # unknown value
    mcode_unknown_c = 'C'
    mcode_unknown_e = 'E'
    mcode_unknown_k = 'K'
    mcode_unknown_n = 'N'
    mcode_unknown_q = 'Q'

    # game codes
    mcode_game_ddr_sn = 'FDH'
    mcode_game_ddr_sn2 = 'GDJ'
    mcode_game_ddr_x = 'HDX'

    mcode_game_dm_v = 'E02'
    mcode_game_dm_v2 = 'F02'
    mcode_game_dm_v3 = 'F32'
    mcode_game_dm_v4 = 'G32'
    mcode_game_dm_v5 = 'H32'
    mcode_game_dm_v6 = 'I32'
    mcode_game_dm_v7 = 'J32'
    mcode_game_dm_v8 = 'K32'

    mcode_game_gf_v = 'E03'
    mcode_game_gf_v2 = 'F03'
    mcode_game_gf_v3 = 'F33'
    mcode_game_gf_v4 = 'G33'
    mcode_game_gf_v5 = 'H33'
    mcode_game_gf_v6 = 'I33'
    mcode_game_gf_v7 = 'J33'
    mcode_game_gf_v8 = 'K33'

    mcode_game_jb = 'H44'
    mcode_game_jb_r = 'I44'
    mcode_game_jb_k = 'J44'
    mcode_game_jb_c = 'K44'

    # region
    mcode_reg_asia = 'A'
    mcode_reg_kor = 'K'
    mcode_reg_jap = 'J'
    mcode_reg_usa = 'U'

    # cabinet
    mcode_cab_a = 'A'
    mcode_cab_b = 'B'
    mcode_cab_c = 'C'
    mcode_cab_d = 'D'

    # revision
    mcode_rev_a = 'A'
    mcode_rev_b = 'B'
    mcode_rev_c = 'C'

    # security scramble table
    scramble_table = [
        0x0C,
        0x02,
        0x0F,
        0x01,
        0x07,
        0x09,
        0x04,
        0x0A,
        0x00,
        0x0E,
        0x03,
        0x0D,
        0x0B,
        0x05,
        0x08,
        0x06
    ]

class dataStructs():
    '''
    Tools for finding proper data values for generating dongles
    '''
    def checkUserInput(checktype:int, userdata:str):
        '''
        Given what the user has inputted, and verify it.
        '''
        if checktype == 1: # checking for dongle type
            validdata = {
                'B':staticValues.key_type_black,
                'W':staticValues.key_type_white,
            }
            if userdata not in validdata:
                return 0
            else: return 1

        if checktype == 2: # checking for game
            validdata = {
                'ddr':staticValues.game_ddr,
                'dm':staticValues.game_dm,
                'gf':staticValues.game_gf,
                'jb':staticValues.game_jb,
            }
            if userdata not in validdata:
                return 0
            else: return 1

        if checktype == 4: # checking for region
            validdata = {
                'A':staticValues.mcode_reg_asia,
                'J':staticValues.mcode_reg_jap,
                'K':staticValues.mcode_reg_kor,
                'U':staticValues.mcode_reg_usa
            }
            if userdata not in validdata:
                return 0
            else: return 1

        if checktype == 5: # checking for PCBID
            if len(userdata) != 8:
                return 0
            else: return 1

    def getDongleType(type:str):
        '''
        Given the type of dongle, return the
        data that the script wants.
        '''
        validtypes = {
            'B':staticValues.key_type_black,
            'W':staticValues.key_type_white,
        }
        if type in validtypes:
            return validtypes.get(type)
        else:
            raise Exception("You did not specify the type correctly. Please use type b for black dongles or w for white dongles.")

    def getSigningKey(data:int):
        '''
        Given a value, return the correct
        signing key that should be used.

        Signing keys will always be 8 characters long.
        '''
        validkeys = {
            1:staticValues.security_key_white, # For e-Amusement WHITE dongles.
            2:staticValues.security_key_black_ps2, # For BLACK PS2 dongles.
            3:staticValues.security_key_black_ddr_x, # For BLACK DDR X dongles.
            4:staticValues.security_key_black_jube_gfdm, # For BLACK Jubeat/GFDM (V4 -> V8) dongles.
        }
        if data in validkeys:
            return validkeys.get(data)
        else:
            raise Exception("The code you have provided doesn't exist! Please use the correct code.")

class mcodeStructs():
    '''
    Tools for generating a proper mcode.
    Also contains proper data structures.
    '''
    def getGameMcode(game:str, version):
        '''
        Given a game and a version, creates a proper mcode for said game.
        '''
        if game == 'ddr':
            validgames = {
                1:staticValues.mcode_game_ddr_sn,
                2:staticValues.mcode_game_ddr_sn2,
                3:staticValues.mcode_game_ddr_x,
            }
            if version in validgames:
                return validgames.get(version)
            else:
                raise Exception("You have provided an incorrect version for DDR! Please use 1 -> 3 for SN, SN2, and X.")

        elif game == 'dm':
            validgames = {
                1:staticValues.mcode_game_dm_v,
                2:staticValues.mcode_game_dm_v2,
                3:staticValues.mcode_game_dm_v3,
                4:staticValues.mcode_game_dm_v4,
                5:staticValues.mcode_game_dm_v5,
                6:staticValues.mcode_game_dm_v6,
                7:staticValues.mcode_game_dm_v7,
                8:staticValues.mcode_game_dm_v8,
            }
            if version in validgames:
                return validgames.get(version)
            else:
                raise Exception("You have provided an incorrect version for DM! Please use 1 -> 8.")

        elif game == 'gf':
            validgames = {
                1:staticValues.mcode_game_gf_v,
                2:staticValues.mcode_game_gf_v2,
                3:staticValues.mcode_game_gf_v3,
                4:staticValues.mcode_game_gf_v4,
                5:staticValues.mcode_game_gf_v5,
                6:staticValues.mcode_game_gf_v6,
                7:staticValues.mcode_game_gf_v7,
                8:staticValues.mcode_game_gf_v8,
            }
            if version in validgames:
                return validgames.get(version)
            else:
                raise Exception("You have provided an incorrect version for GF! Please use 1 -> 8.")

        elif game == 'jb':
            validgames = {
                1:staticValues.mcode_game_jb,
                2:staticValues.mcode_game_jb_r,
                3:staticValues.mcode_game_jb_k,
                4:staticValues.mcode_game_jb_c,
            }
            if version in validgames:
                return validgames.get(version)
            else:
                raise Exception("You have provided an incorrect version for JB! Please use 1 -> 4.")

        else:
            raise Exception("You have provided an incorrect game. Please use ddr, dm, gf, or jb.")
    
    def getMcodeRegion(region:str):
        '''
        Given a user input region, returns a valid, known, region.
        '''
        validregions = {
            'A': staticValues.mcode_reg_asia,
            'J': staticValues.mcode_reg_jap,
            'K': staticValues.mcode_reg_kor,
            'U': staticValues.mcode_reg_usa,
        }
        if region not in validregions:
            raise Exception("You have provided an incorrect region!")
        else:
            return validregions.get(region)