import sys


def fibolacci(n):
    a, b, account = 0, 1, 0
    while True:
        if account > n:
            return
        yield a

        a, b = b, a+b
        account += 1


f = fibolacci(10)  # f 是一个迭代器,由生成器返回

while True:
    try:
        print(next(f), end=" ")

    except StopIteration:
        sys.exit()
