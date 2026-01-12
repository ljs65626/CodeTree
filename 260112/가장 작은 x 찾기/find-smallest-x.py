import sys
n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
# a, b = zip(*ranges)
# a, b = list(a), list(b)

# Please write your code here.


# first_a, first_b = a[0], b[0]
# for i in range(first_a, first_b+1):
#     for j in range(n):
#         if i<a[j] or i>b[j]:
#             i*=2

ans=sys.maxsize
for i in range(1, 10001):
    is_satisfied=True
    cnt=1
    for a, b in ranges:
        if i*2**cnt<a or i>b*2**cnt:
            is_satisfied=False
            break
        cnt+=1
        
    if is_satisfied:
        ans=min(i, ans)

print(ans)

