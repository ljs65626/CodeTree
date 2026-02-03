a = list(map(int, input().split()))

# Please write your code here.

if a[1]-a[0]>a[2]-a[1]:
    print(a[1]-a[0]-1)
else:
    print(a[2]-a[1-1])