# 计算 n 个自然数的立方和


def count_cubic(num):
    sum = 0
    for i in range(num+1):
        sum += i**3
        print(sum)
    return sum


# num = int(input('请输入数字'))
num = 5
num_cubic = count_cubic(num)
print(num_cubic)  # 255