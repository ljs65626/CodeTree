a, b, x, y = map(int, input().split())

# Please write your code here.

first = abs(a-b)
second = abs(a-x) + abs(y-b)
third = abs(a-y) + abs(x-b)

print(min(first, second, third))