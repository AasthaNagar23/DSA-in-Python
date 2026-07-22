def onetoN(n):
    if n==0:
        return 0
    print(n)
    onetoN(n-1)
onetoN(5)