n, t = map(int, input().split())
belt = [list(map(int, input().split())) for _ in range(3)]
# l = list(map(int, input().split()))
# r = list(map(int, input().split()))
# d = list(map(int, input().split()))

# Please write your code here.


for _ in range(t):
    last = belt[2][n-1]
    for i in range(2, -1, -1):
        for j in range(n-2, -1, -1):
            belt[i][j+1] = belt[i][j]
        if i==2:
            belt[i][0] = belt[1][n-1]
        elif i==1:
            belt[i][0] = belt[0][n-1]
        else:
            belt[i][0] = last
    
    # for i in belt:
    #     for j in i:
    #         print(j, end=' ')
    #     print()
    # print()

for i in belt:
    for j in i:
        print(j, end=' ')
    print()