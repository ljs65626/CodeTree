N, L = map(int, input().split())
arr = list(map(int, input().split()))
tmp = L

# Please write your code here.
ans=0
for h in range(1, 101):
    L = tmp
    copy = [v for v in arr]
    for i in range(N):
        if arr[i]+1==h and L>0:
            L-=1
            copy[i] += 1
    for i in range(N):
        cnt=0
        condition_h = 0
        for j in range(N):
            if copy[i]<=copy[j]:
                cnt+=1
        if cnt>=copy[i]:
            condition_h=copy[i]
        ans = max(ans, condition_h)

print(ans)
