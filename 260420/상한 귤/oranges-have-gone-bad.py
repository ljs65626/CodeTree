from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
q = deque()
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
visited = [[False for _ in range(n)] for _ in range(n)]
score = [[0 for _ in range(n)] for _ in range(n)]
start = [(i, j) for i in range(n) for j in range(n) if grid[i][j]==2]
# Please write your code here.
def push(x, y, v):
    q.append((x, y))
    visited[x][y]=True
    score[x][y] = v

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

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x = x+dx
            new_y = y+dy
            if can_go(new_x, new_y):
                push(new_x, new_y, score[x][y]+1)


for x, y in start:
    push(x, y, 0)

bfs()

for i in range(n):
    for j in range(n):
        if grid[i][j]==1 and visited[i][j]==False:
            score[i][j]=-2
        elif grid[i][j]==0:
            score[i][j]=-1

for i in range(n):
    for j in range(n):
        print(score[i][j], end=' ')
    print()
