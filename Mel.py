import memory as mem
import commands
import sys

mem.init()

if(sys.argv == [__file__]):
    fname = input("File? ")



# get fname from args

with open(fname, "rb") as f:
    byte = f.read(4)
    track = 0
    sec = 0
    while byte:
        mem.DRUM.write(track, sec, int.from_bytes(byte,byteorder='big'))
        (track, sec) = mem.DRUM.next(track, sec)
        byte = f.read(4)


#mem.C = commands.Order(mem.DRUM.read(0,0))

for u in mem.DRUM.xyzzy[0]:
    print(commands.Order(u))
    if (u == 0): break
