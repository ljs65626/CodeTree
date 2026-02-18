n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.


# for i in range(2, n):
#     if sequence[0]==sequence[i]-1:
#         k=0
#         for j in range(1, i):
#             sequence[k], sequence[j] = sequence[j], sequence[k]
#             k+=1
#     elif sequence[0]-1==sequence[i]:
#         k=0
#         for j in range(1, i+1):
#             sequence[k], sequence[j] = sequence[j], sequence[k]
#             k+=1


before=sequence[0]
continuous=1
for i in range(1, n):
    if sequence[i]>before:
        continuous+=1
    else:
        continuous=1
    before=sequence[i]

if continuous==n:
    print(0)
else:
    print(n-continuous)