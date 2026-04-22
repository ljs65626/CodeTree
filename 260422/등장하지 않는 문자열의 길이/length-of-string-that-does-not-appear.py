n = int(input())
inp = input()

# Please write your code here.
ans=0
for i in range(1, n+1):
    for j in range(n-i+1):
        origin = inp[j:j+i]
        for k in range(j+1, n-i+1):
            nextt = inp[k:k+i]
            if origin==nextt:
                ans = i
print(ans+1)