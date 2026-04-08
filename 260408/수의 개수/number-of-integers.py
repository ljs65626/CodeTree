import sys
n, m = map(int, input().split())
arr = list(map(int, input().split()))


# Please write your code here.
def upper_bound(target):
    left = 0
    right = n-1
    min_idx = sys.maxsize
    while left<=right:
        mid = (left+right)//2
        if arr[mid]>target:
            right = mid-1
            min_idx = min(min_idx, mid)
        else:
            left = mid+1
    if min_idx==sys.maxsize:
        return 0
    else:
        return min_idx

def lower_bound(target):
    left = 0
    right = n-1
    min_idx = sys.maxsize
    while left<=right:
        mid = (left+right)//2
        if arr[mid]>=target:
            right = mid-1
            min_idx = min(min_idx, mid)
        else:
            left = mid+1
    if min_idx==sys.maxsize:
        return 0
    else:
        return min_idx

for _ in range(m):
    inp = int(input())
    upper = upper_bound(inp)
    lower = lower_bound(inp)
    if upper-lower<0:
        print(1)
    else:
        print(upper-lower)