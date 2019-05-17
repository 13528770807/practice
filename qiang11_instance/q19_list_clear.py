

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst)
lst.clear()
print(lst)


# copy
def copylist(lst):
    new_lst = lst[:]
    return new_lst


li = [1, 2, 3, 4, 5, 6, 7]
print("原列表:", li)
print('现列表:', copylist(li))


# extend()  =====================
def li_extend(lst):
    li_copy = []
    li_copy.extend(lst)
    return li_copy


li = [22, 33, 4, 88, 99]
new_li = li_extend(li)
print('原列表:', li)
print('新列表:', new_li)


# list()  ======================
def list_copy2(li):
    cp_list = list(li)
    return cp_list


li = [1, 3, 4, 6, 7, 9]
li2 = list_copy2(li)
print('原列表:', li)
print('新列表:', li2)
