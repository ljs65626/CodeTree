N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
ans=0
for i in range(1, 10001):
    max_val, min_val = i+K, i
    cnt=0
    for j in arr:
        if j<min_val or j>max_val:
            continue
        else:
            cnt+=1
    ans = max(cnt, ans)

print(ans)