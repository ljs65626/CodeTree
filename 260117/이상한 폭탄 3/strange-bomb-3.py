n, k = map(int, input().split())
num = [int(input()) for _ in range(n)]

# Please write your code here.
ans=0
max_val=0
for i in range(n):
    cnt=0
    for j in range(i, i+k+1):
        if j>=n:
            break
        if i!=j and num[i]==num[j]:
            if cnt==0:
                cnt+=1
            cnt+=1
    if cnt>=1 and cnt>=max_val:
        max_val=cnt
        if num[i]>ans:
            ans=num[i]

print(ans)