

class Zqiang():
    def zqiang(self):  # 第一个参数(self)代表实例化出来的对象
        print(self)
        print(self.__class__)


obj = Zqiang()
obj.zqiang()


class Zqiang():
    def zqiang(runoob):
        print(runoob)
        print(runoob.__class__)


obj2 = Zqiang()
obj2.zqiang()

