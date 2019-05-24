

def bubbling_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubbling_sort(arr)
    print(arr)
