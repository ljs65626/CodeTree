import sys
# n, m = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(n)]

# # Please write your code here.

# def func1(nx, ny, mode):
#     sum_val=0
#     if mode==0:
#         for i in range(2):
#             for j in range(2):
#                 if i==0 and j==1:
#                     continue
#                 sum_val += grid[nx+i][ny+j]
#     elif mode==1:
#         for i in range(2):
#             for j in range(2):
#                 if i==0 and j==0:
#                     continue
#                 sum_val += grid[nx+i][ny+j]
#     elif mode==2:
#         for i in range(2):
#             for j in range(2):
#                 if i==1 and j==0:
#                     continue
#                 sum_val += grid[nx+i][ny+j]
#     else:
#         for i in range(2):
#             for j in range(2):
#                 if i==1 and j==1:
#                     continue
#                 sum_val += grid[nx+i][ny+j]
    
#     return sum_val


# def func2(nx, ny, mode):
#     sum_val=0
#     if mode==0:
#         for j in range(3):
#             sum_val+=grid[nx][ny+j]
#     else:
#         for i in range(3):
#             sum_val+=grid[nx+i][ny]
    
#     return sum_val


# ans = -sys.maxsize
# for mode in range(4):
#     for nx in range(n):
#         for ny in range(m):
#             if nx+1>=n or ny+1>=m:
#                 continue
#             sum_val = func1(nx, ny, mode)
#             ans = max(sum_val, ans)

# for mode in range(2):
#     for nx in range(n):
#         for ny in range(m):
#             if (mode==0 and ny+2>=m) or (mode==1 and nx+2>=n):
#                 continue
#             sum_val = func2(nx, ny, mode)
#             ans = max(sum_val, ans)

# print(ans)




n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

shapes = [
    [[1, 1, 0],
    [1, 0, 0],
    [0, 0, 0]],

    [[1, 1, 0],
    [0, 1, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[0, 1, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]],
]

def get_max_sum(x, y):
    max_sum=0
    for i in range(6):
        is_possible=True
        sum_val=0
        for dx in range(3):
            for dy in range(3):
                if shapes[i][dx][dy]==0:
                    continue
                if x+dx>=n or y+dy>=m:
                    is_possible=False
                else:
                    sum_val += grid[x+dx][y+dy]
        if is_possible:
            max_sum = max(max_sum, sum_val)
    return max_sum
ans=0
for nx in range(n):
    for ny in range(m):
        ans = max(get_max_sum(nx, ny), ans)

print(ans)