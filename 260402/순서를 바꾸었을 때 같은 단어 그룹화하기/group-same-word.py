n = int(input())
d={}

for _ in range(n):
    inp = input()
    sum_val=0
    for i in range(len(inp)):
        sum_val += ord(inp[i])
    
    if sum_val in d:
        d[sum_val]+=1
    else:
        d[sum_val]=1

ans=0
for k, v in d.items():
    ans = max(v, ans)

print(ans)