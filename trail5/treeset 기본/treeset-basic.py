from sortedcontainers import SortedSet
n=int(input())
ss = SortedSet()

for _ in range(n):
    inp = input()
    if inp.startswith('add'):
        _, x = inp.split()
        x = int(x)
        ss.add(x)
    elif inp.startswith('remove'):
        _, x = inp.split()
        x=int(x)
        ss.remove(x)
    elif inp.startswith('find'):
        _, x = inp.split()
        x=int(x)
        if x in ss:
            print('true')
        else:
            print('false')
    elif inp.startswith('lower'):
        _, x = inp.split()
        x=int(x)
        idx = ss.bisect_left(x)
        if idx!=len(ss):
            print(ss[idx])
        else:
            print('None')
    elif inp.startswith('upper'):
        _, x = inp.split()
        x=int(x)
        idx = ss.bisect_right(x)
        if idx!=len(ss):
            print(ss[idx])
        else:
            print('None')
    elif inp.startswith('largest'):
        if len(ss)!=0:
            print(ss[-1])
        else:
            print('None')
    else:
        if len(ss)!=0:
            print(ss[0])
        else:
            print('None')