

# 获取两个list 的交集  intersection
import math

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]


li = [var for var in list1 if var in list2]
print(li)


# 方法二
a = set(list1)
b = set(list2)
print("a & b:", list(a & b))
print(list(set(list1).intersection(set(list2))))


#  给定两个列表取并集 union
print('list1:', set(list1))  # 列表转集合
print('a|b:', a | b)  # 并集

print(list(set(list1).union(set(list2))))


# 获取两个 list 的差集
print('a-b:', a - b)  # 差集: a 中 b 没有的
print(list(set(list1).difference(set(list2))))  # list1 有 list2 中没有的


print('a-b:', list(b - a))
print(list(set(list2).difference(set(list1))))  # list2 中有 list1 中没有的


# 列表嵌套原组排序
a = [(1, 'B'), (1, 'A'), (1, 'C'), (1, 'AC'), (2, 'B'), (2, 'A'), (1, 'ABC')]
# a.sort(reverse=True)
print('sorted:', sorted(a))
print(a)



