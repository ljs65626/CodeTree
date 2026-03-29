import sys
sys.setrecursionlimit(10000)
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
visited = [[False for _ in range(n)] for _ in range(n)]
cnt=0
# Please write your code here.
def in_range(x, y):
    if x>=0 and x<n and y>=0 and y<n:
        return True
    else:
        return False

def can_go(x, y, value):
    if not in_range(x, y):
        return False
    if visited[x][y]==True:
        return False
    if grid[x][y]!=value:
        return False
    return True

def dfs(x, y, value):
    global cnt
    for dx, dy in zip(dxs, dys):
        new_x = x+dx
        new_y = y+dy
        if can_go(new_x, new_y, value):
            cnt+=1
            visited[new_x][new_y]=True
            dfs(new_x, new_y, value)

ans=0
ans_cnt=0
for i in range(n):
    for j in range(n):
        
        if visited[i][j]==False:
            cnt=1
            visited[i][j]=True
            dfs(i, j, grid[i][j])
            if cnt>=4:
                ans+=1
                ans_cnt = max(cnt, ans_cnt)
            else:
                ans_cnt = max(cnt, ans_cnt)

print(ans, ans_cnt)
