import sys
n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
ans=sys.maxsize
for i in range(n):
    ans = min(ans, abs(arr[i]-arr[i+n]))

print(ans)