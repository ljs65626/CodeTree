import sys
sys.setrecursionlimit(10**5)

n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
# Please write your code here.
def swim(k):
    for i in range(n):
        for j in range(m):
            if grid[i][j]<=k:
                grid[i][j]=0

def in_range(x, y):
    if x>=0 and x<n and y>=0 and y<m:
        return True
    else:
        return False

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]==True:
        return False
    if grid[x][y]==0:
        return False
    return True

def dfs(x, y):
    for dx, dy in zip(dxs, dys):
        new_x = x+dx
        new_y = y+dy
        if can_go(new_x, new_y):
            visited[new_x][new_y]=True
            dfs(new_x, new_y)

def reset():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False


max_val = max(max(grid))
ans_k=1
ans_cnt=0
for k in range(1, max_val+1):
    swim(k)
    reset()
    # print(visited)
    safe_cnt=0
    for i in range(n):
        for j in range(m):
            if grid[i][j]>0 and visited[i][j]==False:
                visited[i][j]=True
                dfs(i, j)
                safe_cnt+=1
    if safe_cnt>ans_cnt:
        ans_k=k
        ans_cnt = safe_cnt

print(ans_k, ans_cnt)