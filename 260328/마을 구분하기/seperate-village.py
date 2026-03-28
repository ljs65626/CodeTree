n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
ans=0
cnt=0
answer=[]
# Please write your code here.
def in_range(x, y):
    if x>=0 and x<n and y>=0 and y<n:
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
    global cnt
    for dx, dy in zip(dxs, dys):
        new_x = x+dx
        new_y = y+dy
        if can_go(new_x, new_y):
            cnt+=1
            visited[new_x][new_y]=True
            dfs(new_x, new_y)

for i in range(n):
    for j in range(n):
        if grid[i][j]==1 and visited[i][j]==False:
            visited[i][j]=True
            cnt=1
            dfs(i, j)
            ans+=1
            answer.append(cnt)

print(ans)
answer.sort()
for i in answer:
    print(i)