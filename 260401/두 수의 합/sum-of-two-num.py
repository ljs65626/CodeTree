n, k = map(int, input().split())
d = {}
arr = list(map(int, input().split()))
for i in arr:
    if i in d:
        d[i] +=1
    else:
        d[i] = 1

ans=0
for key in d:
    if (k-key in d) and d[key]>0 and d[k-key]>0:
        d[key]-=1
        d[k-key]-=1
        ans+=1
print(ans)
