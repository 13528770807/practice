'''
def wrapper():
    print('aa')

print(wrapper)

a = wrapper
a()
'''


"""
def fin():
    print("111")


def fin2():
    print("222")


def fin3():
    print("333")


ali = [fin, fin2, fin3]
for i in ali:
    i()
"""

"""
def f():
    print("123")


def fun(f):
    f1 = f
    f1()
    

fun(f)
"""


"""
def fun():
    print(456)


def fun2(f):
    return f


ret = fun2(fun)
ret()
"""

# name = '''fdsfdsfdsjlfjdsifjsflj'''
# print(name)


# ------------ info of Zhang San -----------
# Name  : Zhang San
# Age   : 22
# job   : Teacher
# Hobby: girl
# ----------------- end --------------------


"""
name = input('name:')
age = int(input('age:'))
job = input('job:')
hobby = input('hobby:')
message = '''
------------info of %s ------------
Name   :  %s
Age    :  %d
job    :  %s
hobby  :  %s
-------------  end  ---------------
''' % (name, name, age, job, hobby)
print(message)
"""

'''
name = input("name:")
age = input('age:')
job = input('job:')
hobby = input('hobby:')

dic = {'name': name, 'age': age, 'job': job, 'hobby': hobby}
info = """
=========  info of %(name)s  ========
 Name : %(name)s \n Age : %(age)s \n Job : %(job)s \n Hobby : %(hobby)s
===========  end  ================== 
""" % dic
print(info)
'''

# msg = '我是%s,年龄%d,学习进度为80%%' % ('张三', 18)
# print(msg)

# 0 or 4 and 3 or 7 or 9 and 6
# 0 or 3 or 7 or 6

# i = 1
# while i <= 10:
#     if i == 7:
#         i += 1
#     print(i)
#     i += 1

# i = 1
# while i <= 10:
#     if i == 7:
#         # i += 1
#         break
#     print(i)
#     i += 1
# else:
#     print('打印完毕')

# sum = 0
# i = 1
# while i <= 100:
#     # print(i)
#     sum += i
#     print(sum)
#     i += 1


# sum = 0
# i = 1
# while i < 101:
#     if i % 2 != 0:
#         sum += i
#         print(sum)
#     # print(i)
#     i += 1

# sum = 0
# for i in range(101):
#     if i % 2 == 0:
#         sum += i
#         print(sum)


# sum = 0
# i = 1
# while i < 100:
#     if i % 2 == 0:
#         sum -= i
#     else:
#         sum += i
#     print(sum)
#     i += 1

# n = 1
# x = 0  # 代表偶数
# y = 0  # 代表奇数
# sum = 0  # 代表和
# while n < 100:
#     if n % 2 == 1:
#         x = x + n
#
#     elif n % 2 == 0:
#         y = y + n
#
#     n = n + 1
# sum = x - y;
#
# print(sum)


# x = 1
# y = 98
# sum = 0
# while x < 99 and y > 2:
#     x = x + 2
#     y = y - 1
#     sum = x - y
#
# print(sum)


"""
i = 1
while True:
    name = input("name:")
    passwd = input("passwd:")
    if name  == 'zhangsan' and passwd == '123456':
        print('success')
        break
    else:
        print('passwd error times%s' % (3-i))

    if i == 3:
        print('多次登录')
        break

    i += 1
"""

"""
print(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)

print(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)

# 0 or 1 or 0 and 1 and 1 or 0
# 0 or 1 or 1 and 1 or 0
# 0 or 1 or 1 or 0   # T
"""

"""
8 or 3 and 4 or 2 and 0 or 9 and 7
0 or 2 and 3 and 4 or 6 and 0 or 3

8 or 4 or 0 or 7   # 8
0 or 3 and 4 or 0 or 3
0 or 4 or 0 or 3   # 4
"""


# 6 or 2 > 1   # 6
# 3 or 2 > 1   # 3
# 0 or 5 < 4   # False
# 5 < 4 or 3   # 3
# 2 > 1 or 6   # True
# 3 and 2 > 1  # True
# 0 and 3 > 1  # 0
# 2 > 1 and 3  # 3
# 3 > 1 and 0  # 0
# 3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2  # 2
# 2 or F or T


# sum = 0
# i = 1
# while i < 100:
#     if i == 88:
#         i += 1
#     if i % 2 == 0:
#         sum -= i
#     if i % 2 != 0:
#         sum += i
#     print(sum)
#     i += 1


# a = 1>2 or 4<7 and 8 == 8
# print(a)