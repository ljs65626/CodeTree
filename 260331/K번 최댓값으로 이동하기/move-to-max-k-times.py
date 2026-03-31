from collections import deque
import sys
n, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = tuple(map(int, input().split()))
r-=1
c-=1
visited = [[False for _ in range(n)] for _ in range(n)]
q = deque()
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
# Please write your code here.
def push(x, y):
    visited[x][y] = True
    q.append((x, y))

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
    if grid[x][y]>=grid[r][c]:
        return False
    return True

def maxval(new_x, new_y, max_x, max_y, max_v):
    if grid[new_x][new_y] > max_v:
        max_x = new_x
        max_y = new_y
        max_v = grid[new_x][new_y]
    elif grid[new_x][new_y] == max_v:
        if new_x < max_x:
                max_x = new_x
                max_y = new_y
                max_v = grid[new_x][new_y]
        elif new_x == max_x:
            if new_y < max_y:
                max_x = new_x
                max_y = new_y
                max_v = grid[new_x][new_y]
    return max_x, max_y, max_x, max_y, max_v

def reset():
    for i in range(n):
        for j in range(n):
            visited[i][j]=False

def bfs(r, c):
    max_x = sys.maxsize
    max_y = sys.maxsize
    max_v = -sys.maxsize
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x = x+dx
            new_y = y+dy
            if can_go(new_x, new_y):
                push(new_x, new_y)
                r, c, max_x, max_y, max_v = maxval(new_x, new_y, max_x, max_y, max_v)
    return r, c


for _ in range(k):
    push(r, c)
    reset()
    r, c = bfs(r, c)

print(r+1, c+1)
