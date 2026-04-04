from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
score = [[-1 for _ in range(m)] for _ in range(n)]
q = deque()
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
# Please write your code here.
def push(x, y, s):
    q.append((x, y))
    visited[x][y] = True
    score[x][y] = s

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
                push(new_x, new_y, score[x][y]+1)



push(0, 0, 0)
bfs()
print(score[n-1][m-1])