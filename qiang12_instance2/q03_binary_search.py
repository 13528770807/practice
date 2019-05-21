

def dinarySearch(arr, l, r, n):
    if r >= l:
        mid = (l + r) // 2
        if arr[mid] == n:
            print('exist')
            return mid
        elif arr[mid] > n:
            return dinarySearch(arr, 0, mid-1, n)
        else:
            return dinarySearch(arr, mid+1, r, n)
    else:
        return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    n = 10
    result = dinarySearch(arr, 0, len(arr)-1, n)
    if result == -1:
        print('元素不存在')
    else:
        print('元素存在,查找元素的索引为:{}'.format(result))


"""
# 返回 x 在 arr 中的索引，如果不存在返回 -1
def binarySearch(arr, l, r, x):
    # 基本判断
    if r >= l:

        mid = int(l + (r - l) / 2)

        # 元素整好的中间位置
        if arr[mid] == x:
            return mid

            # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

            # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # 不存在
        return -1


# 测试数组
arr = [2, 3, 4, 10, 40]
x = 10

# 函数调用
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("元素在数组中的索引为 %d" % result)
else:
    print("元素不在数组中") 
"""
