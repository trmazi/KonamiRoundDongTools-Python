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

        print('Producing a ' + types.get(dongtype) + " " + games.get(game) + " dongle, for the " + regions.get(region) + " region.")
        print("The PCBID given was "+pcbid)
        print("")