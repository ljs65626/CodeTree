nums = list(map(int, input().split()))
nums.sort()
# Please write your code here.


def is_possible():
    for i in range(1, 41):
        for j in range(1, 41):
            for k in range(1, 41):
                for l in range(1, 41):
                    a = [i, j, k, l, i+j, j+k, k+l, l+i, i+k, j+l, i+j+k, i+j+l, i+k+l, j+k+l, i+j+k+l]
                    a.sort()
                    if a==nums:
                        return (i, j, k, l)



i, j, k, l = is_possible()
print(i, j, k, l)



