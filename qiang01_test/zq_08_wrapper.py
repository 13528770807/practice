class Animal():
    name = 'monkey'
    age = 10

    __nick_name = "something just like this"

    def __get_nike_name(self):
        return self.__nick_name

    def show_nick_name(self):
        print('昵称 :' + self.__get_nike_name())

    def show_nick_name_for_other(self, abc):
        self.show_nick_name()
        print("it's a secret:" + str(abc))

    def add_num(self, *nums):
        print(*nums)
        print(nums)
        result = 0
        for i in nums:
            result += i
        return result

    # 构造方法，改变私有属性
    def change_nike_name(self, name):
        self.__nick_name = name
        return self.__nick_name

    def show(self):
        print(self.name)
        print(self.age)


class Human(Animal):
    name = 'laowang'
    score = 60


# 实例对象修改的属性优先级高
# human = Human()
# print(human.name+','+str(human.age))
#
# Human.name = 'cls_new_laowang'  # 通过类对象修改属性
# print(human.name)
#
# human.name = 'obj_new_laowang'  # 实例对象修改属性
# print(human.name)
#
# Human.name = 'cls_new_laowang2'  # 类对象修改属性
# print(human.name)
#
# human2 = Human()   # 创建实力对象human2
# print(human2.name)

ani = Animal()
# ani.show()
# ani.show_nick_name()
# ani.show_nick_name_for_other('snake')
# sum = ani.add_num(1, 2, 3, 4, 5)
# print(sum)
ani.show_nick_name()
ani.change_nike_name('snake')
ani.show_nick_name()