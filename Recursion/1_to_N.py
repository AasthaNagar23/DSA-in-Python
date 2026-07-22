def onetoN(n):
    if n==0:
        return 0
    onetoN(n-1)
    print(n)
onetoN(5)