
'''
30 个人在一条船上，超载，需要 15 人下船。

于是人们排成一队，排队的位置即为他们的编号。

报数，从 1 开始，数到 9 的人下船。

如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？'''


people = dict()  # 创建字典,用于标记
for i in range(1, 31):
    people[i] = 'in'

print(people)
check = 0  # 塞选下船人的编号
m = 1  # 控制整体循环
o = 0  # 记录下船人数
while m <= 31:
    if m == 31:
        m = 1
    elif o == 15:
        break
    else:
        if people[m] == 'out':
            m += 1
            continue
        else:
            check += 1
            if check == 9:
                people[m] = 'out'
                check = 0
                print('{} 下船了'.format(m))
                o += 1
            else:
                m += 1
                continue




