n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
plus_cnt = 0
minus_cnt = 0
zero_cnt = 0
for i in range(n):
    if arr[i]<0:
        minus_cnt+=1
    elif arr[i]>0:
        plus_cnt+=1
    else:
        zero_cnt+=1

arr.sort()
if minus_cnt>=2 and plus_cnt>=1:
    max_candidate1 = arr[0]*arr[1]*arr[-1]
    max_candidate2 = arr[-1]*arr[-2]*arr[-3]
    ans = max(max_candidate1, max_candidate2)
elif (minus_cnt==0) or (minus_cnt==1) or (plus_cnt==0):
    ans=arr[-1]*arr[-2]*arr[-3]

print(ans)