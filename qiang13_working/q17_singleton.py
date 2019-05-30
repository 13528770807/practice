

# todo
# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
#         return cls._instance
#
#
# if __name__ == "__main__":
#     class Son(Singleton):
#         def __init__(self, s):
#             self.s = s
#
#
#     a = Son('aaa')
#     b = Son('bbb')
#     print(a.s)
#     print(b.s)

