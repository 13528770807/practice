"""
class Single():
    def foo(self):
        return "aaaaaaaa"


mysingle = Single()

print(mysingle.foo())
"""


""" 单利
class Mysingle():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Mysingle, cls).__new__(cls)

        return cls.instance


mysingle1 = Mysingle()
mysingle2 = Mysingle()

mysingle1.attr1 = 'value1'
# mysingle2.attr2 = 'value2'

print(mysingle1.attr1)
print(mysingle2.attr1)
print(mysingle1 is mysingle2)
"""

""" 装饰器
def singleton(cls):
    instance = {}

    def foo(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return foo


@singleton
class Myclass():
    a = 1


obj1 = Myclass()
obj2 = Myclass()
print(obj1 == obj2)
"""

# 元类(type)
# class Singleton(type):
#     def __init__(self, *args, **kwargs):
#         self._instance = None
#         super(Singleton, self).__init__(*args, **kwargs)
#
#     def __call__(self, *args, **kwargs):
#         if not self._instance:
#             self._instance = super(Singleton, self).__call__(*args, **kwargs)
#
#         return self._instance
#
#
# class Foo(Singleton):
#     a = 1
#
#
# obj1 = Foo()
# obj2 = Foo()
# print(obj1 == obj2)


class Singleton2(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super(Singleton2, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super(Singleton2, self).__call__(*args, **kwargs)
        return self.__instance


class Foo(object):
    __metaclass__ = Singleton2 #在代码执行到这里的时候，元类中的__new__方法和__init__方法其实已经被执行了，而不是在Foo实例化的时候执行。且仅会执行一次。


foo1 = Foo()
foo2 = Foo()
print(Foo.__dict__)  #_Singleton__instance': <__main__.Foo object at 0x100c52f10> 存在一个私有属性来保存属性，而不会污染Foo类（其实还是会污染，只是无法直接通过__instance属性访问）

print(foo1 is foo2)  # True
