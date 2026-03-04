import sys
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[0 for _ in range(m)] for _ in range(n)]


def reset():
    for i in range(n):
        for j in range(m):
            visited[i][j]=0

def overlapped(x1, y1, x2, y2, i, j, k, l):
    reset()
    for a in range(x1, x2+1):
        for b in range(y1, y2+1):
            visited[a][b]+=1
    
    for a in range(i, k+1):
        for b in range(j, l+1):
            visited[a][b]+=1
    
    for a in range(n):
        for b in range(m):
            if visited[a][b]>=2:
                return True
    return False

def rect_sum(x1, y1, x2, y2):
    sum_val=0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            sum_val+=grid[i][j]
    return sum_val

def another_rect(x1, y1, x2, y2):
    area = -sys.maxsize
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if not overlapped(x1, y1, x2, y2, i, j, k, l):
                        area = max(area, rect_sum(x1, y1, x2, y2)+rect_sum(i, j, k, l))
    return area

ans=-sys.maxsize
for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                ans = max(ans, another_rect(i, j, k, l))

print(ans)