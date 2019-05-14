

def common_divisor(x, y):
    if x > y:
        minimum = y
    else:
        minimum = x

    for i in range(1, minimum+1):
        if (x % i == 0) and (y % i == 0):
            common_num = i
    return common_num


print('两数的最大公约数为:{}'.format(common_divisor(54, 24)))


# 公约数
# for i in range(1, 55):
#     if 54 % i == 0:
#         print(i)


def lcm(x, y):
    if x > y:
        bigger_num = x
    else:
        bigger_num = y

    while True:
        if (bigger_num % x == 0) and (bigger_num % y == 0):
            return bigger_num
            break

        else:
            bigger_num += 1


num = lcm(24, 54)
print('两数的最小公倍数为:{}'.format(num))
