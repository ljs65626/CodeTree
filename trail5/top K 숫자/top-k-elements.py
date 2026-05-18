from sortedcontainers import SortedSet
n, k = map(int, input().split())
arr = list(map(int, input().split()))
ss = SortedSet(arr)
# Please write your code here.
i = len(ss)-1
for _ in range(k):
    print(ss[i], end=' ')
    i-=1
