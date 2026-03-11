import copy
n, m = map(int, input().split())
num = [int(input()) for _ in range(n)]

# Please write your code here.
while True:
    # if n<=1:
    #     break
    # tmp=[]
    # for i in range(n):
    #     if i==0:
    #         if num[i]!=num[i+1]:
    #             tmp.append(num[i])
    #     elif i==n-1:
    #         if num[i]!=num[i-1]:
    #             tmp.append(num[i])
    #     else:
    #         if num[i]!=num[i+1] and num[i]!=num[i-1]:
    #             tmp.append(num[i])
    # if n==len(tmp):
    #     break
    # num = copy.deepcopy(tmp)
    # n = len(num)
    tmp=[]
    before=num[0]
    ccnt=1
    for i in range(1, n):
        if before==num[i]:
            ccnt+=1
        else:
            if ccnt<m:
                tmp.append(before)
            ccnt=1
        if i==n-1:
            if ccnt<m:
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



