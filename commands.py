import memory as mem

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
        return "{0:b}".format(self.val)

    def __format__(self, spec):
        return ("{0:"+spec+"}").format(self.val)
        
    def echo(self):
        print("command: {0:8b} = {0}".format(self.command))
        print("dtrack:  {0:8b} = {0}".format(self.dtrack))
        print("dsec:    {0:8b} = {0}".format(self.dsec))
        print("ntrack:  {0:8b} = {0}".format(self.ntrack))
        print("nsec:    {0:8b} = {0}".format(self.nsec))
    
    def exec(self):
        mem.C = self
        [
            hlt, cxe, rau, ral, sau, mst, ldc, ldx,
            inp, exc
        ][mem.C.command](mem.C)



def hcf(o):
    # HALT_AND_CATCH_FIRE
    print("HCF")
    raise SystemExit
    

def hlt(o):
    # TODO: implement this properly
    # sns also uses the same opcode.
    raise SystemExit

def sns(o):
    # What do you want me to sense?
    # Interpreter flags?
    # TODO.
    pass

def cxe(o):
    # TODO
    pass

def rau(o):
    mem.U = mem.read(o)

def ral(o):
    mem.L = mem.read(o)

def sau(o):
    #TODO
    pass

def mst(o):
    #TODO
    pass

def ldc(o):
    #TODO
    pass

def ldx(o):
    #TODO
    pass

def inp(o):
    #TODO
    pass

def exc(o):
    #TODO
    pass
