n = int(input())
status = [tuple(input().split()) for _ in range(n)]

# Please write your code here.
# A=0
# B=0
# C=0
# current=0
# ans=0
# for c, s in status:
#     s = int(s)
#     before=current
#     if c=='A':
#         A+=s
#     elif c=='B':
#         B+=s
#     else:
#         C+=s
#     if A==B==C:
#         current=0
#     elif A==B and A>C:
#         current=1
#     elif A==C and A>B:
#         current=2
#     elif B==C and B>A:
#         current=3
#     elif (A==B and A<C) or (A<B<C) or (B<A<C):
#         current=4
#     elif (A==C and A<B) or (A<C<B) or (C<A<B):
#         current=5
#     elif (C==B and C<A) or (C<B<A) or (B<C<A):
#         current=6
    
#     if current!=before:
#         ans+=1

# print(ans)

ans=0
A=0
B=0
C=0
def get_status(score1, score2, score3):
    score=0
    maxval = max(score1, score2, score3)
    if maxval==score1:
        score+=1
    
    if maxval==score2:
        score+=2
    
    if maxval==score3:
        score+=4
    
    return score


for c, s in status:
    s = int(s)
    
    if c=='A':
        if get_status(A, B, C) != get_status(A+s, B, C):
            ans+=1
        A+=s
    elif c=='B':
        if get_status(A, B, C) != get_status(A, B+s, C):
            ans+=1
        B+=s
    else:
        if get_status(A, B, C) != get_status(A, B, C+s):
            ans+=1
        C+=s
print(ans)