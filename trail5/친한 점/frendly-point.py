from sortedcontainers import SortedSet
n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
queries = [tuple(map(int, input().split())) for _ in range(m)]
ss = SortedSet(points)

for x, y in queries:
    i = ss.bisect_left((x, y))
    if i==len(ss):
        print(-1, -1)
    else:
        x, y = ss[i]
        print(x, y)