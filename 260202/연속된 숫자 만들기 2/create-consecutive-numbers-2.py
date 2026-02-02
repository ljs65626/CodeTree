pos = list(map(int, input().split()))
pos.sort()
# Please write your code here.

if (pos[1]-pos[0])==1 and (pos[2]-pos[1])==1:
    ans=0
elif (pos[1]-pos[0]==2) or (pos[2]-pos[1]==2):
    ans=1
else:
    ans=2

print(ans)

