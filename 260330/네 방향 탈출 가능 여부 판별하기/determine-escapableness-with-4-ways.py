from collections import deque
import sys
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
visited = [[False for _ in range(m)] for _ in range(n)]
q = deque()
# Please write your code here.
def push(x, y):
    if x==n-1 and y==m-1:
        print(1)
        sys.exit()
    q.append((x, y))
    visited[x][y]=True

def in_range(x, y):
    if x>=0 and x<n and y>=0 and y<m:
        return True
    else:
        return False

def can_go(x, y):
    if not in_range(x, y):
        return False
    if grid[x][y]==0:
        return False
    if visited[x][y]==True:
        return False
    return True

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x = x+dx
            new_y = y+dy
            if can_go(new_x, new_y):
                push(new_x, new_y)

push(0, 0)
bfs()
print(0)
