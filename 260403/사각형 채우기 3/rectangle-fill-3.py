n = int(input())

# Please write your code here.
dp = [0] * 1001

dp[1] = 2
dp[2] = 7

for i in range(3, n+1):
    dp[n] = ((dp[n-1]*2) + (dp[n-2]*4)) % 1_000_000_007

print(dp[n])