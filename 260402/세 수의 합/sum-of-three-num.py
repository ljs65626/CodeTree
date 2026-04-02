n, k = map(int, input().split())
arr = list(map(int, input().split()))
# Please write your code here.


d = {}
ans = 0

for i in range(n):
    total = k-arr[i]
    for j in range(i+1, n):
        diff = total - arr[j]
    
        if diff in d:
            ans += d[diff]
        
        if arr[j] in d:
            d[arr[j]] += 1
        else:
            d[arr[j]] = 1
    d = {}

print(ans)

# 3 3 3
