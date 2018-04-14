import sys
import commands

if("-d" in sys.argv):
    print("Decimal mode")
    fmt = "d"
else:
    print("Hex mode")
    fmt = "x"

while 1:
    IN = input(">>")
    try:
        IN = IN.split()
        cmd = IN[0]
        d = IN[1]
        n = IN[2]
        dsec = d[:2]
        dtrk = d[2:]
        nsec = n[:2]
        ntrk = n[2:]

        
    except:
        print("?")
