import sys
n = int(input())
cnt=0
# Please write your code here.
if n==5:
    print(1)
    sys.exit()
if n==2:
    print(1)
    sys.exit()

while n>0:
    if n-5>=2:
        cnt+=1
        n-=5
        continue
    
    n-=2
    cnt+=1

if n==0:
    print(cnt)
else:
    print(-1)