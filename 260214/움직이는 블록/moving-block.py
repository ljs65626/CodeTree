n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.
center = sum(blocks)//n
ans=0
for i in blocks:
    if i>center:
        ans+=i-center

print(ans)