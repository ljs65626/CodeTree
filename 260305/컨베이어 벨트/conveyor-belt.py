n, t = map(int, input().split())
belt = [list(map(int, input().split())) for _ in range(2)]
# Please write your code here.
for _ in range(t):
    temp = belt[1][n-1]
    for i in range(1, -1, -1):
        for j in range(n-2, -1, -1):
            belt[i][j+1] = belt[i][j]
        if i==1:
            belt[1][0] = belt[0][n-1]
        if i==0:
            belt[0][0] = temp

for i in belt:
    for j in i:
        print(j, end=' ')
    print()
