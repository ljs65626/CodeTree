n, m = map(int, input().split())
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))

# Please write your code here.

print(len(A-B)+len(B-A))
