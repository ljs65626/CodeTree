import sys
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
arr = [0]
ans = sys.maxsize
visited=[False]*n
# Please write your code here.

def backtrack(curr_node, sum_val, cnt):
    global ans
    if sum_val>=ans:
        return

    if cnt==n:
        if grid[curr_node][0]!=0:
            sum_val+=grid[curr_node][0]
            ans = min(sum_val, ans)
        return
    
    for next_node in range(1, n):
        if visited[next_node]==True or grid[curr_node][next_node]==0:
            continue
        visited[next_node]=True
        backtrack(next_node, sum_val+grid[curr_node][next_node], cnt+1)
        visited[next_node]=False

backtrack(0, 0, 1)
print(ans)