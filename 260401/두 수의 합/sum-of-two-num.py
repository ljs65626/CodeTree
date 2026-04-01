n, k = map(int, input().split())
arr = list(map(int, input().split()))

d = {}
ans = 0

for num in arr:
    diff = k - num
    
    if diff in d:
        ans += d[diff]
    
    if num in d:
        d[num] += 1
    else:
        d[num] = 1

print(ans)