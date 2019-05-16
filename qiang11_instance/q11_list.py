

# list 定义
ali = ["a", "b", "mpilgrim", "z", "example"]
print(ali)         # ["a", "b", "mpilgrim", "z", "example"]
print(ali[1])      # b


# list 负数
print('负数', '='*60)
print(ali[-1])     # example
print(ali[-3])     # mpilgrim
print(ali)         # ['a', 'b', 'mpilgrim', 'z', 'example']
print(ali[1:3])    # ['b', 'mpilgrim']
print(ali[1:-1])   # ['b', 'mpilgrim', 'z']
print(ali[0:3])    # ['a', 'b', 'mpilgrim']


# list 增加元素
print('增加元素'+'='*60)
ali.append('new')
print(ali)         # ['a', 'b', 'mpilgrim', 'z', 'example', 'new']
ali.insert(1, 'new')
print(ali)         # ['a', 'new', 'b', 'mpilgrim', 'z', 'example', 'new']
ali.extend(['two', 'elements'])
print(ali)         # ['a', 'new', 'b', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']


# list 搜索
print('搜索'+'='*60)
print(ali)         # ['a', 'new', 'b', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
print(ali.index('two'))  # 7
print(ali.index('b'))    # 2
print(ali.index('new'))  # 1 优先获取前面的索引


# list 删除元素
print('删除元素'+'='*60)
print(ali)         # ['a', 'new', 'b', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
ali.remove('z')
print(ali)         # ['a', 'new', 'b', 'mpilgrim', 'example', 'new', 'two', 'elements']
ali.remove('new')  # 删除首个出现的一个值
print(ali)         # ['a', 'b', 'mpilgrim', 'example', 'new', 'two', 'elements']
print(ali.pop())   # 删除最后一个元素, 返回删除元素的值
print(ali)


# list 运算符
print('运算符'+'='*60)
ali2 = ['a', 'b', 'mpilgrim']
ali2 = ali2 + ['example', 'new']
print(ali2)        # ['a', 'b', 'mpilgrim', 'example', 'new']
ali2 += ['two']
print(ali2)        # ['a', 'b', 'mpilgrim', 'example', 'new', 'two']
ali3 = [1, 2, 3]
ali3 = ali3 * 3
print(ali3)        # [1, 2, 3, 1, 2, 3, 1, 2, 3]


# 使用 join 链接 list 成为字符串
print('列表转字符串'+'='*60)
params = {'name': 'zhangsan', 'age': 18, 'gender': 'man'}
resutl = ['{}={}'.format(k, v) for k, v in params.items()]
print(resutl)      # ['age=18', 'name=zhangsan', 'gender=man']
list_to_str = ';'.join(resutl)  # jion 只能用于元素是字符串的 list
print(type(list_to_str), list_to_str)  # <class 'str'> age=18;name=zhangsan;gender=man


# list 分割字符串
print('分割字符串'+'='*60)
ali4 = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
result4 = ';'.join(ali4)
print(result4)  # server=mpilgrim;uid=sa;database=master;pwd=secret
ali5 = result4.split(';')  # 将字符串分割成列表
print(ali5)     # ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
ali5 = result4.split(';', 1)
print(ali5)     # ['server=mpilgrim', 'uid=sa;database=master;pwd=secret']


# list 的映射解析
print('映射解析'+'='*60)
li = [1, 2,  3, 4, 5]
result = [i*2 for i in li]
print(result)   # [2, 4, 6, 8, 10]


# dictionary 中的解析
print('dictionary 中的解析'+'='*60)
params2 = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
print(params2.keys())     # dict_keys(['server', 'uid', 'pwd', 'database'])
print(params2.values())   # dict_values(['sa', 'mpilgrim', 'secret', 'master'])
print(params2.items())    # dict_items([('server', 'mpilgrim'), ('pwd', 'secret'), ('uid', 'sa'), ('database', 'master')])

result_key = [k for k in params2.keys()]
print(result_key)         # ['database', 'uid', 'pwd', 'server']
result_value = [v for v in params2.values()]
print(result_value)       # ['master', 'sa', 'secret', 'mpilgrim']
result_items = ['%s=%s' % (k, v) for k, v in params2.items()]
print(result_items)       # ['database=master', 'uid=sa', 'pwd=secret', 'server=mpilgrim']


# list 过滤
print('list 过滤 '+'='*60)
ali6 = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
result6 = [i for i in ali6 if len(i) > 1]
print(result6)            # ['mpilgrim', 'foo']
result7 = [i for i in ali6 if i != 'b']
print(result7)            # ['a', 'mpilgrim', 'foo', 'c', 'd', 'd']

result8 = [i for i in ali6 if ali6.count(i) == 1]
print(result8)            # ['a', 'mpilgrim', 'foo', 'c']
