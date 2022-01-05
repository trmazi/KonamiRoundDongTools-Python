import sys

from tools.compileinfo import CompileDong

if len(sys.argv) != 4:
    print(f"donglegen_raw <key> <mcode> <pcbid>")
    print("")
    exit()

in_key = sys.argv[1].upper()
in_mcode = sys.argv[2].upper()
in_pcbid = sys.argv[3].upper()

if len(in_key) != 8:
    print(f"invalid key.")
    exit()

if len(in_mcode) != 8 or in_mcode[0] != 'G':
    print("invalid mcode.")
    exit()

if len(in_pcbid) != 8:
    print(f"invalid pcbid.")
    exit()

compileddong = CompileDong.makeBlackDong(in_key, in_mcode, in_pcbid)
open(f"raw_{in_mcode}_{in_pcbid}", "wb").write(bytes(compileddong))