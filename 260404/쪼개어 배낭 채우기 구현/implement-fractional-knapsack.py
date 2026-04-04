n, m = map(int, input().split())
dia = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    w, p = dia[i]
    dia[i].append(p/w)

# print(dia)
dia.sort(key=lambda t:-t[2])
# print(dia)
price=0
for i in range(n):
    w, p, wp = dia[i]
    if m>=w:
        m-=w
        price+=p
    else:
        price+=((m/w) * p)
        break
print(f"{price:.3f}")