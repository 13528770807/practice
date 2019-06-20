

def foo(fun):
    def rapper(*args, **kwrags):
        print('aaa', fun.__name__)
        print('bbb', fun.__dir__)
        return fun(*args, **kwrags)
    return rapper


@foo
def func():
    print('func')
    return 'hahah'


print(func())
