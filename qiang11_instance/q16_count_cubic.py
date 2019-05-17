# 计算 n 个自然数的立方和


def count_cubic(num):
    sum = 0
    for i in range(num+1):
        sum += i**3
    return sum


# num = int(input('请输入数字'))
num = 5
num_cubic = count_cubic(num)
print(num_cubic)  # 255


# 计算数组元素之和
def _sum(arr, n):
    return sum(arr), len(n)


ali = [1, 2, 3, 4]
print(_sum(ali, ali))


# 数组翻转指定个数的元素
def leftRotate(arr, t, l):
    for i in range(t):
        leftRotatebyOne(arr, l)


def leftRotatebyOne(arr, l):
    temp = arr[0]
    for i in range(l-1):
        arr[i] = arr[i+1]
    arr[l-1] = temp


def printArray(arr, l):
    for i in range(l):
        print('{}'.format(arr[i]), end=' ')


arr = [1, 2, 3, 4, 5, 6, 7, 8]
result_arr = leftRotate(arr, 3, len(arr))
print(arr)
printArray(arr, len(arr))

print()
print('%.3f' % (6 % 108))  # a%b 如果b不为0 结果为a


# instance2
print('instance2'+'='*60)


def leftRotate2(li, n, l):
    for i in range(gcd(n, l)):
        print(i)
        temp = li[i]  # 1, 2
        j = i  # 0, 1
        while True:
            k = j + n  # k = 2, 3
            if k >= n:
                k = k - n  # 0, 1
            if k == i:
                break
            li[j] = li[k]
            j = k
        li[j] = temp
    return li


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(a, a % b)


arr2 = [1, 2, 3, 4, 5, 6, 7, 8]
print(gcd(2, len(arr2)))
result_li = leftRotate2(arr2, 2, len(arr2))
print(result_li)

print('='*60)


def reverseArray(li, start, end):
    while start < end:
        temp = li[start]
        li[start] = li[end]
        li[end] = temp
        start += 1
        end -= 1


def leftRotate(li, n):
    reverseArray(li, 0, n-1)
    reverseArray(li, n, len(li)-1)
    reverseArray(li, 0, len(li)-1)


def printArray(li):
    for i in range(0, len(li)):
        print('{}'.format(li[i]), end=' ')


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_li3 = leftRotate(li, 3)
printArray(li)

