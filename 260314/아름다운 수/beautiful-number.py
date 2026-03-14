n = int(input())

ans=0
# Please write your code here.

def check(start, arr):
    leng = len(arr)
    for i in range(start+1, leng):
        if arr[start]!=arr[i]:
            return i-1
    return n-1

def beautiful_num(arr):
    leng = len(arr)
    i=0
    while True:
        end = check(i, arr)
        if arr[i]==2:
            if (end-i+1)%2==0:
                pass
            else:
                return False
        elif arr[i]==3:
            if (end-i+1)%3==0:
                pass
            else:
                return False
        elif arr[i]==4:
            if (end-i+1)%4==0:
                pass
            else:
                return False
        
        i=end+1

        if i>=leng:
            break

    return True



def backtrack(curr_num, arr):
    global ans
    if n+1==curr_num:
        return
    
    for i in range(1, 5):
        arr.append(i)
        backtrack(curr_num+1, arr)
        # print(arr)
        if beautiful_num(arr) and len(arr)==n:
            ans+=1
            # print(arr)
        arr.pop()

arr=[]
backtrack(1, arr)
print(ans)