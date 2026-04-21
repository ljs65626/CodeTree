from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
start_point = []
q = deque()
visited = [[False for _ in range(m)] for _ in range(n)]
score = [[0 for _ in range(m)] for _ in range(n)]
group = [[0 for _ in range(m)] for _ in range(n)]
# Please write your code here.
def in_range(x, y):
    if x>=0 and x<n and y>=0 and y<m:
        return True
    else:
        return False

def push(x, y, v):
    q.append((x, y))
    visited[x][y] = True
    group[x][y] = v

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]==True:
        return False
    if grid[x][y]==1:
        return False
    return True

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x = x+dx
            new_y = y+dy
            if can_go(new_x, new_y):
                push(new_x, new_y, group[x][y])

def reset():
    for i in range(n):
        for j in range(m):
            visited[i][j]=False


def push2(x, y, v):
    q.append((x, y))
    visited[x][y] = True
    score[x][y] = v

def can_go2(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]==True:
        return False
    if grid[x][y]!=1:
        return False
    return True

def bfs2():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x = x+dx
            new_y = y+dy
            if can_go2(new_x, new_y):
                push2(new_x, new_y, score[x][y]+1)

partition=1
for i in range(n):
    for j in range(m):
        if not visited[i][j] and grid[i][j]==0:
            push(i, j, partition)
            bfs()
            partition+=1

reset()
for i in range(n):
    for j in range(m):
        if group[i][j]==1:
            push2(i, j, 0)
bfs2()

max_time=0
max_cnt=0
for i in range(n):
    for j in range(m):
        max_time = max(max_time, score[i][j])
for i in range(n):
    for j in range(m):
        if score[i][j]==max_time:
            max_cnt+=1
print(max_time, max_cnt)




