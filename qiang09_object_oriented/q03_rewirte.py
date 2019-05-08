

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
