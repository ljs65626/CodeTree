from sortedcontainers import SortedDict
n = int(input())
sd = SortedDict()
# Please write your code here.
for _ in range(n):
    inp = input()
    if inp in sd:
        sd[inp]+=1
    else:
        sd[inp]=1

for key, value in sd.items():
    print(f"{key} {(value/n)*100:.4f}")