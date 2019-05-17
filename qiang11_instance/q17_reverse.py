

def list_reverse(li, start, end):
    temp = li[start]
    li[start] = li[end]
    li[end] = temp
    return li


li = [1, 2, 3]
res_li = list_reverse(li, 0, len(li)-1)
print(res_li)


def list_reverse2(li):
    li[0], li[-1] = li[-1], li[0]
    return li


li = [1, 2, 3]
print(list_reverse2(li))



