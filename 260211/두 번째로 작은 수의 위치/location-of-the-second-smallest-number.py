import sys
n = int(input())
a = list(map(int, input().split()))
b = a[:]
b.sort()
second=-1
# Please write your code here.
for i in range(1, n):
    if b[i]>b[0] and second==-1:
        second=b[i]
    elif second==b[i]:
        print(-1)
        sys.exit()


if second!=-1:
    print(a.index(second)+1)
else:
    print(second)
