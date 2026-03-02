n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


def maremmo(k, i, j):
    gold=0
    for a in range(n):
        for b in range(n):
            # if nx+a<0 or ny+b<0 or nx+a>=n or ny+b>=n:
            #     continue
            if (abs(i-a)+abs(j-b)) <= k:
                gold+=grid[a][b]
    
    return gold


ans=0
for k in range(n+1):
    mining = (k**2) + ((k+1)**2)
    for i in range(n):
        for j in range(n):
            gold_cnt = maremmo(k, i, j)
            price = gold_cnt*m
            if price>=mining:
                ans = max(ans, gold_cnt)


print(ans)