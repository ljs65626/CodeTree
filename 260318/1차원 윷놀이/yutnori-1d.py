n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
arr = []
ans=0
# Please write your code here.
curr_dist = [0] * k

def reset():
    for i in range(k):
        curr_dist[i] = 0


def point():
    reset()
    for i in range(n):
        curr_dist[arr[i]]+=nums[i]
    
    score=0
    for i in range(k):
        if curr_dist[i]>=m-1:
            score+=1
    
    return score


def backtrack(curr_num):
    global ans
    if n+1==curr_num:
        ans = max(point(), ans)
        return
    

    for i in range(k):
        arr.append(i)
        backtrack(curr_num+1)
        arr.pop()


backtrack(1)

print(ans)
