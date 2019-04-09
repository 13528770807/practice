
# 去重
list1 = [1, 2, 3, 1, 2, 3]
set2 = set(list1)
print(set2)  # {1, 2, 3}

# 增加
set2.add('a')
print(set2)   # {1, 2, 3, 'a'}

# 迭代增加
set2.update('bcdef')
print(set2)  # {'f', 1, 2, 3, 'b', 'a', 'c', 'd', 'e'}

# 集合删除(随机)
set2.pop()
print(set2)  # {1, 2, 3, 'b', 'a', 'c', 'd', 'e'}

# 遍历
# for i in l2:
    # print(i)

# 交集
set3 = {1, 2, 3, 4, 5}
set4 = {2, 3, 4, 5, 6, 7, 8}
set5 = set3 & set4
print(set5)  # {2, 3, 4, 5}

# 并集
set6 = set3 | set4
print(set6)  # {1, 2, 3, 4, 5, 6, 7, 8}

# 反交集
set7 = set3 ^ set4
print(set7)  # {1, 6, 7, 8}

# 差集
set8 = set4 - set3
print(set8)  # {8, 6, 7}
set9 = set3 - set4
print(set9)  # {1}

# 超集
set10 = set4 > set3
print(set10)  # False
set11 = set3 > set4
print(set11)  # False
