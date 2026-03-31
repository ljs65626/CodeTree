n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# k: 블록이 떨어질 열(column) 위치
# Please write your code here.
k-=1
max_row=-1
for row in range(n):
    is_satisfied=True
    for col in range(k, k+m):
        if grid[row][col]==1:
            is_satisfied=False
            break
    if is_satisfied:
        max_row = row
    else:
        break

if max_row!=-1:
    for col in range(k, k+m):
        grid[max_row][col] = 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()
