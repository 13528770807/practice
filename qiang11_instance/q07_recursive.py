

def fibolacci(n):
    if n <= 1:
        return n
    else:
        return fibolacci(n - 1) + fibolacci(n - 2)


num = int(input("你要输出几项:"))

if num <= 0:
    print("非法操作")
else:
    print('斐波拉契数列')
    for i in range(num):
        print(fibolacci(i))