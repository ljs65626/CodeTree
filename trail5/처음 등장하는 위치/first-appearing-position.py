from sortedcontainers import SortedDict
n = int(input())
arr = list(map(int, input().split()))
sd = SortedDict()
# Please write your code here.
for i in range(n):
    if arr[i] in sd:
        continue
    else:
        sd[arr[i]] = i+1

for key, value in sd.items():
    print(key, value)
