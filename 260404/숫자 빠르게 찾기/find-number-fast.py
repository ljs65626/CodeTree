n, m = map(int, input().split())
arr = list(map(int, input().split()))
# d={}
# # Please write your code here.
# for i in range(n):
#     d[arr[i]] = i+1

def binary_search(target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right) //2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            right = mid-1
        else:
            left = mid+1
    return -1

for _ in range(m):
    q = int(input())
    # if q in d:
    #     print(d[q])
    # else:
    #     print(-1)
    ret_val = binary_search(q)
    if ret_val!=-1:
        print(ret_val+1)
    else:
        print(ret_val)