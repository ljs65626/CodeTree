x1, x2, x3, x4 = map(int, input().split())

# Please write your code here.

# arr = [0] * 101

# for i in range(x1, x2+1):
#     arr[i] += 1

# for i in range(x3, x4+1):
#     arr[i] += 1

# is_satisfied=True
# for i in range(1, 101):
#     if arr[i]>1:
#         is_satisfied=False
#         break

# if is_satisfied:
#     print('nonintersecting')
# else:
#     print('intersecting')

if x2<x3 or x4<x1:
    print('nonintersecting')
else:
    print('intersecting')