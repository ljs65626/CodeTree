from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
start = [tuple(map(int, input().split())) for _ in range(k)]
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
visited = [[False for _ in range(n)] for _ in range(n)]
q = deque()
# Please write your code here.
def push(x, y):
    q.append((x, y))
    visited[x][y]=True

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

def bfs():
    cnt=1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if can_go(new_x, new_y):
                cnt+=1
                push(new_x, new_y)
    return cnt

ans=0
for r, c in start:
    if visited[r-1][c-1]==False:
        push(r-1, c-1)
        ans += bfs()

print(ans)
