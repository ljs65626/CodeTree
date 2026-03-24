import sys
n = int(input())
nums = list(map(int, input().split()))
arr=[]
ans = sys.maxsize
# Please write your code here.
def diff():
    sum_val1=0
    sum_val2=0
    for i in range(n):
        if arr[i]==1:
            sum_val1+=nums[i]
        else:
            sum_val2+=nums[i]
        
        return abs(sum_val1-sum_val2)

def backtrack(curr_loc, cnt):
    global ans
    if curr_loc==2*n+1:
        if cnt==n:
            ans = min(diff(), ans)
        return
    
    for i in range(1, -1, -1):
        if i==1:
            arr.append(i)
            backtrack(curr_loc+1, cnt+1)
            arr.pop()
        else:
            arr.append(i)
            backtrack(curr_loc+1, cnt)
            arr.pop()

backtrack(1, 0)
print(ans)
