n, r, c = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
# Please write your code here.
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
r-=1
c-=1

def in_range(x, y):
    if x>=0 and x<n and y>=0 and y<n:
        return True
    else:
        return False

def simulate(x, y):
    is_moved = False
    for dx, dy in zip(dxs, dys):
        new_x = x+dx
        new_y = y+dy
        if in_range(new_x, new_y) and grid[new_x][new_y] > grid[x][y]:
            is_moved = True
            break
    if is_moved:
        return new_x, new_y
    else:
        return x, y

while True:
    print(grid[r][c], end=' ')
    new_r, new_c = simulate(r, c)
    if new_r==r and new_c==c:
        break
    r, c = new_r, new_c