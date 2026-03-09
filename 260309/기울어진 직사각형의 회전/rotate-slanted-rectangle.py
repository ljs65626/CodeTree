import copy
n=int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())

def move(x, y, m1, m2, m3, m4, direction):
    coords=[]
    dx = [-1, -1, 1, 1]
    dy = [1, -1, -1, 1]
    mm = [m1, m2, m3, m4]
    dir2=0
    for d in range(4):
        for i in range(mm[d]):
            x+=dx[dir2]
            y+=dy[dir2]
            coords.append((x, y))
        dir2 = (dir2+1)%4
    
    values = [grid[x1][y1] for x1, y1 in coords]

    if direction==0:
        values = [values[-1]] + values[:-1]
    else:
        values = values[1:] + [values[0]]
    
    for i, (x1, y1) in enumerate(coords):
        grid[x1][y1] = values[i]


move(r-1, c-1, m1, m2, m3, m4, dir)

for i in grid:
    for j in i:
        print(j, end=' ')
    print()