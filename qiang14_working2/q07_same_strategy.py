

# 61、简述同源策略
"""
 同源策略需要同时满足以下三点要求：
1）协议相同
2）域名相同
3）端口相同

 http:www.test.com与https:www.test.com 不同源——协议不同
 http:www.test.com与http:www.admin.com 不同源——域名不同
 http:www.test.com与http:www.test.com:8081 不同源——端口不同
 只要不满足其中任意一个要求，就不符合同源策略，就会出现“跨域”
"""


# 62、简述cookie和session的区别
import copy

"""
1，session 在服务器端，cookie 在客户端（浏览器）
2、session 的运行依赖 session id，而 session id 是存在 cookie 中的，也就是说，
如果浏览器禁用了 cookie ，同时 session 也会失效，存储Session时，键与Cookie中的sessionid相同，
值是开发人员设置的键值对信息，进行了base64编码，过期时间由开发人员设置
3、cookie安全性比session差
"""


# 63、简述多线程、多进程
"""
进程：
1、操作系统进行资源分配和调度的基本单位，多个进程之间相互独立
2、稳定性好，如果一个进程崩溃，不影响其他进程，但是进程消耗资源大，开启的进程数量有限制

线程：
1、CPU进行资源分配和调度的基本单位，线程是进程的一部分，是比进程更小的能独立运行的基本单位，
一个进程下的多个线程可以共享该进程的所有资源
2、如果IO操作密集，则可以多线程运行效率高，缺点是如果一个线程崩溃，都会造成进程的崩溃

应用：
IO密集的用多线程，在用户输入，sleep 时候，可以切换到其他线程执行，减少等待的时间
CPU密集的用多进程，因为假如IO操作少，用多线程的话，因为线程共享一个全局解释器锁，当前运行的线程会霸占GIL，
其他线程没有GIL，就不能充分利用多核CPU的优势
"""


# 64、简述any()和all()方法
"""
any():只要迭代器中有一个元素为真就为真
all():迭代器中所有的判断项返回都是真，结果才为真
python中什么元素为假？
答案：（0，空字符串，空列表、空字典、空元组、None, False）
"""

print(any([1, 2, 3]))  # True
print(all([1, 2, 3]))  # True
print(all([1, 2, 0]))  # False
print(bool(0))  # False
print(bool(''))  # False
print(bool({}))  # False
print(bool([]))  # False
print(bool(()))  # False
print(bool(None))  # False


a = [True, False]
print(any(a))  # True
print(all(a))  # False
b = ''
print(any(b))  # False
c = ['good', 'built', 'bad']
print(all(c))  #True
print(all("b"))  # True "b"为字符串
print(any("b"))  # True "b"为字符串
d = ['good', 'built', 'bad', '']
print(d)  # ['good', 'built', 'bad', '']
print(all(d))  # False


# 65、IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常
"""
IOError：输入输出异常
AttributeError：试图访问一个对象没有的属性
ImportError：无法引入模块或包，基本是路径问题
IndentationError：语法错误，代码没有正确的对齐
IndexError：下标索引超出序列边界
KeyError:试图访问你字典里不存在的键
SyntaxError:Python代码逻辑语法出错，不能执行
NameError:使用一个还未赋予对象的变量
"""


# 66、python中copy和deepcopy区别
"""
1、复制不可变数据类型，不管copy还是deepcopy,都是同一个地址当浅复制的值是不可变对象
（数值，字符串，元组）时和=“赋值”的情况一样，对象的id值与浅复制原来的值相同。

2、复制的值是可变对象（列表和字典）
浅拷贝copy有两种情况：
第一种情况：复制的 对象中无 复杂 子对象，原来值的改变并不会影响浅复制的值，同时浅复制的值改变也并不会影响原来的值。原来值的id值与浅复制原来的值不同。
第二种情况：复制的对象中有 复杂 子对象 （例如列表中的一个子元素是一个列表）， 改变原来的值 中的复杂子对象的值  ，会影响浅复制的值。
深拷贝deepcopy：完全复制独立，包括内层列表和字典
"""
h = 'zhang'
i = h
j = copy.copy(h)
k = copy.deepcopy(h)
print(h, id(h))  # zhang 139883821544760
print(i, id(i))  # zhang 139883821544760
print(j, id(j))  # zhang 139883821544760
print(k, id(k))  # zhang 139883821544760


li1 = [1, 2, 3, 4, 5]
e = copy.copy(li1)
f = copy.deepcopy(li1)
li1.append(6)
print(li1, id(li1))  # [1, 2, 3, 4, 5, 6] 139927175333768
print(e, id(e))  # [1, 2, 3, 4, 5, 6] 139680848638344
print(f, id(f))  # [1, 2, 3, 4, 5] 139680908423112

li2 = [1, 2, 3, [3, 5, 6], [7, 8]]
l = copy.copy(li2)
m = copy.deepcopy(li2)
li2[3].append(9)
print(li2, id(li2))  # [1, 2, 3, [3, 5, 6, 9], [7, 8]] 139927175355592
print(l, id(l))  # [1, 2, 3, [3, 5, 6, 9], [7, 8]] 139927169888648
print(m, id(m))  # [1, 2, 3, [3, 5, 6], [7, 8]] 139927174931016


# 67、列出几种魔法方法并简要介绍用途
"""
__init__:对象初始化方法
__new__:创建对象时候执行的方法，单列模式会用到
__str__:当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
__del__:删除对象执行的方法
"""


# 68、C:\Users\ry-wu.junya\Desktop>python 1.py 22 33命令行启动程序并传参，print(sys.argv)会输出什么数据？
# 文件名和参数构成的列表


# 69, 将 [x for x in range(3)] 改成生成器
o = (x for x in range(3))  # 将[]改成()
print(type(o))  # <class 'generator'>  # 函数出现yield 即生成器


# 70 a = ' hahhaa '  去除尾部空格
str1 = ' hhahhahhaha '
res = str1.strip()
print(res)  # hhahhahhaha

