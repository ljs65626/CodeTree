n = int(input())
arr1 = list(map(int, input().split()))
set1 = set(arr1)

m = int(input())
arr2 = list(map(int, input().split()))

# Please write your code here.

for i in arr2:
    if i in set1:
        print(1, end=' ')
    else:
        print(0, end=' ')