import sys
n, m = map(int, input().split())
coord = list(tuple(map(int, input().split())) for _ in range(n))
arr=[]
ans = sys.maxsize
# Please write your code here.
def dist(x1, y1, x2, y2):
    return pow(((x1-x2)**2) + ((y1-y2)**2), 1/2)

def func():
    max_dist = -sys.maxsize
    for i in range(m):
        x1, y1 = arr[i]
        for j in range(i+1, m):
            x2, y2 = arr[j]
            max_dist = max(dist(x1, y1, x2, y2), max_dist)
    return max_dist


def backtrack(curr_loc, cnt):
    global ans
    if curr_loc==n:
        if cnt==m:
            ans = min(ans, func())
        return
    
    for i in range(1, -1, -1):
        if i==1:
            arr.append(coord[curr_loc])
            backtrack(curr_loc+1, cnt+1)
            arr.pop()
        else:
            backtrack(curr_loc+1, cnt)


backtrack(0, 0)
print(int((ans**2)+0.5))