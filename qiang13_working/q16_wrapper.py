

# 实例一
import time


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
    def inner(*args, **kwargs):  # 闭包函数
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


print('='*60)


def performance(unit):
    def performance_decorator(f):
        def foo(*args, **kwargs):
            start = time.time()
            fun = f(*args, **kwargs)
            end = time.time()
            print('fun_time:%f' % (end - start), unit)
            return fun
        return foo
    return performance_decorator


@performance('zhang')  # 带有参数的装饰器
def test_foo(n):
    fibo_li = list()
    a, b = 0, 1
    for i in range(n):
        fibo_li.append(a)
        a, b = b, a+b
    return fibo_li


print(test_foo(10))


print('*'*60)


from functools import reduce


def performance(unit):
    def performance_decorator(f):
        def p(x):
            t1 = time.time()
            r = f(x)
            t2 = time.time()
            print('call %s() in %f %s' % (f.__name__, t2 - t1, unit))
            return r

        return p

    return performance_decorator


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(4))



