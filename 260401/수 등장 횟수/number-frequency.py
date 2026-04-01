n, m = map(int, input().split())
n_arr = list(map(int, input().split()))
m_arr = list(map(int, input().split()))

d= dict()

for i in n_arr:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

# print(d)
for i in m_arr:
    if i in d:
        print(d[i], end=' ')
    else:
        print(0, end=' ')


#count() 함수는 O(N)이기 때문에 결국 O(N^2)으로 시간 초과이다.
# for i in m_arr:
#     print(n_arr.count(i), end=' ')