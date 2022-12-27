def NWD(a, b):
    while b != 0:
        tmp = a
        a = b
        b = tmp % b
    return a


print(NWD(12, 18))
