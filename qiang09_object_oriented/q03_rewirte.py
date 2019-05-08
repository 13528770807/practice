

class Parent:
    def myMethod(self):
        print("调用父类的方法")


class Child(Parent):
    def myMethod(self):
        print("调用子类的方法")


c = Child()  # 子类实例
c.myMethod()  # 重写父类的方法
super(Child, c).myMethod()  # 通过子类对象调用父类已被覆盖的方法


class JustCount():
    __secortcount = 0
    publiccount = 0

    def count(self):
        self.__secortcount += 1
        self.publiccount += 1
        print(self.__secortcount)


counter = JustCount()
counter.count()  # 通过方法访问私有属性
counter.count()  # 通过方法访问私有属性
print(counter.publiccount)  # 正常访问公有属性
# print(counter.__secortcount)  # error 实例不能访问私有变量


class Site:
    def __init__(self, name, url):
        self.name = name
        self.__url = url

    def who(self):
        print("name:{}\nurl:{}".format(self.name, self.__url))

    def __foo(self):
        print("私有方法")

    def foo(self):
        print("你访问{}的地址为{}".format(self.name, self.__url))


site = Site("百度", "www.baidu.com")
site.who()
site.foo()  # 访问公有方法
# site.__foo()  # error 实例不能方法公有方法


class Victor():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Victor({}, {}) '.format(self.a, self.b)

    def __add__(self, other):
        # return Victor(self.a + other.a, self.b + other.b)  # 第一参数与另一实例第一参数相加,第二参数与另一实例第二参数相加
        # return Victor(self.a + other.b, self.b + other.a)  # 第一参数与另一实例第二参数相加,第二参数与另一实例第一参数相加(交叉相加)
        return Victor(self.a + self.b, other.a + other.b)   # 实例内部两参数相加


vict = Victor(10, 20)
vict2 = Victor(2, 6)
print(vict.__str__())  # __str__ 说明
print(vict + vict2)
