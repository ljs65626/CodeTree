n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# k: 블록이 떨어질 열(column) 위치
# Please write your code here.
k-=1
tmp_row=-1
for row in range(n-1, -1, -1):
    is_satisfied=True
    for col in range(k, k+m):
        if grid[row][col]==1:
            is_satisfied=False
            break
    if is_satisfied:
        tmp_row = row
        break

if is_satisfied:
    for col in range(k, k+m):
        grid[tmp_row][col] = 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()
