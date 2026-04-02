n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)] 
arr=[]
visited=[False]*(n+1)
ans = 0
# Please write your code here.
def func():
    sum_val=0
    for i in range(n):
        sum_val += nums[i][arr[i]-1]
        i+=1
    return sum_val


def backtrack(curr_loc):
    global ans
    if curr_loc==n+1:
        ans = max(ans, func())
        return
    

    for i in range(1, n+1):
        if visited[i]==True:
            continue
        
        visited[i]=True
        arr.append(i)
        backtrack(curr_loc+1)
        arr.pop()
        visited[i]=False

backtrack(1)
print(ans)
