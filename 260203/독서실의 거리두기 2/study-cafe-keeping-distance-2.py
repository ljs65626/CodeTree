import sys
N = int(input())
seats = list(map(int, list(input())))

# # Please write your code here.

# ans = -sys.maxsize
# if seats[0]==0:
#     mindiff1 = sys.maxsize
#     seats[0]==1
#     before=0
#     for i in range(1, N):
#         if seats[i]==1:
#             diff = i-before
#             before = i
#             mindiff1 = min(diff, mindiff1)
#     seats[0]==0
#     ans = max(mindiff1, ans)

# if seats[-1]==0:
#     mindiff2 = sys.maxsize
#     seats[-1]=1
#     before=-1
#     for i in range(N):
#         if before==-1 and seats[i]==1:
#             before=i
#         elif seats[i]==1:
#             diff = i-before
#             before=i
#             mindiff2 = min(diff, mindiff2)
#     seats[-1]=0
#     ans = max(ans, mindiff2)

# before=-1
# maxdiff = -sys.maxsize
# diff=-1
# for i in range(N):
#     if before==-1 and seats[i]==1:
#         before = i
#     elif seats[i]==1:
#         diff = i-before
#         if diff>maxdiff:
#             maxi = i
#             maxbefore = before
#             maxdiff = diff
#         before=i


# if diff!=-1:
#     mindiff3 = sys.maxsize
#     seats[(maxi+maxbefore)//2]=1
#     before=-1
#     for i in range(N):
#         if before==-1 and seats[i]==1:
#             before = i
#         elif seats[i]==1:
#             diff = i-before
#             mindiff3 = min(mindiff3, diff)
#             before=i
#     ans = max(mindiff3, ans)

# print(ans)
ans = -sys.maxsize
for i in range(N):
    if seats[i]==0:
        seats[i]=1
        before=-1
        mindiff=sys.maxsize
        for j in range(N):
            if before==-1 and seats[j]==1:
                before=j
            elif seats[j]==1:
                diff=j-before
                mindiff = min(diff, mindiff)
                before=j
        seats[i]=0
        ans = max(ans, mindiff)

print(ans)

