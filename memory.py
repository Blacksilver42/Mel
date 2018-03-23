def init(tracks=122,sectors=64):
    global U
    global L
    global C
    global X
    global DRUM
    U = 0 #   upper accumulator
    L = 0 #   lower accumulator
    C = 0 # command register
    X = 0 #   index register

    # The actual freakin' drum.
    DRUM = [[0 for i in range(sectors)] for j in range(tracks)]


def cmd2i(x):
    if(typeof(x)==int):
        return x
    return x.val

def echo():
    echo_reg()
    echo_mem()

def echo_mem():
    print(DRUM)

def echo_reg():
    spec = "32b"
    print("U:", ("{0:"+spec+"} = {0}").format(U))
    print("L:", ("{0:"+spec+"} = {0}").format(L))
    print("C:", ("{0:"+spec+"} = {0}").format(C))
    print("X:", ("{0:"+spec+"} = {0}").format(X))

def read(order):
    return DRUM[order.dtrack][order.dsec]

def cread():
    return read(mem.C)

def xread(track, sec):
    return DRUM[track][sec]

def write(order, value):
    DRUM[order.dtrack][order.dsec] = value
    return read(order)

def xwrite(track, sec, value):
    DRUM[track][sec] = value
    return xread(track, sec)
