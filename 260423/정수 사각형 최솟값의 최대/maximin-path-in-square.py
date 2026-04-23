import sys
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
# Please write your code here.

def initialize():
    dp[0][0] = grid[0][0]
    for i in range(1, n):
        dp[i][0] = min(grid[i][0], dp[i-1][0])

    for i in range(1, n):
        dp[0][i] = min(grid[0][i], dp[0][i-1])


initialize()

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(max(dp[i][j-1], dp[i-1][j]), grid[i][j])

for i in range(n):
    for j in range(n):
        print(dp[i][j], end=' ')
    print()

print(dp[n-1][n-1])

