n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
arr = []
ans=0
# Please write your code here.
curr_dist = [0] * k

# def reset():
#     for i in range(k):
#         curr_dist[i] = 0


def point():
    
    score=0
    for i in range(k):
        if curr_dist[i]>=m-1:
            score+=1
    
    return score


def backtrack(curr_num):
    global ans
    if n==curr_num:
        ans = max(point(), ans)
        return
    

    for i in range(k):
        if curr_dist[i]>=m-1:
            continue
        curr_dist[i]+=nums[curr_num]
        backtrack(curr_num+1)
        curr_dist[i]-=nums[curr_num]


backtrack(0)

print(ans)
