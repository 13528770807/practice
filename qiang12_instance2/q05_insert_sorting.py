

# 插入排序（英语：Insertion Sort）是一种简单直观的排序算法。它的工作原理是通过构建有序序列，
# 对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。


def insertSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:  # 判断索引大于0, 第二个数小于第一个数(第一个数大于第二个数)
            arr[j+1] = arr[j]  # 第一个数往后移(前一个数)
            j -= 1
        arr[j+1] = key  # 当条件不成立之后 赋值


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6]
    insertSort(arr)
    print(arr)


