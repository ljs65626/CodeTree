n = int(input())
segments = [list(map(int, input().split())) for _ in range(n)]
xone, xtwo=zip(*segments)
xone = list(xone)
xtwo = list(xtwo)
# Please write your code here.
xone.sort()
xtwo.sort()
ans = min(xtwo[-1]-xone[1], xtwo[-2]-xone[0])
print(ans)
