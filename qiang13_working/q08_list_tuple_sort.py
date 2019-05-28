
# 列表内元阻排序
lst3 = [("A", 1), ("C", 18), ("F", 9), ("B", 2)]
lst3.sort(key=lambda x: x[0], reverse=True)  # 列表中的元阻第一位降序排序
resul = sorted(lst3, key=lambda a: a[1])  # 列表中的元阻第二位升序排序
print('lst3:', lst3)
print('resul:', resul)