

# 使用 update() 方法，第二个参数合并第一个参数
def Merge(dic1, dic2):
    return dic1.update(dic2)


dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
print(Merge(dict1, dict2))  # 返回 None
print(dict1)  # {'c': 4, 'b': 8, 'd': 6, 'a': 10}


# 使用 **，函数将参数以字典的形式导入
def Merge2(dic3, dic4):
    print(dic3)
    print({**dic3})
    res = {**dic3, **dic4}
    return res


dict3 = {'a': 10, 'b': 8}
dict4 = {'d': 6, 'c': 4}
print(Merge2(dict3, dict4))
