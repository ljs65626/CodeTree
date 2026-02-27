n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
cnt=0
for i in range(n):
    base_x, base_y = lines[i]
    for j in range(n):
        if i==j:
            continue
        x, y = lines[j]
        if (base_x<=x and y<=base_y) or (x<=base_x and base_y<=y):
            cnt+=1
    
print(n-cnt)
