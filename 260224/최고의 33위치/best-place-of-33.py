import sys
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


ans = -sys.maxsize
for nx in range(n-3+1):
    for ny in range(n-3+1):
        sum_val=0
        for i in range(3):
            for j in range(3):
                sum_val += grid[nx+i][ny+j]
        ans = max(sum_val, ans)

print(ans)