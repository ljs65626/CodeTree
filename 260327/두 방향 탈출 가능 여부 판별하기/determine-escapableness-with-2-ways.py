import sys
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dxs = [1, 0]
dys = [0, 1]
# Please write your code here.
def in_range(x, y):
    if x>=0 and x<n and y>=0 and y<m:
        return True
    else:
        return False

def Can_go(x, y):
    if not in_range(x, y):
        return False
    if grid[x][y]==0:
        return False
    if visited[x][y]==1:
        return False
    return True

def dfs(x, y):
    if x==n-1 and y==m-1:
        print(1)
        sys.exit()
    for dx, dy in zip(dxs, dys):
        new_x = x+dx
        new_y = y+dy

        if Can_go(new_x, new_y):
            visited[new_x][new_y]=1
            dfs(new_x, new_y)

visited[0][0]=1
dfs(0, 0)
print(0)