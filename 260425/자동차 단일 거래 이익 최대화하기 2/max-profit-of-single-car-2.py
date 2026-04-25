n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
ans = 0
first = 0
for i in range(1, n):
    if arr[i]<arr[i-1]:
        diff=0
        first = i 
    else:
        end = i
        diff = arr[end] - arr[first]
        ans = max(diff, ans)
    
print(ans)