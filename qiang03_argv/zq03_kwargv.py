from cmath import pi


def printinfo(argv, **kwargsll):
    print("输出：")
    print(argv)
    print(kwargsll)


printinfo(66, a=1, b=2)


def sum(argv1, argv2):
    total = argv1 + argv2
    print("函数内：", total)
    return total

aaa = sum(10, 20)
print("函数外：", aaa)

import builtins
print(dir(builtins))


sum = lambda argv3, argv4: argv3 + argv4
print(sum(30, 50))


if True:
    msg = "I`m zhangqiang"

print(msg)


num1 = 20
def foo():
    global num1  # 声明global 关键字
    num1 = 60
    print(num1)

foo()
print(num1)


def outer():
    num = 10
    def inner():
        nonlocal num  # 声明nonlocal
        num = 100
        print(num)
    inner()
    print(num)

outer()


a = 10
def sum():
    global a
    a = a +1
    print(a)

sum()
print(a)


a = 10
def sum(a):
    a = a + 1
    print(a)

sum(a)
print(a)


# strip() 移除字符 默认空字符
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
list_derived = [weapon.strip() for weapon in freshfruit]
print(list_derived)


list_derived2 = [str(round(355/113, i)) for i in range(1, 9)]
print(list_derived2)
print(pi)
print(str(round(9/3)))
