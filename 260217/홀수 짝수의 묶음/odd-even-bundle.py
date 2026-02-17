import sys
N = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
odd_cnt=0
even_cnt=0
for i in numbers:
    if i%2==0:
        even_cnt+=1
    else:
        odd_cnt+=1

while odd_cnt>even_cnt:
    odd_cnt-=2
    even_cnt+=1

if even_cnt==odd_cnt:
    print(even_cnt+odd_cnt)
    sys.exit()

if odd_cnt==0:
    print(1)
    sys.exit()

print((odd_cnt*2)+1)

