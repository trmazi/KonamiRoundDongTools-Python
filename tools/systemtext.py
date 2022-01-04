class generateSystemPrints():
    '''
    Dumb tools to print happy messages to the console.
    Using this file so that I don't clutter up the main file.
    '''
    def printStartingText(dongtype:str, game, version, region, pcbid):
        '''
        Prints the starting message when you first run the program.
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
            'A':'Asian',
            'J':'Japanese',
            'K':'Korean',
            'U':'United States'
        }

        if game == 'ddr':
            versions = {
                '1':'SuperNova',
                '2':'SuperNova2',
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

        print('Producing a ' + types.get(dongtype) + " " + games.get(game) + " "+ versions.get(version)+ " dongle, for the " + regions.get(region) + " region.")
        print("The PCBID given was "+pcbid)
        print("")