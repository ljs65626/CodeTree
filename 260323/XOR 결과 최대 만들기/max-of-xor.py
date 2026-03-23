import sys
n, m = map(int, input().split())
nums = list(map(int, input().split()))
ans=-sys.maxsize
arr=[]
# Please write your code here.

def func():
    ans2=0
    for i in arr:
        ans2 = ans2^i
    return ans2


def backtrack(curr_num, cnt):
    global ans
    if curr_num==n:
        if cnt==m:
            ans = max(func(), ans)
        return
    
    for i in range(1, -1, -1):
        if i==1:
            arr.append(nums[curr_num])
            backtrack(curr_num+1, cnt+1)
            arr.pop()
        else:
            backtrack(curr_num+1, cnt)

backtrack(0, 0)
print(ans)
