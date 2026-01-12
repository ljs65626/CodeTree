import sys
n=int(input())
seat = list(map(int, list(input())))
# Please write your code here.
ans=-sys.maxsize
for i in range(n):
    if seat[i]!=1:
        seat[i]=1
        before_index=-1
        small_diff = sys.maxsize
        for j in range(n):
            if before_index==-1 and seat[j]==1:
                before_index=j
            elif seat[j]==1:
                diff = j-before_index         
                small_diff = min(diff, small_diff)
                before_index=j
                
        ans = max(small_diff, ans)

        seat[i]=0


print(ans)