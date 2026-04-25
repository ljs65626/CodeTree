N = int(input())
B = [int(input()) for _ in range(N)]
A = []
# Please write your code here.

b_cards = set(B) 


for i in range(1, 2*N+1):
    if i not in b_cards:
        A.append(i)
ans=0
B.sort()
B_arrow=0
for i in range(N):
    if A[i]>B[B_arrow]:
        ans+=1
        B_arrow+=1

print(ans)
