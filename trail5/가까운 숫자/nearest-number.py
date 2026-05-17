from sortedcontainers import SortedSet
import sys
n = int(input())
queries = list(map(int, input().split()))
ss = SortedSet([0])
min_val = sys.maxsize
# Please write your code here.
def distance(x):
    global min_val
    right = ss.bisect_right(x)
    mid = right-1
    left = right-2
    if right!=len(ss):
        diff = min((ss[mid]-ss[left]), (ss[right]-ss[mid]))
    else:
        diff = ss[mid]-ss[left]
    
    min_val = min(diff, min_val)
    return min_val


for q in queries:
    ss.add(q)
    print(distance(q))
