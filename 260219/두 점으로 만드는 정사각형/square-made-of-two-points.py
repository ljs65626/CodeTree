x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.

maxx = max(x1, x2, a1, a2)
minx = min(x1, x2, a1, a2)

maxy = max(y1, y2, b1, b2)
miny = min(y1, y2, b1, b2)

maxx-minx

maxval = max(maxx-minx, maxy-miny)
print(maxval**2)