import sys
n = int(input())
arr=[]
# Please write your code here.

def print_ans():
    for i in arr:
        print(i, end='')

def is_continuous(i, j):
    mid = (i+j)//2
    if arr[i:mid+1]==arr[mid+1:j+1]:
        return True
    else:
        return False

def check(num):
    arr.append(num)
    leng = len(arr)
    for i in range(leng):
        for j in range(i+1, leng, 2):
            if is_continuous(i, j):
                arr.pop()
                return False
    return True


def backtrack(curr_num):
    if curr_num==n+1:
        print_ans()
        sys.exit()
        return
    
    for i in range(4, 7):
        if check(i):
            backtrack(curr_num+1)
            arr.pop()
        else:
            continue

backtrack(1)