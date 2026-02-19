arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
A = arr[0]
B = arr[1]
C = arr[2]
ABCD = arr[-1]
D = ABCD-(A+B+C)

print(A, B, C, D)