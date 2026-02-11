n = int(input())
status = [tuple(input().split()) for _ in range(n)]

# Please write your code here.
A=0
B=0
C=0
current=0
ans=0
for c, s in status:
    s = int(s)
    before=current
    if c=='A':
        A+=s
    elif c=='B':
        B+=s
    else:
        C+=s
    
    if A==B==C:
        current=0
    elif A==B and A>C:
        current=1
    elif A==C and A>B:
        current=2
    elif B==C and B>A:
        current=3
    elif A==B and A<C:
        current=4
    elif A==C and A<B:
        current=5
    else:
        current=6
    
    if current!=before:
        ans+=1

print(ans)