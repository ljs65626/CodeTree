K, N = map(int, input().split())
# Please write your code here.

arr=[]
def backtrack(curr_num):
    if N+1==curr_num:
        for i in arr:
            print(i, end=' ')
        print()
        return
    
    for i in range(1, K+1):
        if curr_num==1 or curr_num==2 or i!=arr[-1] or i!=arr[-2]:
            arr.append(i)
            backtrack(curr_num+1)
            arr.pop()
        else:
            continue
backtrack(1)