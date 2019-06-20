

l = [x for x in range(11)]
print(l)

g = (x for x in range(11))  # [] 将表达式改成 () 即为生成器
print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

for i in g:
    print('i:', i)

print('*'*60)


def fibo(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n += 1


fi = fibo(10)  # 生成器调用next()开始执行, 遇yield 返回并中断, next()再次执行时从yield返回的位置开始执行
print(fi.__next__())
print(fi.__next__())
print(fi.__next__())
print(fi.__next__())
print(fi.__next__())
print(fi.__next__())
print(fi.__next__())


def add():
    print('sleep 1')
    yield 1
    print('sleep 2')
    yield 3
    print('sleep 3')
    yield 5


a = add()
print(a)
print('one=====>', a.__next__())
print('two=====>', a.__next__())
print('three=====>', a.__next__())



