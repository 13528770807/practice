

#合并两个列表，相同的不要
# 方法一
li1 = [1, 2, 34, 5, 6]
li2 = [2, 3, 4, 5, 67, 8, 89, 9, 34, 666]

for i in range(len(li1)):
    if li1[i] not in li2:
        li2.append(li1[i])

print('li2:', li2)


# extend
li1.extend(li2)
print('li1:', li1)


# 方法二
lst2 = [1, 2, 34, 5, 6, 2, 3, 4, 5, 67, 8, 89, 9, 34, 666, 9]
n = 0
while n < len(lst2):
    for i in lst2:
        if lst2.count(i) > 1:
            lst2.remove(i)
        n += 1

print('lst2:', lst2)


