

# 实例一
def f1(x):
    print('4 >> x:', x)
    return x * x


def new_fn(f):
    print('1 >> f:', f.__name__)

    def fn(j):
        print('3 >> print ' + f.__name__)
        return f(j)

    return fn


g1 = new_fn(f1)
print('2 >> g1:', g1.__name__)
print('5 >> g1:', g1(5))


# 实例二
def wrapper(fun):  # 把函数foo 做为参数传进来
    def inner(*args, **kwargs):
        print('*args,**kwargs:', *args, **kwargs)  # *args, **kwargs 解包参数
        print('outfun_name:', fun.__name__)  # 主要功能的增加, 获取函数名 等
        return fun(*args, **kwargs)  # 调用原函数并返回
    return inner  # 返回自身函数名


# @wrapper
def foo(n, m):
    print('n:', n)
    print('m:', m)
    return n+m+100


foo1 = wrapper(foo)  # foo1 实际就是 inner ; (foo1对象名,也可以写成 foo)
print(foo1(1, 2))  # 调用 inner 函数
# print(foo(1, 2))