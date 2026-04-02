n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
ans=0

def backtrack(curr_loc, sum_val):
    global ans
    if curr_loc==n:
        ans = max(ans, sum_val)
        return
    
    for i in range(n):
        if visited[i]==True:
            continue
        
        sum_val+=grid[curr_loc][i]
        visited[i]=True
        backtrack(curr_loc+1, sum_val)
        visited[i]=False
        sum_val-=grid[curr_loc][i]

backtrack(0, 0)
print(ans)