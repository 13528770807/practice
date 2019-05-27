
# _a  __a  __a__  的区别
'''
-a: 变量名  不能用from model import * 导入
__a: 私有属性
__a__: 魔法方法
'''


import math
import time

"""
类里面的修饰符有什么不同.
@classmethod @staticmethod

"""


# property
class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def run(self):
        print('run....')
        return 1+1

    def perimeter(self):
        return 2 * self.radius * math.pi


# print(Circle.area(10))
c = Circle(10)
print(c.radius)
print(c.area)  # 可以像访问属性一样访问 area
print(c.run())
print(c.perimeter())


# staticmethod
class Date():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def today():
        t = time.localtime()  # 获取当天时间
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    @staticmethod
    def tomorrow():
        t = time.localtime(time.time()+86400)  # 获取当天+1天时间(明天),
        return Date(t.tm_year, t.tm_mon, t.tm_mday)


a = Date('2019', 2, 22)
b = Date.today()
c = Date.tomorrow()
print('a:', a.year, a.month, a.day)
print('b:', b.year, b.month, b.day)
print('c:', c.year, c.month, c.day)


