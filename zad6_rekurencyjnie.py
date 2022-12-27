def NWD2(a, b):
    if b == 0:
        print(a)
    else:
        tmp = a
        a = b
        b = tmp % b
        NWD2(a, b)
