import sys
n=int(input())
height = [int(input()) for _ in range(n)]
# Please write your code here.
ans=sys.maxsize
for minimum in range(101):
    maximum = 17 + minimum
    if maximum>100:
        break
    cost=0
    for i in range(n):
        if height[i]>maximum:
            cost+=((height[i]-maximum)*(height[i]-maximum))
        elif height[i]<minimum:
            cost+=((minimum-height[i])*(minimum-height[i]))
    ans = min(cost, ans)

print(ans)
