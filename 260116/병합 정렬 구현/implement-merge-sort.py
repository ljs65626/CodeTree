n=int(input())
arr = list(map(int, input().split()))

merge_arr=[0]*n

def merge(arr, low, mid, high):
    i=low
    j=mid+1
    k=low
    while i<=mid and j<=high:
        if arr[i]<arr[j]:
            merge_arr[k] = arr[i]
            i+=1
        else:
            merge_arr[k] = arr[j]
            j+=1
        k+=1
    
    while i<=mid:
        merge_arr[k] = arr[i]
        i+=1
        k+=1
    while j<=high:
        merge_arr[k] = arr[j]
        j+=1
        k+=1

    for l in range(low, high+1):
        arr[l] = merge_arr[l]
    
def merge_sort(arr, low, high):
    if low<high:
        mid = (low+high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)


merge_sort(arr, 0, n-1)
for i in arr:
    print(i, end=' ')