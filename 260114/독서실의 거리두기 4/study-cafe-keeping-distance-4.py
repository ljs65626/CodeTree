import sys
N = int(input())
seat = list(map(int, list(input())))
ans=-sys.maxsize
# Please write your code here.
for i in range(N):
    if seat[i]==1:
        continue
    seat[i]=1
    for j in range(N):
        if seat[j]==1:
            continue
        seat[j]=1
        before=-1
        min_diff = sys.maxsize
        diff=sys.maxsize
        for k in range(N):
            if seat[k]==1 and before==-1:
                before=k
            elif seat[k]==1:
                diff=k-before
                before=k
            min_diff = min(diff, min_diff)
        
        ans = max(min_diff, ans)
        seat[j]=0
    seat[i]=0

print(ans)