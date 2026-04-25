n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
ans = 0
first = 0
before_first=0
for i in range(1, n):
    if arr[i]<arr[i-1]:
        diff=0
        if arr[before_first] > arr[first]:
            before_first = first
        first = i 
    else:
        end = i
        if arr[before_first] < arr[first]:
            first = before_first
        diff = arr[end] - arr[first]
        ans = max(diff, ans)
    
print(ans)