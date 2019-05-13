import cmath
import random
from math import pi


print('hello world')

print('='*60)
a = 10
b = 20
c = a + b
print('{}+{}的和为{}'.format(a, b, c))
# print("两数之和为%.1f" % (float(input("请输入第一个值:")) + float(input("请输入第二个值:"))))


# python 平方根
# num = float(input("请输入一个数字:"))
# num_sqrt = num ** 0.5
# print('%0.3f的平方根为：%0.3f' % (num, num_sqrt))
# print('{0:0.3f}的平方根为：{1:0.3f}'.format(num, num_sqrt))

print('='*60)
# 计算实数和复数的平方根
# num1 = int(input("请输入一个数字:"))
num1 = 4
num_sqrt1 = cmath.sqrt(num1)
print('{0}的平方根为：{1:.3f}+{2:.3f}j'.format(num1, num_sqrt1.real, num_sqrt1.imag))


# 圆的面积
def findArea(r):
    a = pi*(r**2)
    return a


print("圆的面积为：%.6f" % findArea(4))

# 生成随机数
random1 = random.randint(1, 6)
print('随机数为:', random1)


# 交换变量
# x = int(input("请输入x的值:"))
# y = int(input("请输入y的值:"))
#
# x = x + y
# print(x)
# y = x - y
# print(y)
# x = x - y
# print(x)
#
# print('交换后x的值为{}：'.format(x))
# print('交换后y的值为{}：'.format(y))

# 异或
print('='*60)
# x = int(input("请输入x的值:"))  # 6 5
# y = int(input("请输入y的值:"))  # 9 3
#
# x = x ^ y
# # 0110(6) ^ 1001(9) = 1111(15)
# # 0101(5) ^ 0011(3) = 0110(6)
# print(x)
# y = x ^ y
# # 1111(15) ^ 1001(9) = 0110(6)
# # 0110(6) ^ 0011(3) = 0101(5)
# print(y)
# x = x ^ y
# # 1111(15) ^ 0110(6) = 1001(9)
# # 0110(6) ^ 0101(5) = 0011(3)
# print(x)
#
# print('交换后x的值为{}：'.format(x))
# print('交换后y的值为{}：'.format(y))


def xor(x, y):
    x = x ^ y  # x1 = x ^ y
    y = x ^ y  # y = x ^ y ^ y   (公式:y^x^y=x)  y = x
    x = x ^ y  # x = x ^ y ^ y   (上一步:y=x 得:x=x^y^x)  x = y
    return x, y


print(xor(10, 20))
