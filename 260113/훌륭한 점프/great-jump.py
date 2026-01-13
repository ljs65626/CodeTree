import sys
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_val = max(arr)

ans=sys.maxsize
def its_possible(i):
    indexes=list()
    for j, elem in enumerate(arr):
        if j==0 or j==n-1 or elem<=i:
            indexes.append(j)
    
    max_val2=0
    for j in indexes:
        max_val2 = max(arr[j], max_val2)
    
    if max_val2!=i:
        return False

    before_index=0

    for j in indexes:
        dist=j-before_index
        if dist>k:
            return False
        before_index=j
    
    return True

for i in range(1, max_val+1):
    if its_possible(i):
        # print(i)
        ans = min(ans, i)

print(ans)