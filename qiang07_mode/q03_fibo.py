def fibo(n):
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a+b
    print()


def fibo2(m):
    a, b = 0, 1
    fibo_list = list()
    while b < m:
        fibo_list.append(b)
        a, b = b, a+b
    print()
    return fibo_list

