def cmmdc(n1, n2):
    tryout = 0
    smallest = 0
    if n1 > n2:
        tryout = n1 - n2
        smallest = n2
    else:
        tryout = n2 - n1
        smallest = n1

    if n1 % tryout == 0 & n2 % tryout == 0:
        return tryout
    else:
        return cmmdc(smallest, tryout)


print(cmmdc(252, 105))
