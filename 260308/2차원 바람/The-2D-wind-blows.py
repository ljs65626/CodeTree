import copy
import sys
n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]
if q==0:
    for i in a:
        for j in i:
            print(j, end=' ')
        print()
    sys.exit(0)
# Please write your code here.
def move(x1, y1, x2, y2):
    temp1 = a[x1][y2]
    for i in range(y2-1, y1-1, -1):
        a[x1][i+1] = a[x1][i]
    
    ##test##
    # for i in a:
    #     for j in i:
    #         print(j, end=' ')
    #     print()
    # print()
    ##test##

    temp2 = a[x2][y2]
    for i in range(x2-1, x1, -1):
        a[i+1][y2] = a[i][y2]
    a[x1+1][y2] = temp1

    temp3 = a[x2][y1]
    for i in range(y1, y2):
        a[x2][i] = a[x2][i+1]
    a[x2][y2-1] = temp2

    ##test##
    # for i in a:
    #     for j in i:
    #         print(j, end=' ')
    #     print()
    ##test##

    temp4 = a[x1][y1]
    for i in range(x1, x2-1):
        a[i][y1] = a[i+1][y1]
    a[x2-1][y1] = temp3


def range_count(i, j):
    cnt=1
    if i-1>=0:
        cnt+=1
    if i+1<n:
        cnt+=1
    if j-1>=0:
        cnt+=1
    if j+1<m:
        cnt+=1
    
    return cnt

def total(i, j):
    sum_val=0
    sum_val+=a[i][j]
    if i-1>=0:
        sum_val+=a[i-1][j]
    if i+1<n:
        sum_val+=a[i+1][j]
    if j-1>=0:
        sum_val+=a[i][j-1]
    if j+1<m:
        sum_val+=a[i][j+1]
    return sum_val



for x1, y1, x2, y2 in winds:
    x1-=1
    y1-=1
    x2-=1
    y2-=1
    move(x1, y1, x2, y2)
    temp = copy.deepcopy(a)
    # for i in a:
    #     for j in i:
    #         print(j, end=' ')
    #     print()
    # print()

    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            temp[i][j] = total(i, j) // range_count(i, j)
    
    a=copy.deepcopy(temp)


for i in temp:
    for j in i:
        print(j, end=' ')
    print()

