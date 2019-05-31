

# 单例1 使用模块
# from qiang13_working.q18_mysingleton import mysingleton
#
# mysingleton.foo()


# # 单例2 使用基类
# class Singleton():
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_inst'):
#             cls._inst = super(Singleton, cls).__new__(cls)
#         return cls._inst
#
#
# class Son(Singleton):
#     def __init(self, x):
#         self.x = x
#
#
# a = Son(4)
# b = Son(6)
# print(a)
# print(b)


# 使用装饰器 实现单例3
# def foo(f):  # 类f 当做参数传入函数
#     _instance = {}  # 创建空字典, 用于存放实例对象
#
#     def wrapper(*args, **kwargs):
#         if f not in _instance:  # 判断字典里是否创建过对象
#             _instance[f] = f(*args, **kwargs)  # 如果没有创建对象,创建对象并加入空字典
#         return _instance[f]  # 如果已经创建, 直接返回对象
#     return wrapper
#
#
# @foo
# class A(object):
#     a = 1
#
#     def __init__(self, x):
#         self.x = x
#
#
# a = A(6)
# print(a)
# b = A(4)
# print(b)
#
# print(a.a)
# print(a.x)
# print(b.x)


# # 使用类  bug
# class Singleton1():
#     def __init__(self, n):
#         self.n = n
#
#     @classmethod
#     def foo(cls, *args, **kwargs):
#         if not hasattr(Singleton1, '_instance'):
#             Singleton1._instance = Singleton1(*args, **kwargs)
#         return Singleton1._instance
#
#
# c = Singleton1(6)
# d = Singleton1(8)
#
# print(c)
# print(d)


# 使用元类4
class Singleton2(type):

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance1'):
            cls._instance1 = super(Singleton2, cls).__call__(*args, **kwargs)
        return cls._instance1


# class B(object):  # py2
class B(metaclass=Singleton2):  # py3
    __metaclass__ = Singleton2


e = B()
f = B()
print(e)
print(f)
print(e is f)

