n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
# Please write your code here.
d={}

for x, y in points:
    if x in d:
        d[x] = min(y, d[x])
    else:
        d[x] = y
ans=0
for k, v in d.items():
    ans+=v

print(ans)