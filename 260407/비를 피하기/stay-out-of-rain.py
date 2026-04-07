from collections import deque
import sys
n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
q = deque()
ans = [[0 for _ in range(n)] for _ in range(n)]
score = [[0 for _ in range(n)] for _ in range(n)]
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def check():
    for i in range(n):
        for j in range(n):
            if grid[i][j]==2:
                if visited[i][j]==True:
                    ans[i][j] = score[i][j]
                else:
                    ans[i][j] = -1

def push(x, y, v):
    visited[x][y] = True
    q.append((x, y))
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
    if grid[x][y]==1:
        return False
    return True

# def reset():
#     for i in range(n):
#         for j in range(n):
#             visited[i][j] = False
#             score[i][j] = 0

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x = x+dx
            new_y = y+dy
            if can_go(new_x, new_y):
                push(new_x, new_y, score[x][y]+1)


for i in range(n):
    for j in range(n):
        if grid[i][j]==3:
            push(i, j, 0)
bfs()
check()
# ans[i][j] = check()


for i in range(n):
    for j in range(n):
        print(ans[i][j], end=' ')
    print()
