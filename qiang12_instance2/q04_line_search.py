

def search(arr, x, n):
    for i in range(n):
        if arr[i] == x:
            print('exist')
            return i
    else:
        return -1


if __name__ == "__main__":
    arr = ['A', 'B', 'C', 'D', 'E']
    x = 'E'
    n = len(arr)
    result = search(arr, x, n)
    if result != -1:
        print('存在,查找的索引为:{}'.format(result))
    else:
        print('不存在')
