n=int(input())
arr = [0] + list(map(int, input().split()))

def heapify(arr, n, i):
    biggest=i
    left = i*2
    right=i*2+1

    if left<=n and arr[left]>arr[biggest]:
        biggest=left
    
    if right<=n and arr[right]>arr[biggest]:
        biggest=right

    if biggest!=i:
        arr[i], arr[biggest] = arr[biggest], arr[i]
        heapify(arr, n, biggest)


def heap_sort(arr, n):
    for i in range(n//2, 0, -1):
        heapify(arr, n, i)
    
    while n>1:
        arr[1], arr[n] = arr[n], arr[1]
        n-=1
        heapify(arr, n, 1)


heap_sort(arr, n)

for i in range(1, n+1):
    print(arr[i], end=' ')