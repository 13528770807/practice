

import random


li = [1, 2, 3, 4, 5, 6]
random.shuffle(li)  # 随机(洗牌)
print(li)

str1 = " abcd"
str2 = "abCd "
print(str1.lstrip())  # 去掉左边空格
print(str2.rstrip())  # 去掉右边空格

print(str1.upper().lstrip())
print(str2.lower())

print(str1.islower())
print(str2.isupper())

try:
    if 1 != "1":
        print('ture')
    else:
        print('error')
except Exception as e:
    print('e error')
    print(e)
