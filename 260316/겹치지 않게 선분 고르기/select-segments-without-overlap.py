n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
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
    for i in range(n):
        if arr[i]==1:
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
        cnt=0
        if is_satisfied()==True:
            for j in arr:
                if j==1:
                    cnt+=1
            ans = max(ans, cnt)
        return
    
    for i in range(2):
        arr.append(i)
        backtrack(curr_num+1)
        arr.pop()


backtrack(1)
print(ans)