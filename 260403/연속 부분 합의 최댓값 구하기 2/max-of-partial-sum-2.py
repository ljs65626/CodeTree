import sys
n=int(input())
arr = list(map(int, input().split()))
max_val=-sys.maxsize
sum_val=0
all_minus = True
for i in range(n):
    if arr[i]>=0:
        all_minus=False

if all_minus:
    print(max(arr))
    sys.exit()

for i in range(n):
    sum_val+=arr[i]
    if sum_val<0:
        sum_val=0
        continue
    max_val = max(max_val, sum_val)

print(max_val)