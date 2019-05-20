

# 将字符串作为代码执行
def exec_code():
    Code = '''

for i in range(101):
    print(i, end=' ')
print()
    
    '''
    exec(Code)


exec_code()


# 字符串翻转
str = 'Zhangqiang'
print(str[::-1])

print(type(str))
print(reversed(str))
print(''.join(str))
print(''.join(reversed(str)))


# 对字符串切片及翻转
def reverse1(str2, num=2):
    Lfirst = str2[0: num]
    Lsecond = str2[num: len(str2)]
    Rfirst = str2[0:-num]
    Rsecond = str2[-num:len(str2)]

    print('Rfirst:', Rfirst)  # Rfirst: Runo
    print('Rsecond:', Rsecond)  # Rsecond: ob
    print('times1:', Lsecond + Lfirst)  # times1: noobRu
    print('times2:', Rsecond + Rfirst)  # times2: obRuno


if __name__ == "__main__":
    str2 = 'Runoob'
    reverse1(str2)


# 按键(key)或值(value)对字典进行排序
def sorted_dict():
    key_value = dict()
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[8] = 18
    key_value[3] = 323

    print('按键排序:', key_value)
    print(sorted(key_value))

    for i in sorted(key_value):
        print('sorted:', (i, key_value[i]), end=' ')
    print()

    print('items_value:', sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))


sorted_dict()


# 字典列表排序
lis = [{"name": "Taobao", "age": 100},
{"name": "Runoob", "age": 7},
{"name": "Google", "age": 100},
{"name": "Wiki", "age": 200}]

print('sorted_age:', sorted(lis, key=lambda i: i['age']))
print('\r')
print('sorted_age_name:', sorted(lis, key=lambda k: (k['age'], k['name'])))
print('sorted_reverse_by_age:', sorted(lis, key=lambda a: a['age'], reverse=True))


# 计算字典值之和
def dict_sum():
    dict = {'a': 100, 'b': 200, 'c': 300}
    count = 0
    for k, v in dict.items():
        count += v
    print('dict_sum:', count)


dict_sum()


def dict_sum2():
    dict = {'a': 100, 'b': 200, 'c': 300}
    count = 0
    for i in dict:
        count += dict[i]
    print('dict_sum2:', count)


dict_sum2()


# 移除字典键值对
test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}

# del
# del test_dict['Google']

# pop
# pop_value = test_dict.pop('Zhihu')
# print('pop_value:', pop_value)
print(test_dict.pop('ZhangSan', 'None_key'))

print('test_dict:', test_dict)


new_dict = {k: v for k, v in test_dict.items() if k != 'Zhihu'}
print(new_dict)
