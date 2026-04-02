n, k = map(int, input().split())
arr = list(map(int, input().split()))
d = {}
arr2 = []
# Please write your code here.
for num in arr:
    if num in d:
        d[num]+=1
    else:
        d[num] = 1
# print(d)

for key in d:
    arr2.append((key, d[key]))

arr2.sort(key=lambda t: (-t[1], -t[0]))

for i in range(k):
    print(arr2[i][0], end=' ')

"""

d = {
    3 : 2
    1 : 2
    2 : 1
}


"""
