n, m = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.
maxa=max(a)
for i in range(maxa, 100001):
    sumval=0
    cnt=0
    for j in a:
        if sumval+j<=i:
            sumval+=j
        elif sumval+j>i:
            cnt+=1
            sumval=j
    cnt+=1

    if cnt<=m:
        print(i)
        break
    
