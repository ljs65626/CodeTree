arr = list(map(int, input().split()))
arr.sort()
# Please write your code here.
A = arr[0]
B = arr[1]
ABC = arr[-1]
C = ABC-(A+B)
print(A, B, C)
