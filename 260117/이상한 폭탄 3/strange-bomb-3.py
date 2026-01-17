n, k = map(int, input().split())
num = [int(input()) for _ in range(n)]
max_a = max(num)
# Please write your code here.
# ans=0
# max_val=0
# for i in range(n):
#     cnt=0
#     for j in range(i+1, i+k+1):
#         if j>=n:
#             break
#         if num[i]==num[j]:
#             if cnt==0:
#                 cnt+=1
#             cnt+=1
#     if cnt>=1 and cnt>=max_val:
#         max_val=cnt
#         if num[i]>ans:
#             ans=num[i]

# print(ans)
# print(max_val)

bomb = [0] * (max_a+1)
exploded = [False] * n
for i in range(n):
    for j in range(i+1, i+k+1):
        if j>=n:
            break
        if num[i]!=num[j]:
            continue
        if exploded[i]==False:
            bomb[num[i]]+=1
            exploded[i]=True
        if exploded[j]==False:
            bomb[num[j]]+=1
            exploded[j]=True

maxval=1
maxidx=0
for i in range(1, max_a+1):
    if bomb[i]>=maxval:
        maxval=bomb[i]
        maxidx=i

print(maxidx)
# print(maxval)


