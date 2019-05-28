

#合并两个列表，相同的不要
li1 = [1, 2, 34, 5, 6]
li2 = [2, 3, 4, 5, 67, 8, 89, 9, 34]

# for i in range(len(li1)):
#     if li1[i] not in li2:
#         li2.append(li1[i])
#
# print(li2)


# TODO
# li1.extend(li2)
# print('li1==>', li1)
# for i in range(len(li1)):
#     print(i)
#     if li1.count(li1[i]) > 1:
#         print('remove:', li1[i])
#         li1.remove(li1[i])
#
# print('result:', li1)


# li1.extend(li2)
# i = 0
# while i < len(li1):
#     for j in li1:
#         while li1.count(j) > 1:
#             li1.remove(j)
#         i = i + 1
#     print(li1)

# li3 = [1, 2, 3]
# li3.remove(3)
# print(li3)
