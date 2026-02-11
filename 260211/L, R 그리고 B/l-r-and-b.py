board = [list(input()) for _ in range(10)]

# Please write your code here.
for i in range(10):
    for j in range(10):
        if board[i][j]=='B':
            bi=i
            bj=j
        elif board[i][j]=='L':
            li=i
            lj=j

print(abs(bi-li)+abs(bj-lj)-1)