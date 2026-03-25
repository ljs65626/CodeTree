n = int(input())
arr=[]
visited=[False]*(n+1)
# Please write your code here.
def print_answer():
    for i in arr:
        print(i, end=' ')
    print()

def backtrack(curr_loc):
    if curr_loc==n+1:
        print_answer()
        return
    
    for i in range(1, n+1):
        if visited[i]==True:
            continue
        
        visited[i]=True
        arr.append(i)
        backtrack(curr_loc+1)
        arr.pop()
        visited[i]=False

backtrack(1)
