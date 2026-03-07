n, m, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), q) for r, q in [tuple(input().split()) for _ in range(q)]]

# Please write your code here.

def move(i, dir):
    if i<0 or i>=n:
        return
    if dir=='L':
        temp = arr[i][m-1]
        for j in range(m-2, -1, -1):
            arr[i][j+1] = arr[i][j]
        arr[i][0] = temp
        ##
    else:
        ##
        temp = arr[i][0]
        for j in range(1, m):
            arr[i][j-1] = arr[i][j]
        arr[i][m-1] = temp
        ##

def issame_down(i):
    if i+1<n:
        for j in range(m):
            if arr[i][j]==arr[i+1][j]:
                return True
    return False

def issame_up(i):
    if i-1>=0:
        for j in range(m):
            if arr[i][j]==arr[i-1][j]:
                return True
    return False


for r, q in winds:
    r-=1
    move(r, q)
    tmp1 = r
    tmp2 = q

    ##test##
    # for i in arr:
    #     for j in i:
    #         print(j, end=' ')
    #     print()
    # print()
    ##test##

    while r>=0 and issame_up(r)==True:
        r-=1
        if q=='L':
            move(r, 'R')
            q='R'
        else:
            move(r, 'L')
            q='L'
    r=tmp1
    q=tmp2

    ##test##
    # for i in arr:
    #     for j in i:
    #         print(j, end=' ')
    #     print()
    # print()
    ##test##

    while r<n and issame_down(r)==True:
        r+=1
        if q=='L':
            move(r, 'R')
            q='R'
        else:
            move(r, 'L')
            q='L'

    ##test##
    # for i in arr:
    #     for j in i:
    #         print(j, end=' ')
    #     print()
    # print()
    ###
    

for i in arr:
    for j in i:
        print(j, end=' ')
    print()