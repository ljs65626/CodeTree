import copy
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
bombed = [[False for _ in range(n)] for _ in range(n)]
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

def reset():
    for i in range(n):
        for j in range(n):
            bombed[i][j]=False       

def howmany():
    reset()
    arrow=0
    ccnt=0
    bomb_shapes = [
        [],
        [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]],
        [[-1, 0], [1, 0], [0, 0], [0, -1], [0, 1]],
        [[-1, -1], [-1, 1], [0, 0], [1, -1], [1, 1]]
    ]
    for i in range(n):
        for j in range(n):
            if grid[i][j]==1:
                for k in range(5):
                    dx, dy = bomb_shapes[arr[arrow]][k]
                    nx, ny = i+dx, j+dy
                    if in_range(nx, ny):
                        bombed[nx][ny]=True
                arrow+=1
    
    for i in range(n):
        for j in range(n):
            if bombed[i][j]==True:
                ccnt+=1
                
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
