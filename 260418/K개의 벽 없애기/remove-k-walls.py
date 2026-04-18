import sys
from collections import deque
sys.setrecursionlimit(10000)
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]
score = [[0 for _ in range(n)] for _ in range(n)]
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
one_count = []
oc=0
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            one_count.append((i, j))
            oc+=1


arr=[]
min_score = sys.maxsize
def backtracking(curr_loc, cnt):
    global min_score
    if curr_loc==oc:
        if cnt==k:
            reset()
            zero()
            push(r1-1, c1-1, 0)
            bfs()
            if visited[r2-1][c2-1]==True:
                min_score = min(min_score, score[r2-1][c2-1])
            recovery()
        return
    
    for i in range(1, -1, -1):
        if i==1:
            arr.append(i)
            backtracking(curr_loc+1, cnt+1)
            arr.pop()
        else:
            arr.append(i)
            backtracking(curr_loc+1, cnt)
            arr.pop()

def zero():
    for i in range(oc):
        if arr[i]==1:
            x, y=one_count[i]
            grid[x][y] = 0

def recovery():
    for i in range(oc):
        if arr[i]==1:
            x, y = one_count[i]
            grid[x][y] = 1

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x = x+dx
            new_y = y+dy
            if can_go(new_x, new_y):
                push(new_x, new_y, score[x][y]+1)

def push(x, y, v):
    visited[x][y]=True
    q.append((x, y))
    score[x][y] = v

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]==True:
        return False
    if grid[x][y]==1:
        return False
    return True

def in_range(x, y):
    if x>=0 and x<n and y>=0 and y<n:
        return True
    else:
        return False

def reset():
    for i in range(n):
        for j in range(n):
            visited[i][j]=False
            score[i][j] = 0


backtracking(0, 0)

if min_score==sys.maxsize:
    print(-1)
else:
    print(min_score)