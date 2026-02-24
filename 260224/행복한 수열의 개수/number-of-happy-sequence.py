import sys
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# Please write your code here.
ans=0

if m==1 and n==1:
    print(2)
    sys.exit()

for nx in range(n):
    before = grid[nx][0]
    continuous=1
    for ny in range(1, n):
        if grid[nx][ny]==before:
            continuous+=1
        before = grid[nx][ny]
    
        if continuous>=m:
            ans+=1
            break


for ny in range(n):
    before = grid[0][ny]
    continuous=1
    for nx in range(1, n):
        if grid[nx][ny]==before:
            continuous+=1
        before = grid[nx][ny]

        if continuous>=m:
            ans+=1
            break
    
print(ans)
