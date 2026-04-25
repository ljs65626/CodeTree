import sys
n = int(input())
# cnt=0
# # Please write your code here.

# while n>0:
#     if n==5:
#         cnt+=1
#         n-=5
#         break
#     if (n-5)>3:
#         cnt+=1
#         n-=5
#         continue
    
#     n-=2
#     cnt+=1

# if n==0:
#     print(cnt)
# else:
#     print(-1)

ans=sys.maxsize
for i in range(0, 100_001):
    if (n-(5*i))>=0:
        if (n-(5*i))%2==0:
            cnt = i+((n-(5*i))//2)
            ans = min(ans, cnt)

print(ans)