

def list_reverse(ali, start, end):
    temp = ali[start]
    ali[start] = ali[end]
    ali[end] = temp
    return ali


li = [1, 2, 3]
res_li = list_reverse(li, 0, len(li)-1)
print(res_li)  # [3, 2, 1]


def list_reverse2(ali):
    ali[0], ali[-1] = ali[-1], ali[0]
    return ali


li = [1, 2, 3]
print(list_reverse2(li))  # [3, 2, 1]


# 指定两元素对调 ============================
def element_refore(ali, s, e):
    ali[s], ali[e] = ali[e], ali[s]
    return ali


li2 = [11, 22, 33, 44]
num1 = li2.index(11)
num2 = li2.index(33)
res_li2 = element_refore(li2, num1, num2)
print(res_li2)  # [33, 22, 11, 44]


# instance2 ==============================
def element_refore2(ali, f, s):
    first_ele = ali.pop(f)
    second_ele = ali.pop(s - 1)

    ali.insert(f, second_ele)
    ali.insert(s, first_ele)

    return ali


li3 = [55, 66, 77, 88]
num3 = 1
num4 = 3
res_li3 = element_refore2(li3, num3-1, num4-1)
print(res_li3)  # [77, 66, 55, 88]


# reverse ========================================
def li_reversed(ali):
    return [ele for ele in reversed(ali)]


lst = [10, 11, 12, 13, 14, 15]
print(li_reversed(lst))  # [15, 14, 13, 12, 11, 10]


# instance2 ============================================
def li_reversed2(ali):
    ali.reverse()
    return ali


lst2 = [10, 11, 12, 13, 14, 15, 16]
print(li_reversed2(lst2))  # [16, 15, 14, 13, 12, 11, 10]


# instance3 =========================================
def li_reversed3(ali):
    new_lst = ali[::-1]
    return new_lst


lst3 = [33, 66, 88, 99]
print(li_reversed3(lst3))  # [99, 88, 66, 33]
