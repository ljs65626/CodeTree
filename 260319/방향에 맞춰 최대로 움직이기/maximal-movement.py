n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
ans=0
arr=[]
# Please write your code here.
dxs = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 0, 1, 1, 1, 0, -1, -1, -1]

def in_range(x, y):
    if x<n and x>=0 and y<n and y>=0:
        return True
    else:
        return False

def backtrack(curr_num, nx, ny):
    global ans
    ans = max(len(arr), ans)
    if curr_num==n*n:
        return

    n_dir = move_dir[nx][ny]
    curr_x = nx
    curr_y = ny
    for i in range(n-1):
        nx+=dxs[n_dir]
        ny+=dys[n_dir]
        if in_range(nx, ny) and num[nx][ny]>num[curr_x][curr_y]:
            arr.append(num[nx][ny])
            backtrack(curr_num+1, nx, ny)
            # print(arr)
            arr.pop()

backtrack(0, r-1, c-1)
print(ans)
