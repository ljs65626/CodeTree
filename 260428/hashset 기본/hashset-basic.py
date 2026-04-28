n=int(input())
s =set()

for _ in range(n):
    inp = input()
    if inp.startswith('add'):
        _, v = inp.split()
        v=int(v)
        s.add(v)
    elif inp.startswith('remove'):
        _, v = inp.split()
        v=int(v)
        s.remove(v)
    else:
        _, v = inp.split()
        v=int(v)
        if v in s:
            print('true')
        else:
            print('false')