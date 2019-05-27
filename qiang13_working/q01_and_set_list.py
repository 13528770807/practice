

# 获取两个list 的交集  intersection
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]


li = [var for var in list1 if var in list2]
print(li)


# 方法二
print(list(set(list1).intersection(set(list2))))


#  给定两个列表取并集 union
print(list(set(list1).union(set(list2))))


# 获取两个 list 的差集
print(list(set(list1).difference(set(list2))))  # list1 有 list2 中没有的

print(list(set(list2).difference(set(list1))))  # list2 中有 list1 中没有的
