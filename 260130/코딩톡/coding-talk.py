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

target_c, target_u = message[p-1]
target_u = int(target_u)
for i in range(p-1, -1, -1):
    c, u = message[i]
    u=int(u)
    if u!=target_u:
        break
    is_read[programers.index(c)] = True


for i, (c, u) in enumerate(message, start=1):
    u = int(u)
    if i>=p:
        if p==i and u==0:
            sys.exit()
        is_read[programers.index(c)] = True


for i in range(n):
    if is_read[i]==False:
        print(programers[i], end=' ')


