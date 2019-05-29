import copy


# 切片反转
str = "dhajdfna"
# 问:用切片或其他方法对该字符串进行反转?

print(str[::-1])


# 问:(1)这样书写有没有什么问题?
#    (2)如果这样写会存在哪些隐患?
a = "hello"  # 全局变量


def test1(a):
    a = a + "world"
    print(a)


def test2():
    a = "python"
    print(a)


test1(a)
test2()


# is 和 == 的区别,及平时怎么什么使用?
# Is对比的是内存地址，==是值对比
li1 = [1, 2, 3, [4, 5, [6, 7]]]
li2 = copy.copy(li1)  # 浅拷贝, 只拷贝表面层
print(id(li1))  # 140448503823752
print(id(li2))  # 140448503980808
print(li1 is li2)  # False
print(li1 == li2)  # True

li3 = copy.deepcopy(li1)
print(id(li1))  # 140448503823752
print(id(li3))  # 140448503411400
print(li1 is li3)  # False
print(li1 == li3)  # True

a = 1
b = a
print(id(a))  # 10919328
print(id(b))  # 10919328
print(a is b)  # True
