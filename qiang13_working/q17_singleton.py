

"""
# 使用装饰器
def foo(f):  # 类f 当做参数传入函数
    _instance = {}  # 创建空字典, 用于存放实例对象

    def wrapper(*args, **kwargs):
        if f not in _instance:  # 判断字典里是否创建过对象
            _instance[f] = f(*args, **kwargs)  # 如果没有创建对象,创建对象并加入空字典
        return _instance[f]  # 如果已经创建, 直接返回对象
    return wrapper


@foo
class A(object):
    a = 1

    def __init__(self, x):
        self.x = x


a = A(6)
print(a)
b = A(4)
print(b)

print(a.a)
print(a.x)
print(b.x)
"""


# 装饰器
class Singleton():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_inst'):
            cls._inst = super(Singleton, cls).__new__(cls)
        return cls._inst


class Son(Singleton):
    def __init(self, x):
        self.x = x


a = Son(4)
b = Son(6)
print(a)
print(b)

