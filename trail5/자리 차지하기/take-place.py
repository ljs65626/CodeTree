from sortedcontainers import SortedSet
n, m = map(int, input().split())
arr = list(map(int, input().split()))
ss = SortedSet(list(range(-1, -(m+1), -1)))
# Please write your code here.
# print(ss)
ans=0
for a in arr:
    if len(ss)==0:
        break
    i = ss.bisect_left(-a)
    if i!=len(ss):
        ss.remove(ss[i])
        ans+=1
    else:
        break

print(ans)