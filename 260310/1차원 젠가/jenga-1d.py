import copy
n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.
tmp = []

for i in range(n):
    if i>=s1-1 and i<=e1-1:
        continue
    tmp.append(blocks[i])

blocks = copy.deepcopy(tmp)

tmp = []
leng = len(blocks)
for i in range(leng):
    if i>=s2-1 and i<=e2-1:
        continue
    tmp.append(blocks[i])

blocks = copy.deepcopy(tmp)

print(len(blocks))
for i in blocks:
    print(i)


