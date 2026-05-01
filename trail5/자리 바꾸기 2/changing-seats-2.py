n, k = tuple(map(int, input().split()))
change = [tuple(map(int, input().split())) for _ in range(k)]
arr = list(range(n+1))
move = [set() for _ in range(n+1)]
# 3K에 걸쳐 자리바꿈이 진행

for i in range(1, n+1):
    move[i].add(i)

for _ in range(3):
    for i, j in change:
        move[arr[i]].add(j)
        move[arr[j]].add(i)
        arr[i], arr[j] = arr[j], arr[i]


for i in range(1, n+1):
    print(len(move[i]))
