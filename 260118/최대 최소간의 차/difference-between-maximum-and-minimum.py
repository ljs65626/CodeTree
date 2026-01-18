import sys
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

ans=sys.maxsize
for mini in range(1, 10001):
    maxi = k+mini
    if maxi>10000:
        break
    cost=0
    for i in range(n):
        if arr[i]>maxi:
            cost+=(arr[i]-maxi)
        elif arr[i]<mini:
            cost+=(mini-arr[i])
    
    ans = min(cost, ans)

print(ans)