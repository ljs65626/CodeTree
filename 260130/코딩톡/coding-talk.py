import sys
n, m, p = map(int, input().split())
message = [tuple(input().split()) for _ in range(m)]
# Please write your code here.

start=65
programers = []
for _ in range(n):
    programers.append(chr(start))
    start+=1
is_read = [False] * n

for i, (c, u) in enumerate(message, start=1):
    if i<p:
        continue
    u = int(u)
    if p==i and u==0:
        sys.exit()
    is_read[programers.index(c)] = True


for i in range(n):
    if is_read[i]==False:
        print(programers[i], end=' ')


