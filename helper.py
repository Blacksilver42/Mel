from commands import Order

while(1):
    
    print("   (cmd)(dtrak)(dsec)(ntrak)(nsec)x")
    IN = input(">> ")
    try:
        n = int(IN,2)
    except:
        continue

    o = Order(n)
    print(o, "| {0} = 0x{0:08X}".format(n))
    print()
