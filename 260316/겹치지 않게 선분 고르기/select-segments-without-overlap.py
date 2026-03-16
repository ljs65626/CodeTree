n = int(input())
lines = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]
whether = [0] * 1001
global ans
ans=0
arr = []
# Please write your code here.
def reset():
    for i in range(1001):
        whether[i] = 0


def is_satisfied():
    reset()
    for i in arr:
        a, b = lines[i]
        for j in range(a, b+1):
            whether[j]+=1
    
    for i in whether:
        if i>1:
            return False
    return True


def backtrack(curr_num):
    global ans
    if n+1==curr_num:
        return
    
    for i in range(1, n+1):
        arr.append(i)
        backtrack(curr_num+1)
        if is_satisfied()==True:
            ans = max(ans, len(arr))
        arr.pop()


backtrack(1)
print(ans)