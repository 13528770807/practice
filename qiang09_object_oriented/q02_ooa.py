

class people():
    # 基本属性,类属性
    name = ''
    age = 18
    # 私有属性, 私有属性在类的外部无法直接访问
    __weight = 0

    # 构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.weight = w

    def speak(self):
        print('姓名:{}  今年:{}'.format(self.name, self.age))


# 单继承父类
class student(people):
    def __init__(self, n, a, w, g):
        # 调用父类的构造方法
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        # print('姓名:{} 今年:{} 读{}年级了'.format(self.name, self.age, self.grade))
        print('姓名:%s 今年:%d 读%d年级了' % (self.name, self.age, self.grade))


# 另一个类, 为多继承准备
class speaker():
    name = ''
    topic = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print('姓名:%s 讲的主题是%s' % (self.name, self.topic))


# 多重继承
# class simple(student, speaker):
class simple(speaker, student):  # 方法名相同, 调用排前面的父类的方法
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


# 定义基本类
xiaoming = people('小明', 20, 60)
xiaoming.speak()

# 单继承父类
xiaoli = student('小李', 6, 39, 3)
xiaoli.speak()

# 多继承
sim = simple('Tom', 22, 70, 9, 'python')
sim.speak()  # 方法名相同, 调用排前面的父类的方法
