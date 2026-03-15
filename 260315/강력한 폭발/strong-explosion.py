import copy
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
cnt=0
ans = 0
arr=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            cnt+=1
# Please write your code here.

def in_range(x, y):
    if x>=0 and x<n and y>=0 and y<n:
        return True
    else:
        return False

def howmany():
    arrow=0
    ccnt=0
    temp = copy.deepcopy(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j]==1:
                if arr[arrow]==1:
                    nx = i
                    ny = j
                    for k in range(2):
                        nx-=1
                        if in_range(nx, ny) and temp[nx][ny]==0:
                            ccnt+=1
                            temp[nx][ny] = 1
                    nx = i
                    ny = j
                    for k in range(2):
                        nx+=1
                        if in_range(nx, ny) and temp[nx][ny]==0:
                            ccnt+=1
                            temp[nx][ny] = 1
                    ccnt+=1
                    arrow+=1
                elif arr[arrow]==2:
                    dxs = [-1, 0, 1, 0]
                    dys = [0, 1, 0, -1]
                    n_dir = 0
                    for k in range(4):
                        if in_range(i+dxs[n_dir], j+dys[n_dir]) and temp[i+dxs[n_dir]][j+dys[n_dir]]==0:
                            ccnt+=1
                            temp[i+dxs[n_dir]][j+dys[n_dir]]=1
                        n_dir+=1
                    ccnt+=1
                    arrow+=1
                else:
                    dxs = [-1, -1, 1, 1]
                    dys = [-1, 1, 1, -1]
                    n_dir=0
                    for k in range(4):
                        if in_range(i+dxs[n_dir], j+dys[n_dir]) and temp[i+dxs[n_dir]][j+dys[n_dir]]==0:
                            ccnt+=1
                            temp[i+dxs[n_dir]][j+dys[n_dir]]=1
                        n_dir+=1
                    ccnt+=1
                    arrow+=1
    return ccnt


def backtrack(curr_num):
    global ans
    if curr_num==cnt+1:
        tmp = howmany()
        ans = max(tmp, ans)
        return
    
    for i in range(1, 4):
        arr.append(i)
        backtrack(curr_num+1)
        arr.pop()



backtrack(1)

print(ans)
