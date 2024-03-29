
class fileTools():
    '''
    Tools to generate files and send them to the user's computer.
    This is done by sending all of your money to Konami.
    '''
    def makeFile(dongletype:str, game:str, version:str, region:str, pcbid:str, finaldata:list):
        '''
        Given the dongle type, the game, the version, the pcbid, and the final data.
        Makes a .bin file for the user that can be directly used or written to a dongle.
        '''
        types = {
            'B':'BLACK',
            'W':'WHITE',
        }
        games = {
            'ddr':'DanceDanceRevolution',
            'dm':'DrumMania',
            'gf':'GuitarFreaks',
            'jb':'Jubeat',
        }
        regions = {
            'A':'Asia',
            'J':'Japan',
            'K':'Korea',
            'U':'United_States'
        }

        if game == 'ddr':
            versions = {
                '1':'SuperNOVA',
                '2':'SuperNOVA2',
                '3':'DDR_X'
            }
        elif game == 'dm' or game == 'gf':
            versions = {
                '1':'V',
                '2':'V2',
                '3':'V3',
                '4':'V4',
                '5':'V5',
                '6':'V6',
                '7':'V7',
                '8':'V8',
            }
        elif game == 'jb':
            versions = {
                '1':'Jubeat1',
                '2':'Ripples',
                '3':'Knit',
                '4':'Copius',
            }

        filename = ("dongle_"+
        types.get(dongletype)+"_"
        +games.get(game)+"_"
        +versions.get(version)+"_"
        +regions.get(region)+"_"
        +pcbid+".bin")

        print("")
        print('Making a file in the current directory with the name of:')
        print(filename)

        file = open(filename, 'wb')
        file.write(bytes(finaldata))
        file.close()
        
        print("")
        print("Done!")
        print("Thank you for playing!")