

#合并两个列表，相同的不要
# 方法一
li1 = [1, '2', 34, 5, 6]
li2 = [2, 3, 4, 5, 67, 8, 89, 9, 34, 666]

for i in range(len(li1)):
    if li1[i] not in li2:
        li2.append(li1[i])

print('li2:', li2)  # li2: [2, 3, 4, 5, 67, 8, 89, 9, 34, 666, 1, 6]


# extend  列表相加
li1.extend(li2)
print('li1:', li1)  # li1: [1, 2, 34, 5, 6, 2, 3, 4, 5, 67, 8, 89, 9, 34, 666, 1, 6]


# 方法二
lst2 = [1, 2, 34, 5, 6, 2, 3, 4, 5, 67, 8, 89, 9, 34, 666, 9]
n = 0
while n < len(lst2):  # 逐个遍历, 规避 for 循环漏掉
    for i in lst2:
        if lst2.count(i) > 1:
            lst2.remove(i)
        n += 1

print('lst2:', lst2)  # lst2: [1, 34, 6, 2, 3, 4, 5, 67, 8, 89, 34, 666, 9]


l1 = [1, 2, 3, "4", 5]
# l2 = [1, 3, 4, 7]


# list1 = str(l1)
# str1 = 'aaa'
# str2 = list1 + str1
# print(type(list1))  # <class 'str'>
# print(str2)  # [1, 2, 3, '4', 5]aaa


ali = [int(x) for x in l1]  # 通过列表推导式 将含有字符串的列表 转为整型数字列表
print('ali:', ali)  # ali: [1, 2, 3, 4, 5]


# 方法三
print('set().union:', list(set(li1).union(set(li2))))

# 方法四
a = set(li1)
b = set(li2)
print('a|b:', list(a | b))


