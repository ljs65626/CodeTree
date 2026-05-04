from sortedcontainers import SortedSet
t = int(input())

ss = SortedSet()

for _ in range(t):
    k = int(input())
    for _ in range(k):
        inp = input()
        if inp.startswith('I'):
            _, v = inp.split()
            v=int(v)
            ss.add(v)
        elif inp.startswith('D 1'):
            if len(ss)!=0:
                ss.remove(ss[-1])
            else:
                continue
        else:
            if len(ss)!=0:
                ss.remove(ss[0])
            else:
                continue
    
    if len(ss)!=0:
        print(ss[-1], ss[0])
    else:
        print('EMPTY')
    
    ss.clear()