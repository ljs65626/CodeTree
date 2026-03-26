n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
ans=-1
visited=[False]*n
# Please write your code here.

def backtrack(curr_loc, minnest):
    global ans
    if minnest<ans:
        return

    if curr_loc==n:
        ans = max(minnest, ans)
        return

    for i in range(n):
        if visited[i]==True:
            continue
        
        
        visited[i]=True
        backtrack(curr_loc+1, min(grid[curr_loc][i], minnest))
        visited[i]=False
    

backtrack(0, 10001)
print(ans)