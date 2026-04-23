n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
# Please write your code here.

def initialize():
    dp[0][n-1] = grid[0][n-1]
    for i in range(1, n):
        dp[i][n-1] = dp[i-1][n-1] + grid[i][n-1]

    for i in range(n-2, -1, -1):
        dp[0][i] = dp[0][i+1] + grid[0][i]


initialize()
# for i in range(n):
#     for j in range(n):
#         print(dp[i][j], end=' ')
#     print()

for i in range(1, n):
    for j in range(n-2, -1, -1):
        dp[i][j] = min(dp[i][j+1]+grid[i][j], dp[i-1][j]+grid[i][j])


# for i in range(n):
#     for j in range(n):
#         print(dp[i][j], end=' ')
#     print()
print(dp[n-1][0])