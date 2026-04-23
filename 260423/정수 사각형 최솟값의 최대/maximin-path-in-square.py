n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
# Please write your code here.

def initialize():
    dp[0][0] = grid[0][0]
    for i in range(1, n):
        dp[i][0] = grid[i][0]

    for i in range(1, n):
        dp[0][i] = grid[0][i]


initialize()

min_val = grid[0][0]
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(max(dp[i][j-1], dp[i-1][j]), grid[i][j])




print(dp[n-1][n-1])