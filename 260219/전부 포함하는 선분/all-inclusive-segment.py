import sys
n = int(input())
segments = [list(map(int, input().split())) for _ in range(n)]
x1, x2=zip(*segments)
x1 = list(x1)
x2 = list(x2)
# Please write your code here.
# xone = sorted(segments, key=lambda t: t[0])
# xtwo = sorted(segments, key=lambda t: t[1])
# if xone[0]==xtwo[n-1]:
#     print(xtwo[n-2][1]-xone[1][0])
#     sys.exit()
# ans = min(xtwo[n-1][1]-xone[1][0], xtwo[n-2][1]-xone[0][0])
# print(ans)



# ans = sys.maxsize
# for i in range(n):
#     line = [0]*101
#     for j in range(n):
#         if i==j:
#             continue
#         x1, x2 = segments[j]
#         for k in range(x1, x2+1):
#             line[k]=1
#     first_index=-1
#     for j in range(1, 101):
#         if first_index==-1 and line[j]==1:
#             first_index=j
#         elif line[j]==1:
#             last_index=j
    
#     ans = min(last_index-first_index, ans)

# print(ans)

skip=0
for i in range(n):
    if x1[skip]>x1[i]:
        skip=i

min_x1 = sys.maxsize
max_x2 = -sys.maxsize
for i in range(n):
    if i==skip:
        continue
    min_x1 = min(min_x1, x1[i])
    max_x2 = max(max_x2, x2[i])

ans = max_x2-min_x1

skip=0
for i in range(n):
    if x2[skip]<x2[i]:
        skip=i


min_x1 = sys.maxsize
max_x2 = -sys.maxsize
for i in range(n):
    if i==skip:
        continue
    min_x1 = min(min_x1, x1[i])
    max_x2 = max(max_x2, x2[i])
ans = min(ans, max_x2-min_x1)

print(ans)

