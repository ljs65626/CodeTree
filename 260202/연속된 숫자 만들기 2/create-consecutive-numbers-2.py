a,b,c = tuple(map(int, input().split()))

# Please write your code here.

if b-a==1 and c-b==1:
    ans=0
elif (b-a==2) or (c-b==2):
    ans=1
else:
    ans=2

print(ans)