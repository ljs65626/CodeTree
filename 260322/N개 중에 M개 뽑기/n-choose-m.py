N, M = map(int, input().split())
arr=[]
nums = [i for i in range(1, N+1)]
# Please write your code here.
def print_answer():
    for i in range(N):
        if arr[i]==1:
            print(nums[i], end=' ')
    print()


def backtrack(curr_num, cnt):
    if curr_num==N+1:
        if cnt==M:
            print_answer()
        return
    
    for i in range(1, -1, -1):
        arr.append(i)
        if i==1:
            backtrack(curr_num+1, cnt+1)
        else:
            backtrack(curr_num+1, cnt)
        arr.pop()


backtrack(1, 0)

