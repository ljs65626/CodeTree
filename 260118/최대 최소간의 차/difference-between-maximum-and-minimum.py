import sys
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
def get_cost(low, high):
    cost=0
    for i in range(n):
        if arr[i]>high:
            cost+=(arr[i]-high)
        elif arr[i]<low:
            cost+=(low-arr[i])
    
    return cost


ans=sys.maxsize
for mini in range(1, 10001):
    cost = get_cost(mini, mini+k)
    
    ans = min(cost, ans)

print(ans)