

# 判断元素是否是列表中
from _bisect import bisect_left

lst = [1, 3, 4, 5, 7, 8]
for i in lst:
    if i == 8:
        print('存在')


if 4 in lst:
    print('存在')

# set / bisect ==============================
list_set = [1, 6, 3, 5, 3, 4]
list_bisect = [1, 6, 3, 5, 3, 4]

lst = set(list_set)
print(lst)
for i in lst:
    if i == 6:
        print('存在')

if 4 in lst:
    print('存在')

list_bisect.sort()
if bisect_left(list_bisect, 6):
    print('存在')

