import copy
import sys
A = input()
n = len(A)
B = ""
# Please write your code here.

def Encoding(B):
    before=B[0]
    E=""
    cnt=1
    for i in range(1, n):
        if before==B[i]:
            cnt+=1
            if i==n-1:
                E = E + B[i] + str(cnt)
            before = B[i]
        else:
            E = E+before+str(cnt)
            if i==n-1:
                E = E+B[i]+str(cnt)
            before=B[i]
            cnt=1

    return E

if len(A)==1:
    print(2)
    sys.exit()

ans=sys.maxsize
for i in range(n):
    B = A[n-i:] + A[:n-i]
    E = Encoding(B)
    # print(E)
    ans = min(len(E), ans)
print(ans)
