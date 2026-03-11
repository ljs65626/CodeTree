import copy
import sys
n, m = map(int, input().split())
num = [int(input()) for _ in range(n)]

if m==1:
    print(0)
    sys.exit()

# Please write your code here.
while True:
    tmp=[]
    before=num[0]
    ccnt=1
    for i in range(1, n):
        if before==num[i]:
            ccnt+=1
        else:
            if ccnt<m:
                for j in range(ccnt):
                    tmp.append(before)
            ccnt=1
        if i==n-1:
            if ccnt<m:
                for j in range(ccnt):
                    tmp.append(num[i])
        before=num[i]
    if n==len(tmp) or n==1:
        break
    num = copy.deepcopy(tmp)
    n = len(num)
    if n==0:
        break

print(len(num))
for i in range(n):
    print(num[i])
