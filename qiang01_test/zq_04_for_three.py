def test(x, y=[]):
    for o in range(x):
        y.append(o)
    print(y)


test(3)
test(1, [3, 2, 1])
test(3)