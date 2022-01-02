import os
import sys

from tools.structs import staticValues, dataStructs
from tools.mcodetools import mcodeTools
from tools.systemtext import generateSystemPrints

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
    5:'Invalid PCBID. PCBID must be 20 characters long.',
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
    sys.exit(0)
elif verifyprompt == 'Yes':
    print('')
    print("OK, let's do it!")

# Let's actually start making the dongle!
#   For starters, we need to generate an mcode that the game will like.
mcode = mcodeTools.makeMcode(sys.argv[2], sys.argv[3], sys.argv[4])
print(mcode)