n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# Please write your code here.
cnt=0
for i in range(n-1, -1, -1):
    if coins[i]<=k:
        cnt+=k//coins[i]
        k = k%coins[i]
print(cnt)