from sortedcontainers import SortedDict

n=int(input())
sd = SortedDict()

for _ in range(n):
    inp = input()

    if inp.startswith('add'):
        _, k, v = inp.split()
        k = int(k)
        v = int(v)
        sd[k] = v
    elif inp.startswith('remove'):
        _, k = inp.split()
        k=int(k)
        sd.pop(k)
    elif inp.startswith('find'):
        _, k = inp.split()
        k=int(k)
        if k in sd:
            print(sd[k])
        else:
            print('None')
    else:
        if len(sd)!=0:
            for v in sd.values():
                print(v, end=' ')
            print()
        else:
            print('None')
        