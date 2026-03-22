N, M = map(int, input().split())
arr=[]
# Please write your code here.
def print_answer():
    for i in arr:
        print(i, end=' ')
    print()


def backtrack(curr_num, cnt):
    if curr_num==M+1:
        print_answer()
        return
    
    for i in range(cnt, N+1):
        arr.append(i)
        backtrack(curr_num+1, i+1)
        arr.pop()


backtrack(1, 1)

