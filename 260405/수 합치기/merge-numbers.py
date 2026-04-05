import heapq
import sys
n=int(input())
arr = list(map(int, input().split()))
heapq.heapify(arr) #기본 min-heap
sum_val=0
if len(arr)==1:
    print(0)
    sys.exit()

while len(arr)!=1:
    first=heapq.heappop(arr) # 꺼낸 후 다시 힙 정렬
    second = heapq.heappop(arr) # 꺼낸 후 다시 힙 정렬
    sum_val += (first+second)
    heapq.heappush(arr, first+second) # 넣은 다시 힙 정렬

print(sum_val)