import sys
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_val = max(arr)

ans=sys.maxsize
def its_possible(i):
    indexes=list()
    for j, elem in enumerate(arr):
        if elem<=i:
            indexes.append(j)

    before_index=0

    for j in indexes:
        dist=j-before_index
        if dist>k:
            return False
        before_index=j
    
    return True

for i in range(max(arr[1], arr[n-1]), max_val+1):
    if its_possible(i):
        # print(i)
        ans = min(ans, i)

print(ans)