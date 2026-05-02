n, m = map(int, input().split())

A = [input() for _ in range(n)]
B = [input() for _ in range(n)]
ans=0

# Please write your code here.
def is_seperated(i, j, k):
    s1=set()
    s2=set()
    for a in A:
        s1.add(a[i]+a[j]+a[k])
    for b in B:
        s2.add(b[i]+b[j]+b[k])

    for s in s1:
        if s in s2:
            return False
    return True
    



for i in range(m):
    for j in range(i+1, m):
        for k in range(j+1, m):
            if is_seperated(i, j, k):
                ans+=1

print(ans)