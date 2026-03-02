n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


def maremmo(k, i, j, square):
    nx = i-k  #leftupi
    ny = j-k  #leftupj
    gold=0
    for a in range(square):
        for b in range(square):
            if nx+a<0 or ny+b<0 or nx+a>=n or ny+b>=n:
                continue
            if (abs(i-(nx+a))+abs(j-(ny+b))) <= k:
                gold+=grid[nx+a][ny+b]
    
    return gold


square=1
ans=0
for k in range(n+1):
    mining = (k**2) + ((k+1)**2)
    print(mining)
    for i in range(n):
        for j in range(n):
            gold_cnt = maremmo(k, i, j, square)
            price = gold_cnt*m
            if price>=mining:
                ans = max(ans, gold_cnt)
    square+=2


print(ans)