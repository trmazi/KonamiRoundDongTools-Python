import sys

from tools.structs import staticValues, dataStructs
from tools.compileinfo import CompileDong
from tools.mcodetools import mcodeTools
from tools.systemtext import generateSystemPrints
from tools.filetools import fileTools

# This tools should be used to
# generate dongle .bin files for 
# round konami dongles based on the
# 1Wire TI EEprom.

# Needs this core information to work.
# - The type (B or W)
# - The signing key (has to match a game version)
# - The mcode (is somewhat user-settable, but must match some data)
# - The PCBID (must follow a strict data set)

# Starting arguments should be:
# - Dongle type (B or W)
# - The game 
#   - ddr
#   - dm
#   - gf
#   - jb
# - The version (in the form of numbers)
# - Game region (A, J, K, U)
# - PCBID

# Do checking on the input from the user.
if len(sys.argv) != 6:
    print(f"donglegen <dongtype> <game> <version> <region> <pcbid>")
    print("")
    print("Valid dongle types are B or W.")
    print("Valid games are ddr, dm, gf, and jb.")
    print("Valid versions can be found in the readme.md file")
    print("Valid regions are A, J, K, and U")
    sys.exit(0)

checks = {
    1:'Invalid dongle type. Refer to the readme.',
    2:'Invalid game. Refer to the readme.',
    3:'Invalid version. Version must be a NUMBER! Refer to the readme.', # Not actually being used atm :kek:
    4:'Invalid region. Refer to the readme.',
    5:'Invalid PCBID. PCBID must be 8 characters long.',
}
for chk in range(1, 6):
    check = dataStructs.checkUserInput(chk, sys.argv[chk])
    if check == 0:
        print(checks.get(chk))
        sys.exit(0)

# do a quick user verification
generateSystemPrints.printStartingText(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
verifyprompt = input('Does this look correct? Please type Yes or No. ')
if verifyprompt == 'No':
    print('')
    print('Please fix your input and try again.')
    exit()
elif verifyprompt == 'Yes':
    print('')
    print("OK, let's do it!")
else:
    print('')
    print('Please fix your input and try again.')
    exit()

# Let's actually start making the dongle!

# Here's the current workflow. 
# 1: Gather all of the starting information
#   - Determine if it's a black or white dongle.
#   - Get the signing key
#   - Get the mcode
#   - Get the PCBID
# 2: Compile the data into an array
# 3: Get a fully formed string from the array
# 4: Convert the string to the proper formatting
# 5: Write the string to a bin file
# 6: Verify the file with some more checks
# 7: Profit.

dongtype = dataStructs.getDongleType(sys.argv[1])
version = int(sys.argv[3])

if dongtype == staticValues.key_type_white: # compile a white dongle
    mcode = mcodeTools.makeMcode(sys.argv[2], version, sys.argv[4])
    compileddong = CompileDong.makeWhiteDong(sys.argv[5], mcode)

elif dongtype == staticValues.key_type_black: # compile a black dongle
    if sys.argv[2] == staticValues.game_ddr and version == 1:
        key = dataStructs.getSigningKey(2)
    elif sys.argv[2] == staticValues.game_ddr and version == 2:
        key = dataStructs.getSigningKey(2)
    elif sys.argv[2] == staticValues.game_ddr and version == 3:
        key = dataStructs.getSigningKey(3)
    else:
        raise Exception('Failed getting the signing key!')

    mcode = mcodeTools.makeMcode(sys.argv[2], version, sys.argv[4])
    compileddong = CompileDong.makeBlackDong(key, mcode, sys.argv[5])
    
# Now that we have a dongle made, we need to write it to a file.
# The file will be stored from where the user wrote the command.

fileTools.makeFile(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], compileddong)
