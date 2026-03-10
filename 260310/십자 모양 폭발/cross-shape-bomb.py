n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
tmp = [[0 for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    if x>=0 and x<n and y>=0 and y<n:
        return True
    else:
        return False

def bomb(x, y):
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]
    scale = grid[x][y]-1
    grid[x][y]=0
    for d in range(4):
        nx=x
        ny=y
        for i in range(scale):
            nx+=dxs[d]
            ny+=dys[d]
            if in_range(nx, ny):
                grid[nx][ny] = 0
    
    for j in range(n):
        arrow = n-1
        for i in range(n-1, -1, -1):
            if grid[i][j]!=0:
                tmp[arrow][j] = grid[i][j]
                arrow-=1

bomb(r-1, c-1)

for i in tmp:
    for j in i:
        print(j, end=' ')
    print()
