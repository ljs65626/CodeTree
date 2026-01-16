n=int(input())
arr = list(map(int, input().split()))


def select_pivot(arr, low, high):
    left = low
    right = high
    mid = (low+high)//2

    if arr[left]<=arr[mid]<=arr[right] or arr[right]<=arr[mid]<=arr[left]:
        return mid
    elif arr[mid]<=arr[left]<=arr[right] or arr[right]<=arr[left]<=arr[mid]:
        return left
    else:
        return right


def partition(arr, low, high):
    pivot_index = select_pivot(arr, low, high)
    pivot = arr[pivot_index]
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    i=low-1
    for j in range(low, high):
        if arr[j]<pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

def quick_sort(arr, low, high):
    if low<high:
        pos = partition(arr, low, high)
        quick_sort(arr, low, pos-1)
        quick_sort(arr, pos+1, high)

quick_sort(arr, 0, n-1)

for i in arr:
    print(i, end=' ')