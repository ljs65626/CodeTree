n = int(input())

# Please write your code here.
# 1. DP[N-1]의 트리들은 반드시 DP[N]의 왼쪽 서브트리에 존재해야한다.
# 2. DP[N] 노드는 반드시 가장 끝 오른쪽에 존재한다.
dp = [0] * 20
dp[0] = 1
dp[1] = 1
dp[2] = 2


for i in range(3, 20):
    sum_val=0
    for j in range(i):
        sum_val += dp[j] * dp[(i-1)-j]
    dp[i] = sum_val

print(dp[n])