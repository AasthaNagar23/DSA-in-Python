def fibo(n):        # 1 1 2 3 5 8 13
    if n==0:
        return 1
    if n==1:
        return 1
    return fibo(n-2)+fibo(n-1)
print(fibo(3))