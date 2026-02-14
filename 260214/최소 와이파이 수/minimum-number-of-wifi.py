n, m = map(int, input().split())
arr = list(map(int, input().split()))
isit=[False]*n
ans=0
# Please write your code here.
for i in range(n):
    if arr[i]==1 and isit[i]==False:
        for j in range(i, i+(2*m+1)):
            if j>=n:
                break
            isit[j]=True
        ans+=1
print(ans)