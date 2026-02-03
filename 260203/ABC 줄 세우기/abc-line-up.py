n = int(input())
arr = list(input().split())

# Please write your code here.
ans=0
while True:
    saved=False
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            saved=True
            ans+=1
    if not saved:
        break

print(ans)