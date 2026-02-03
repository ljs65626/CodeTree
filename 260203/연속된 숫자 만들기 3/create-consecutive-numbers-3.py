import sys
a = list(map(int, input().split()))

# Please write your code here.

if (a[1]-a[0]==1) and (a[2]-a[1]==1):
    print(0)
    sys.exit()

if a[1]-a[0]>a[2]-a[1]:
    print(a[1]-a[0]-1)
else:
    print(a[2]-a[1-1])