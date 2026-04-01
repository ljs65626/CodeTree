n = int(input())
d = dict()

for _ in range(n):
    inp = input()
    if inp.startswith('add'):
        a, b, c = inp.split()
        b = int(b)
        c = int(c)
        d[b] = c
    elif inp.startswith('remove'):
        a, b = inp.split()
        b = int(b)
        d.pop(b)
    else:
        a, b = inp.split()
        b = int(b)
        if b in d:
            print(d[b])
        else:
            print(None)