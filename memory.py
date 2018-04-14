import commands

class Drum:
    def __init__(self, tracks, sectors):
        self.tracks = tracks
        self.sectors = sectors
        self.xyzzy = [[0 for i in range(sectors)] for j in range(tracks)]
        
    def read(self, track, sec):
        return self.xyzzy[track][sec]

    def oread(self, order):
        return self.read(order.dtrack,order.dsec)

    def cread(self):
        return self.oread(C)

    def write(self, track, sec, value):
        self.xyzzy[track][sec] = value
        return value

    def owrite(self, order, value):
        return self.write(order.dtrack, order.dsec)

    def cwrite(self, value):
        return self.owrite(C, value)

    def next(self, trk, sec):
        if(sec >= self.sectors):
            sec = 0
            trk += 1
        else:
            sec += 1

        return (trk, sec)

    def cnext(self):
        (C.dtrack, C.dsec) = self.next(C.dtrack, C.dsec)
        
            

def init(tracks=122,sectors=64):
    global U
    global L
    global C
    global X
    global B
    global DRUM
    U = 0 #   upper accumulator
    L = 0 #   lower accumulator
    C = 0 # command register
    X = 0 #   index register
    B = 0 #  branch control
    
    # The actual freakin' drum.
    DRUM = Drum(tracks,sectors)


def cmd2i(x):
    if(typeof(x)==int):
        return x
    return x.val

def echo(reg_spec="032b"):
    echo_reg(spec=reg_spec)
    DRUM()

def echo_reg(spec = "032b"):
    print("U:", ("{0:"+spec+"} = {0}").format(U))
    print("L:", ("{0:"+spec+"} = {0}").format(L))
    print("C:", ("{0:"+spec+"} = {0}").format(C))
    print("X:", ("{0:"+spec+"} = {0}").format(X))


