import memory as mem
import commands
import sys



if(len(sys.argv) < 2):
    fname = input("File? ")

# get fname from args

with open(fname, "rb") as f:
    mem.input(f)
