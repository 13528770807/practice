import sys

ali = [1, 2, 3, 4, 5]
it = iter(ali)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()




