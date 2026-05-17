from sortedcontainers import SortedSet
n, m = map(int, input().split())
queries = list(map(int, input().split()))
arr = list(range(1, m+1))

ss = SortedSet(arr)
# Please write your code here.

for i in queries:
    ss.remove(i)
    print(ss[-1])

