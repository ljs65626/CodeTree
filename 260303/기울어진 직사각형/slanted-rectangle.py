n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs = [-1, -1, 1, 1]
dys = [1, -1, -1, 1]


def in_range(x, y):
    if (x<n and x>=0) and (y<n and y>=0):
        return True
    else:
        return False

def sum_of_num(i, j, w, h):
    nx=i
    ny=j
    sum_val=0
    moves = [w, h, w, h]
    # for k in range(w):
    #     if not in_range(nx+dxs[0], ny+dys[0]):
    #         return 0
    #     else:
    #         sum_val+=grid[nx+dxs[0]][ny+dys[0]]
    #         nx+=dxs[0]
    #         ny+=dys[0]
    
    # for k in range(h):
    #     if not in_range(nx+dxs[1], ny+dys[1]):
    #         return 0
    #     else:
    #         sum_val+=grid[nx+dxs[1]][ny+dys[1]]
    #         nx+=dxs[1]
    #         ny+=dys[1]

    # for k in range(w):
    #     if not in_range(nx+dxs[2], ny+dys[2]):
    #         return 0
    #     else:
    #         sum_val+=grid[nx+dxs[2]][ny+dys[2]]
    #         nx+=dxs[2]
    #         ny+=dys[2]
    
    # for k in range(h):
    #     if not in_range(nx+dxs[3], ny+dys[3]):
    #         return 0
    #     else:
    #         sum_val+=grid[nx+dxs[3]][ny+dys[3]]
    #         nx+=dxs[3]
    #         ny+=dys[3]
    
    # return sum_val

    for dx, dy, move in zip(dxs, dys, moves):
        for _ in range(move):
            nx+=dx
            ny+=dy
            if not in_range(nx, ny):
                return 0
            sum_val+=grid[nx][ny]
    return sum_val

ans=0
for i in range(n):
    for j in range(n):
        for w in range(1, n):
            for h in range(1, n):
                sum_val = sum_of_num(i, j, w, h)
                ans = max(ans, sum_val)

print(ans)
