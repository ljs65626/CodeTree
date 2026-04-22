from collections import deque
n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
stone_pos = [(i, j) for i in range(n) for j in range(n)]
ans=0
q=deque()
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
arr=[]
visited=[[False for _ in range(n)] for _ in range(n)]
# Please write your code here.

def in_range(x, y):
    if x>=0 and x<n and y>=0 and y<n:
        return True
    else:
        return False

def can_go(new_x, new_y, x, y):
    if not in_range(new_x, new_y):
        return False
    if visited[new_x][new_y]==True:
        return False
    if abs(grid[new_x][new_y]-grid[x][y])<u or abs(grid[new_x][new_y]-grid[x][y])>d:
        return False
    return True


def push(x, y):
    q.append((x, y))
    visited[x][y]=True
    

def bfs():
    ret_val=0
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x = x+dx
            new_y = y+dy
            if can_go(new_x, new_y, x, y):
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

def backtracking(curr_loc, cnt):
    global ans
    if curr_loc==n**2:
        if cnt==k:
            reset()
            for x, y in arr:
                push(x, y)
            ans = max(bfs(), ans)
        return
    
    arr.append(stone_pos[curr_loc])
    backtracking(curr_loc+1, cnt+1)
    arr.pop()

    backtracking(curr_loc+1, cnt)

backtracking(0, 0)
print(ans)
