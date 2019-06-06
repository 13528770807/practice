

# 51、正则匹配，匹配日期2018-03-20
import re

# method 1
url = 'https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
res = re.findall(r'(\d+-\d+-\d+)', url)
print(res)  # ['2018-03-20', '2018-03-20']

# method 2
res1 = re.findall(r'dateRange=(.*?)%7C(.*?)&', url)
print(res1)  # [('2018-03-20', '2018-03-20')]


# 52, list = [2,4,3,5,1,8,9] can not use sort()
# method 1
li = [2, 4, 3, 5, 1, 8, 9]
for i in range(len(li)-1, 0, -1):
    for j in range(i):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]

print(li)  # [1, 2, 3, 4, 5, 8, 9]


# method 2
li1 = [2, 4, 3, 5, 1, 8, 9]
for i in range(len(li)-1):
    for j in range(len(li)-1-i):
        if li1[j] > li1[j+1]:
            li1[j], li1[j+1] = li1[j+1], li1[j]

print(li1)  # [1, 2, 3, 4, 5, 8, 9]


# method 3
li1 = [2, 4, 3, 5, 1, 8, 9]
new_li1 = []


def foo(li):
    m = min(li)
    new_li1.append(m)
    li1.remove(m)
    if len(li) != 0:
        foo(li)
    return new_li1


print(foo(li1))  # [1, 2, 3, 4, 5, 8, 9]


# 53、写一个单列模式
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, '_inst'):
            # cls._inst = super(Singleton, cls).__new__(cls)
            cls._inst = object.__new__(cls)
        return cls._inst


a = Singleton()
b = Singleton()
print(id(a))  # 139622375921256
print(id(b))  # 139622375921256

a.age = 19
print(a.age)  # 19
print(b.age)  # 19


# 54,保留两位小数  round(数值,保留位数)
num = 12.248388282
num1 = 2.248388282
print('num:%.2f' % num)  # num:12.25
print('num:%0.2f' % num1)  # num:2.25

print(round(num, 1))  # 12.2
print(round(num, 2))  # 12.25
print(round(num1, 1))  # 2.2
print(round(num1, 2))  # 2.25


# 55、求三个方法打印结果
"""
fn("one",1）直接将键值对传给字典；
fn("two",2)因为字典在内存中是可变数据类型，所以指向同一个地址，传了新的额参数后，会相当于给字典增加键值对
fn("three",3,{})因为传了一个新字典，所以不再是原先默认参数的字典
"""
dic1 = {}


def foo(k, v, dic1={}):
    dic1[k] = v
    print(dic1)


foo('one', 1)
foo('two', 2)
foo('three', 3, {})
print('='*60)


# 56、列出常见的状态码和意义
"""
200 OK 
请求正常处理完毕

204 No Content 
请求成功处理，没有实体的主体返回

206 Partial Content 
GET范围请求已成功处理

301 Moved Permanently 
永久重定向，资源已永久分配新URI

302 Found 
临时重定向，资源已临时分配新URI

303 See Other 
临时重定向，期望使用GET定向获取

304 Not Modified 
发送的附带条件请求未满足

307 Temporary Redirect 
临时重定向，POST不会变成GET

400 Bad Request 
请求报文语法错误或参数错误

401 Unauthorized 
需要通过HTTP认证，或认证失败

403 Forbidden 
请求资源被拒绝

404 Not Found 
无法找到请求资源（服务器无理由拒绝）

500 Internal Server Error 
服务器故障或Web应用故障

503 Service Unavailable 
服务器超负载或停机维护
"""


# 57、分别从前端、后端、数据库阐述web项目的性能优化
'''
前端优化：
1、减少http请求、例如制作精灵图
2、html和CSS放在页面上部，javascript放在页面下面，因为js加载比HTML和Css加载慢，
所以要优先加载html和css,以防页面显示不全，性能差，也影响用户体验差

 
后端优化：
1、缓存存储读写次数高，变化少的数据，比如网站首页的信息、商品的信息等。应用程序读取数据时，
一般是先从缓存中读取，如果读取不到或数据已失效，再访问磁盘数据库，并将数据再次写入缓存。
2、异步方式，如果有耗时操作，可以采用异步，比如celery
3、代码优化，避免循环和判断次数太多，如果多个if else判断，优先判断最有可能先发生的情况

 
数据库优化：
1、如有条件，数据可以存放于redis，读取速度快
2、建立索引、外键等
'''


# 58、使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
dic = {"name": "zs", "age": 18}
dic1 = {"name": "zs", "age": 18}
dic.pop('name')
print(dic)
del dic1['name']
print(dic1)


# 59、列出常见MYSQL数据存储引擎
"""
InnoDB：支持事务处理，支持外键，支持崩溃修复能力和并发控制。如果需要对事务的完整性要求比较高（比如银行），
要求实现并发控制（比如售票），那选择InnoDB有很大的优势。如果需要频繁的更新、删除操作的数据库，也可以选择InnoDB，
因为支持事务的提交（commit）和回滚（rollback）。 

MyISAM：插入数据快，空间和内存使用比较低。如果表主要是用于插入新记录和读出记录，
那么选择MyISAM能实现处理高效率。如果应用的完整性、并发性要求比 较低，也可以使用。

MEMORY：所有的数据都在内存中，数据的处理速度快，但是安全性不高。如果需要很快的读写速度，
对数据的安全性要求较低，可以选择MEMOEY。它对表的大小有要求，不能建立太大的表。所以，这类数据库只使用在相对较小的数据库表。
"""


# 60, zip() 函数
a = zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5))
a1 = dict(a)
print('a:', a1)  # a: {'e': 5, 'a': 1, 'c': 3, 'b': 2, 'd': 4}

print(list(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5))))  # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

# num2 = range(10)
# res = [x for x in num if x in a1]
# print(res)

res2 = [a1[x] for x in a1]
print(res2)


# dict() 创建新字典
di = dict([['name', 'zhangsna'], ['age', 18]])
print(di)
di1 = dict([('name', 'lisi'), ('age', 19)])
print(di1)
