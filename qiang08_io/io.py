hello = "hello\nchina"
print(hello)
print(repr(hello))


for i in range(1, 11):
    print(repr(i).rjust(2), repr(i*i).rjust(3), end=" ")
    print(repr(i**3).rjust(4))


print("="*60)
for i in range(1, 11):
    print("{0:3d}{1:4d}{2:5d}".format(i, i**2, i**3))


print('{}和{}'.format('google', 'runoob'))
print('{0}和{1}'.format('google', 'runoob'))
print('{1}和{0}'.format('google', 'runoob'))


import math
print('pi的值近似为：{0:.3f}'.format(math.pi))


# 字典格式化输出
dic = dict(zhangsan=1, lisi=2, wangwu=3)
# dic = {'zhangsan': 1, 'lisi': 2, 'wangwu': 3}
print(dic)
print('zhangsan:{0[zhangsan]:d}'.format(dic))
print('zhangsan:{0[zhangsan]:d}; lisi:{0[lisi]:d}; wangwu:{0[wangwu]:d}'.format(dic))
print('='*60)
print('wangwu:{wangwu:d}; lisi:{lisi:d}; zhangsan:{zhangsan:d}'.format(**dic))


