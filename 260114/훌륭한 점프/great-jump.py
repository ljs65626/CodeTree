import sys
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_val = max(arr)

ans=sys.maxsize
def is_possible(i):

    before_index=0

    for j in range(1, n):
        if arr[j]<=i:
            dist=j-before_index
            if dist>k:
                return False
            before_index=j
    
    return True

for i in range(max(arr[0], arr[n-1]), max_val+1):
    if is_possible(i):
        # print(i)
        ans = min(ans, i)

print(ans)