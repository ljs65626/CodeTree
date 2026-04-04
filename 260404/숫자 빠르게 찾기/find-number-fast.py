n, m = map(int, input().split())
arr = list(map(int, input().split()))
d={}
# Please write your code here.
for i in range(n):
    d[arr[i]] = i+1

for _ in range(m):
    q = int(input())
    if q in d:
        print(d[q])
    else:
        print(-1)