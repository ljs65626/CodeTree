import sys
n = int(input())
nums = list(map(int, input().split()))
arr=[]
arr.append(nums[0])
is_in = False
ans = sys.maxsize
# Please write your code here.




def backtrack(curr_loc):
    global is_in
    global ans
    if curr_loc==n-1:
        is_in = True
        ans = min(len(arr)-1, ans)
        return

    for i in range(1, arr[-1]+1):
        if curr_loc+i >= n:
            break
        arr.append(nums[curr_loc+i])
        backtrack(curr_loc+i)
        arr.pop()


backtrack(0)

if is_in:
    print(ans)
else:
    print(-1)