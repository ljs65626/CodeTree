import sys
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
# x1 = [seg[0] for seg in segments]
# x2 = [seg[1] for seg in segments]

# Please write your code here.
maxx = -sys.maxsize
miny = sys.maxsize
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        x, y = segments[j]
        maxx = max(maxx, x)
        miny = min(miny, y)
    
        if maxx<=miny:
            print('Yes')
            sys.exit()


print('No')