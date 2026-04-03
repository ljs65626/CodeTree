N = int(input())

# Please write your code here.
# N-2 or N-3까지 올라올 수 있어야 한다.


dp = [0] * 1001
dp[0]=1
dp[1]=0
dp[2]=1
dp[3]=1

for i in range(4, N+1):
    dp[i] = (dp[i-2] + dp[i-3]) %10007
print(dp[N])