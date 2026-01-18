n, m = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.

for i in range(100001):
    sumval=0
    cnt=0
    for j in a:
        if sumval+j<=i:
            sumval+=j
        else:
            cnt+=1
            sumval=j
    cnt+=1

    if cnt==m:
        print(i)
        break
    
