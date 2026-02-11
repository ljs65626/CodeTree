import sys
n = int(input())
a = list(map(int, input().split()))
second_min = sys.maxsize
second_index=-1
# Please write your code here.
for i in range(1, n):
    if a[i] > a[0]:
        if a[i]<second_min:
            second_min = a[i]
            second_index=i+1

print(second_index)
