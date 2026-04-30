n = int(input())
a = list(map(int, input().split()))
set1 = set(a)



m = int(input())
b = list(map(int, input().split()))

# Please write your code here.

for inp in b:
    if inp in set1:
        print(1)
    else:
        print(0)
