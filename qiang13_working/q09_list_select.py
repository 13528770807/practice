

# l1=[1,2,3,4,5,"4",6,7,8,9......]
# 问:不知道列表长度情况下,写一个函数, 剔除4和"4"

# 方法一 不成立 不使用while循环会漏掉元素
def select_ele(li):
    for i in li:
        if i == 4 or i == "4":
            li.remove(i)
    return li


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5, "4", 6, 7, 8, 9]
    print(select_ele(l1))


# 方法二
def select_ele2(li, n=0):
    while n < len(li):  # 逐个遍历,规避 for 循环漏掉
        for i in li:
            if i == 4 or i == '4':
                li.remove(i)
            n += 1
    return li


l1 = [1, 2, 3, 4, 5, "4", 6, 7, 8, 9]
print(select_ele2(l1))

