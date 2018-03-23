import memory as mem
import commands

mem.init(tracks=10,sectors=10)

## An example command
#part   (cmd)(dtrk )(dsec)(ntrk )(nsec)x
cmd =  "00011000000100000000000000000010"
#value  RAL  0      0     0      1

foo = int(cmd,2)

mem.xwrite(0,0,commands.Order(foo))
mem.xwrite(1,0,42)


mem.xread(0,0).exec()

mem.echo_reg()
