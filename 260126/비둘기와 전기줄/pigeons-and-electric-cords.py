N = int(input())



# Please write your code here.
is_First = [-1] * 11

ans=0
for _ in range(N):
    p, pos = map(int, input().split())
    if is_First[p]==-1:
        is_First[p] = pos
    else:
        if is_First[p]!=pos:
            ans+=1
            is_First[p] = pos

print(ans)

