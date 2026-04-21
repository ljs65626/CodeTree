from collections import deque
import sys
n, k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
start = []
for _ in range(k):
    x, y = tuple(map(int, input().split()))
    start.append((x-1, y-1))
visited = [[False for _ in range(n)] for _ in range(n)]
q=deque()
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
arr = []
one_point = 0
one_arr = []
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            one_point+=1
            one_arr.append((i, j))
ans = -sys.maxsize
# Please write your code here.
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

def push(x, y):
    q.append((x, y))
    visited[x][y] = True

def bfs():
    ret_val=0
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x = x+dx
            new_y = y+dy
            if can_go(new_x, new_y):
                push(new_x, new_y)

    for i in range(n):
        for j in range(n):
            if visited[i][j]==True:
                ret_val+=1
    return ret_val

def reset():
    for i in range(n):
        for j in range(n):
            visited[i][j]=False

def commit():
    for i in range(one_point):
        if arr[i]==1:
            x, y = one_arr[i]
            grid[x][y] = 0

def rollback():
    for i in range(one_point):
        if arr[i]==1:
            x, y = one_arr[i]
            grid[x][y] = 1

def backtracking(curr_loc, cnt):
    global ans
    if curr_loc==one_point:
        if cnt==m:
            reset()
            commit()
            for x, y in start:
                push(x, y)
            ans = max(bfs(), ans)
            rollback()
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

backtracking(0, 0)
print(ans)
