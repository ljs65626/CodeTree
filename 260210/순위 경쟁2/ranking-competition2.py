n = int(input())
lists = [tuple(input().split()) for _ in range(n)]

# Please write your code here.
current = 0
A =0
B=0
ans=0
for c, s in lists:
    s = int(s)
    before = current
    if c=='A':
        A+=s
    else:
        B+=s
    
    if A==B:
        current=0
    elif A>B:
        current=1
    else:
        current=2
    
    if before!=current:
        ans+=1

print(ans)