# Please write your code here.

from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    if x>=0 and x<n and y>=0 and y<m:
        return True
    else:
        return False

def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    melt_list = []

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x = x + dx
            new_y = y + dy
            
            if in_range(new_x, new_y) and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                
                if grid[new_x][new_y] == 0:
                    q.append((new_x, new_y))
                elif grid[new_x][new_y] == 1:
                    melt_list.append((new_x, new_y))

    for x, y in melt_list:
        grid[x][y] = 0

    return len(melt_list)

time = 0
last_cheese_cnt = 0

while True:
    melted_cnt = bfs()
    
    if melted_cnt == 0:
        break
        
    last_cheese_cnt = melted_cnt 
    time += 1

print(time, last_cheese_cnt)