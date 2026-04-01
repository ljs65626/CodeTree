n = int(input())
d= dict()
for _ in range(n):
    inp = input()
    if inp in d:
        d[inp] +=1
    else:
        d[inp] = 1

ans = 0
for k in d:
    ans = max(ans, d[k])

print(ans)