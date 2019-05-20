

# 列表出现次数
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]


count = 0
for i in lst:
    if i == 10:
        count += 1
print("times:", count)


def count10(lst, x):
    return lst.count(x)


print(count10(lst, 10))


# 统计和
list1 = [11, 5, 17, 18, 23]

total = 0
for i in range(len(list1)):
    total += list1[i]
print('tt:', total)


# while 统计和
total1 = 0
i = 0
while i <= len(list1)-1:
    total1 += list1[i]
    i += 1
print('total:', total)


# 使用递归
list1 = [11, 5, 17, 18, 23]


def sumOflist(list1, size):
    if size == 0:
        return 0
    else:
        return list1[size-1] + sumOflist(list1, size-1)


print('sumOflist:', sumOflist(list1, len(list1)))


# 列表和
def sumlist(li, sum=1):
    for i in range(len(li)):
        sum *= li[i]
    return sum


list3 = [1, 2, 3]
list4 = [3, 2, 4]
print('multi:', sumlist(list3))
print('multi2:', sumlist(list4))


# 列表最小元素
list5 = [10, 20, 4, 45, 99]
list5.sort()
print(list5)
print(list5[0])
print(list5[:1])

print('min:', min(list5))


# 列表最大元素
list6 = [10, 20, 4, 45, 99]
list6.sort()
print('biggest:', list6[len(list6)-1])

print('max:', max(list6))


# 移除字符串中的指定位置字符
test_str = "Runoob"
new_str = ''
print('index:', test_str.index('o'))
for i in range(len(test_str)):
    if i != test_str.index('o'):
        new_str += test_str[i]
print('new_str:', new_str)


# 判断字符串是否存在子字符串
string = "www.runoob.com"
sub_str = "runoob"

if sub_str in string:
    print('True')


def check(string, sub_str):
    print('find:', string.find(sub_str))
    if string.find(sub_str) == -1:
        print('no exist')
    else:
        print('exist')


string1 = "www.runoob.com"
sub_str1 = "runoob"
check(string1, sub_str1)


#  判断字符串长度
string2 = "www.runoob.com"
print('len:', len(string2))


def findLen(str):
    count = 0
    print(str[:], end=' ')
    while str[count:]:
        count += 1
    return count


print('count:', findLen(string2))


import re


# 使用正则表达式提取字符串中的 URL
def Find(string):
    # findall() 查找匹配正则表达式的字符串
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    return url


string = 'Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com'
print("Urls: ", Find(string))

