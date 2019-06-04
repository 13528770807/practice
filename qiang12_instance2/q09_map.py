

def foo(x):
    return x * 2


print(list(map(foo, [1, 2, 3, 4, 5])))


data = list(range(10))
print(list(map(lambda x: x**3, data)))


# 假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，
# 请利用map()函数，把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list：


li1 = ['sAof', 'MIni', 'ddFF']
print(li1[1].upper())
print(li1[0][3].lower())


# 使用函数实现
def foo1(x):
    return x[0:1].upper() + x[1:].lower()


print(list(map(foo1, li1)))

# 使用匿名函数实现
print(list(map(lambda x: x[0:1].upper() + x[1:].lower(), li1)))