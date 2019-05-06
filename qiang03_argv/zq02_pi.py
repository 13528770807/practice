from cmath import pi

print(pi)


print(r'\n')
print('\n')
print(R'\n')

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)

tup3 = 'a','b','c'  # 元组不用括号也可以
print(type(tup3))

# 常量>>>
i = 256*256
print('i的值为：%d' % i)
print('i的值为：', i)

# flag = 1
# while flag: print("welcome")
# print('good bye')

# for i in range(-10, -100, -30):
#     print(i)


for i in range(-100, -10, 30):
    print(i)
