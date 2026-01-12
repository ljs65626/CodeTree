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


def satisfied(x):
    for a, b in ranges:
        x*=2
        if x<a or x>b:
            return False
    return True

ans=sys.maxsize
for i in range(1, 10001):
    if satisfied(i):
        ans = min(ans, i)

print(ans)

