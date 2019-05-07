class MyNumbers():
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


mynumber = MyNumbers()
# mynumber.__iter__()
# print(mynumber.__next__())
# print(mynumber.__next__())
# print(mynumber.__next__())
num = iter(mynumber)
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
