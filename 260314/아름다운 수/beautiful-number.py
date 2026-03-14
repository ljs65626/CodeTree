n = int(input())
ans=0
# Please write your code here.

def check(start, value, arr):
    leng = len(arr)
    for i in range(start+1, leng):
        if arr[start]!=arr[i]:
            return i-1
    return n-1

def beautiful_num(arr):
    two_check=False
    three_check=False
    four_check=False
    for i, v in enumerate(arr):
        end = check(i, v, arr)
        if v==2 and two_check==False:
            if (end-i+1)%2==0:
                two_check=True
            else:
                return False
        elif v==3 and three_check==False:
            if (end-i+1)%3==0:
                three_check=True
            else:
                return False
        elif v==4 and four_check==False:
            if (end-i+1)%4==0:
                four_check=True
            else:
                return False
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