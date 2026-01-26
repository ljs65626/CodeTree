N = int(input())



# Please write your code here.
is_First = [True] * 11
number_pos = [0] * 11

ans=0
for _ in range(N):
    p, pos = map(int, input().split())
    if is_First[p]==True:
        is_First[p]=False
        number_pos[p] = pos
    else:
        if number_pos[p]!=pos:
            ans+=1
            number_pos[p] = pos

print(ans)