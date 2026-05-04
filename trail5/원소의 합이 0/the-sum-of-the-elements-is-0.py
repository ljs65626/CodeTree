n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))
ans=0
# Please write your code here.
d=dict()

for i in C:
    for j in D:
        key=i+j
        if key in d:
            d[key]+=1
        else:
            d[key]=1

# print(d)

for a in A:
    for b in B:
        ab = a+b
        if -ab in d:
            ans+=d[-ab]
print(ans)