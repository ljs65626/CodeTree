n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
sum_val=0
diff=0
for a, b in zip(A, B):
    a+=diff
    diff = a-b
    sum_val+=diff
print(sum_val)