

b = 'hello,wor*ldhh'  # 字符串内指定符号切割
print(b.split("*"))   # ['hello,wor', 'ldhh']

li = list()
a = ["啊啊啊啊啊", "呃呃呃。鹅鹅鹅鹅鹅鹅饿"]  # 列表内指定符号切割
for i in range(0, len(a)):
    # li.append(a[i].split("。"))
    li = li + a[i].split('。')

print(li)

lis = ['aaaj']
lis = lis + ['bbb']  # 列表可以用 "+" 号相加 相当于 extend() 方法
print(lis)

li1 = [1, 2, 3]
li2 = [6, 7, 8, 9]
# li1.append(li2)
print(li1)  # [1, 2, 3, [6, 7, 8, 9]]
# li1.extend(li2)
print(li1)  # [1, 2, 3, 6, 7, 8, 9]
li1 = li1 + li2
print(li1)  # [1, 2, 3, 6, 7, 8, 9]
