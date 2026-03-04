n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def is_possible(x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if grid[i][j]<=0:
                return False
    return True

def get_rect_sum(x1, y1, x2, y2):
    sum_val=0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            sum_val+=grid[i][j]
    return sum_val

ans=-1
for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                if is_possible(i, j, k, l):
                    area = ((abs(k-i)+1)*(abs(l-j)+1))
                    ans = max(area, ans)

print(ans)
                    