from collections import deque
import sys
n = int(input())
r1, c1, r2, c2 = map(int, input().split())
if r1==r2 and c1==c2:
    print(0)
    sys.exit()
visited = [[False for _ in range(n)] for _ in range(n)]
score = [[0 for _ in range(n)] for _ in range(n)]
q = deque()
dxs = [-1, -2, -2, -1, 1, 2, 2, 1]
dys = [-2, -1, 1, 2, 2, 1, -1, -2]
# Please write your code here.
def push(x, y, v):
    q.append((x, y))
    visited[x][y] = True
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
    return True

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x = x+dx
            new_y = y+dy
            if can_go(new_x, new_y):
                push(new_x, new_y, score[x][y]+1)


push(r1-1, c1-1, 0)
bfs()

if score[r2-1][c2-1]:
    print(score[r2-1][c2-1])
else:
    print(-1)
