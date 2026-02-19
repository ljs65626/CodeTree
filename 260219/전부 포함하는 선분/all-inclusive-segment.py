import sys
n = int(input())
segments = [list(map(int, input().split())) for _ in range(n)]
# xone, xtwo=zip(*segments)
# xone = list(xone)
# xtwo = list(xtwo)
# Please write your code here.
xone = sorted(segments, key=lambda t: t[0])
xtwo = sorted(segments, key=lambda t: t[1])
if xone[0]==xtwo[n-1]:
    print(xtwo[n-2][1]-xone[1][0])
    sys.exit()
ans = min(xtwo[n-1][1]-xone[1][0], xtwo[n-2][1]-xone[0][0])
print(ans)

