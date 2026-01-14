n = int(input())
adjacent = list(map(int, input().split()))

# Please write your code here.

for i in range(1, n+1):
    arr=list()
    arr.append(i)
    for j in range(n-1):
        if abs(adjacent[j]-arr[j])==0:
            break
        arr.append(abs(adjacent[j]-arr[j]))
    arr = set(arr)
    if len(arr)==n:
        break


for i in arr:
    print(i, end=' ')
