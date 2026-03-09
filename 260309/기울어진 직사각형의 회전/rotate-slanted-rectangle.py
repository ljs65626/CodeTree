import copy
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir1 = map(int, input().split())

# Please write your code here.

# def move(x, y, m1, m2, m3, m4, direction):
#     nx=x
#     ny=y
#     tmp = copy.deepcopy(grid)
#     if direction==0:
#         dx = [-1, -1, 1, 1]
#         dy = [1, -1, -1, 1]
#         dir2 = 0
#         for i in range(m1):
#             if nx+dx[dir2]<n and nx+dx[dir2]>=0 and ny+dy[dir2]<n and ny+dy[dir2]>=0:
#                 pass
#             else:
#                 dir2=(dir2+1)%4
#             nx+=dx[dir2]
#             ny+=dy[dir2]
#             tmp[nx][ny] = grid[nx-dx[dir2]][ny-dy[dir2]]
#         dir2=(dir2+1)%4

#         for i in range(m2):
#             if nx+dx[dir2]<n and nx+dx[dir2]>=0 and ny+dy[dir2]<n and ny+dy[dir2]>=0:
#                 pass
#             else:
#                 dir2=(dir2+1)%4
#             nx+=dx[dir2]
#             ny+=dy[dir2]
#             tmp[nx][ny] = grid[nx-dx[dir2]][ny-dy[dir2]]
#         dir2=(dir2+1)%4
        
#         for i in range(m3):
#             if nx+dx[dir2]<n and nx+dx[dir2]>=0 and ny+dy[dir2]<n and ny+dy[dir2]>=0:
#                 pass
#             else:
#                 dir2=(dir2+1)%4
#             nx+=dx[dir2]
#             ny+=dy[dir2]
#             tmp[nx][ny] = grid[nx-dx[dir2]][ny-dy[dir2]]
#         dir2=(dir2+1)%4
        
#         for i in range(m4):
#             if nx+dx[dir2]<n and nx+dx[dir2]>=0 and ny+dy[dir2]<n and ny+dy[dir2]>=0:
#                 pass
#             else:
#                 dir2=(dir2+1)%4
#             nx+=dx[dir2]
#             ny+=dy[dir2]
#             tmp[nx][ny] = grid[nx-dx[dir2]][ny-dy[dir2]]
        
        
#         tmp[x][y] = grid[nx-dx[dir2]][ny-dy[dir2]]
#     else:
#         dx = [-1, -1, 1, 1]
#         dy = [-1, 1, 1, -1]
#         dir2 = 0
#         origi = dir2
#         for i in range(m1):
#             if nx+dx[dir2]<n and nx+dx[dir2]>=0 and ny+dy[dir2]<n and ny+dy[dir2]>=0:
#                 pass
#             else:
#                 dir2=(dir2+1)%4
#             nx+=dx[dir2]
#             ny+=dy[dir2]
#             tmp[nx][ny] = grid[nx-dx[dir2]][ny-dy[dir2]]
#         dir2=(origi+1)%4
#         origi = dir2
#         for i in range(m2):
#             if nx+dx[dir2]<n and nx+dx[dir2]>=0 and ny+dy[dir2]<n and ny+dy[dir2]>=0:
#                 pass
#             else:
#                 dir2=(dir2+1)%4
#             nx+=dx[dir2]
#             ny+=dy[dir2]
#             tmp[nx][ny] = grid[nx-dx[dir2]][ny-dy[dir2]]
#         dir2=(origi+1)%4
#         origi = dir2
#         for i in range(m3):
#             if nx+dx[dir2]<n and nx+dx[dir2]>=0 and ny+dy[dir2]<n and ny+dy[dir2]>=0:
#                 pass
#             else:
#                 dir2=(dir2+1)%4
#             nx+=dx[dir2]
#             ny+=dy[dir2]
#             tmp[nx][ny] = grid[nx-dx[dir2]][ny-dy[dir2]]
#         dir2=(origi+1)%4
#         origi=dir2
#         for i in range(m4):
#             if nx+dx[dir2]<n and nx+dx[dir2]>=0 and ny+dy[dir2]<n and ny+dy[dir2]>=0:
#                 pass
#             else:
#                 dir2=(dir2+1)%4
#             nx+=dx[dir2]
#             ny+=dy[dir2]
#             tmp[nx][ny] = grid[nx-dx[dir2]][ny-dy[dir2]]
        
#         tmp[x][y] = grid[nx-dx[dir2]][ny-dy[dir2]]

#     return tmp

import copy

def move(x, y, m1, m2, m3, m4, direction):
    tmp = copy.deepcopy(grid)
    
    dx = [-1, -1, 1, 1]
    dy = [1, -1, -1, 1]
    move_counts = [m1, m2, m3, m4]
    
    coords = []
    nx, ny = x, y
    for d in range(4):
        for _ in range(move_counts[d]):
            nx += dx[d]
            ny += dy[d]
            coords.append((nx, ny))
            
    values = [grid[r][c] for r, c in coords]
    
    if direction == 0:
        values = [values[-1]] + values[:-1]
    else:
        values = values[1:] + [values[0]]
        
    for i, (r, c) in enumerate(coords):
        tmp[r][c] = values[i]
        
    return tmp

tmp = move(r-1, c-1, m1, m2, m3, m4, dir1)

for i in tmp:
    for j in i:
        print(j, end=' ')
    print()
        


