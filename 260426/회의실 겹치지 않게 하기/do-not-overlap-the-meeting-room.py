n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
meetings.sort(key=lambda t : t[1])
cnt=1
before=0
for i in range(1, n):
    start, end = meetings[i]
    b_start, b_end = meetings[before]
    if start>=b_end:
        cnt+=1
        before = i

print(n-cnt)