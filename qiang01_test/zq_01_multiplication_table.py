# 乘法表
for k in range(1, 10):
    for i in range(1, k+1):
        print('%d*%d=%02d' % (i, k, k*i), end=' ')
    print('')
