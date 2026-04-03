n = int(input())

# Please write your code here.
dp = [0] * 1001
dp[0] = 1
dp[1] = 2
dp[2] = 7
for i in range(3, n+1):
    dp[i] = (3*dp[i-1] + dp[i-2] - dp[i-3]) % 1_000_000_007

print(dp[n])