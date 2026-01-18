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
    cnt=0
    condition_h = 0
    for j in range(N):
        if h<=copy[j]:
            cnt+=1
    if cnt>=h:
        ans = max(ans, h)
    # print(ans, end=' ')

print(ans)
