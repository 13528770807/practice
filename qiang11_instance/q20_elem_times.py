

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
