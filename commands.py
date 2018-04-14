import memory as mem
import sys
import getch


class Order:
    def __init__(self, val):
        self.val = val
        self.command   = (val & 4160749568) >> 27
        self.dtrack  = (val & 133169152)  >> 20
        self.dsec    = (val & 1032192)    >> 14
        self.ntrack = (val & 16256)      >> 7
        self.nsec   = (val & 126)        >> 1

        #self.echo()
    
    def __str__(self):
        f="x"
        if(hasattr(self,"name")):
            pass
        else:
            self.name = ("{0} {1:"+f+"}{2:"+f+"} {3:"+f+"}{4:"+f+"}").format(
                order_map[self.command].__name__,
                self.dtrack, self.dsec,
                self.ntrack, self.nsec)
        return self.name

    def __format__(self, spec):
        return ("{0:"+spec+"}").format(self.val)

    def __eq__(self, other):
        return self.val == other.val
    
    def echo(self):
        print("command: {0:8b} = {1}".format(self.command,order_map[self.command].__name__))
        print("dtrack:  {0:8b} = {0}".format(self.dtrack))
        print("dsec:    {0:8b} = {0}".format(self.dsec))
        print("ntrack:  {0:8b} = {0}".format(self.ntrack))
        print("nsec:    {0:8b} = {0}".format(self.nsec))
    
    def __call__(self):
        self.exec()
    
    def exec(self):
        print(self)
        order_map[mem.C.command]()
        mem.C = Order(mem.DRUM.read(self.ntrack,self.nsec))
    



def hcf():
    # HALT_AND_CATCH_FIRE
    print("Burn, baby, burn.")
    exit(1)


def transfer():
    mem.C.ntrack = mem.C.dtrack
    mem.C.nsec   = mem.C.dsec

def hlt(): #00000
    if(mem.U.dtrack != 0):
        sns()
    else:
        raise SystemExit

def sns(): #00000
    # What do you want me to sense?
    # Interpreter flags?
    # TODO.
    pass

def cxe(): #00001
    # TODO
    pass

def rau(): #00010
    mem.U = mem.DRUM.cread()

def ral(): #00011
    mem.L = mem.DRUM.cread()

def sau(): #00100
    #TODO
    pass

def mst(): #00101
    #TODO
    pass

def ldc(): #00110
    #TODO
    pass

def ldx(): #00111
    #TODO
    pass

def inp(): #01000
    mem.B = False
    try:
        if(mem.C.dtrack == 0):
            mem.U = getch.getch()
        if(mem.C.dtrack == 1):
            mem.L = getch.getch()
        if(mem.C.dtrack == 2):
            mem.U = int(input())
        if(mem.C.dtrack == 3):
            mem.L = int(input())
    except:
        mem.B = True

def exc(): #01001
    #TODO
    pass

def dvu(): #01010
    mem.U = mem.U / mem.DRUM.cread()

def div(): #01011
    #TODO
    dvu()

def srl(): #01100
    #TODO: there are like 6 unused bits in this command.
    if(mem.C.dtrack == 0):
        mem.U = mem.U >> mem.C.dsec
    if(mem.C.dtrack == 1):
        mem.U = mem.U << mem.C.dsec

def slc(): #01101
    # Cluster Foxtrot you, McBee.
    srl()

def mpy(): #01110
    mem.L = mem.U * mem.cread()

def mpt(): #01111
    mem.U = mem.U * 10

def prd(): #10000
    # I'm out of clever insults.
    pass

def pru(): #10001
    if(mem.C.dtrack == 0):
        print(mem.U)
    else:
        print(chr(mem.U))

def ext(): #10010
    mem.U = mem.cread() & mem.U

def mml(): #10011
    #TODO
    pass

def cme(): #10100
    mem.B = (mem.cread() == mem.U)

def cmg(): #10101
    mem.B = (mem.cread() > mem.U)

def tmi(): #10110
    if(mem.U < 0):
        transfer()

def tbc(): #10111
    if(mem.B):
        transfer()

def stu(): #11000
    mem.cwrite(mem.U)

def stl(): #11001
    mem.cwrite(mem.L)

def clu(): #11010
    stu()
    mem.U = 0

def cll(): #11011
    stl()
    mem.L = 0

def adu(): #11100
    mem.U += mem.cread()

def adl(): #11101
    mem.L += mem.cread()

def sbu(): #11110
    mem.U -= mem.cread()

def sbl(): #11111
    mem.L -= mem.cread()



order_map = [
    hlt, cxe, rau, ral, sau, mst, ldc, ldx,
    inp, exc, dvu, div, srl, slc, mpy, mpt,
    prd, pru, ext, mml, cme, cmg, tmi, tbc,
    stu, stl, clu, cll, adu, adl, sbu, sbl
]

def get_order(name):
    for i in order_map:
        if(i.__name__ == name):
            return i
