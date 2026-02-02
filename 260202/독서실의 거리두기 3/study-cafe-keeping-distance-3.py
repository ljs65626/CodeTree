import sys
N = int(input())
seats = list(input())

# Please write your code here.

maxdiff = -sys.maxsize
ans = sys.maxsize


before=0
for i in range(1, N):
    if seats[i]=='1':
        diff = i-before

        if diff>maxdiff:
            maxdiff = diff
            maxfirst = before
            maxlast = i

        before = i
ii = (maxfirst+maxlast)//2
seats[ii] = '1'
# print(seats)
before=0
for i in range(1,N):
    if seats[i]=='1':
        diff = i-before
        before = i
        ans = min(ans, diff)

print(ans)