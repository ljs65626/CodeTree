n, m = map(int, input().split())
d= dict()
arr = [input() for _ in range(n)]
cnt=1
for i in arr:
    d[i] = cnt
    cnt+=1

for _ in range(m):
    inp = input()
    if inp not in d:
        inp = int(inp)
        print(arr[inp-1])
    else:
        print(d[inp])