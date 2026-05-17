from sortedcontainers import SortedSet


ss = SortedSet()
n, m = map(int, input().split())
arr = list(map(int, input().split()))
# Please write your code here.
for i in arr:
    ss.add(i)

for _ in range(m):
    inp = int(input())
    i = ss.bisect_left(inp)
    if i==len(arr):
        print(-1)
    else:
        print(ss[i])