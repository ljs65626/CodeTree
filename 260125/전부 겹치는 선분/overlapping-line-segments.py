import sys
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]


# Please write your code here.
arr = [0] * 101

for x, y in segments:
    for i in range(x, y+1):
        arr[i] += 1

for i in range(1, 101):
    if arr[i]==n:
        print('Yes')
        sys.exit()

print('No')