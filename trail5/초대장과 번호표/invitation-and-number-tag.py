from collections import deque
N, G = map(int, input().split())
ans=1
person_to_groups = [[] for _ in range(N+1)]
uninvited_sets = []
is_invited = set()
q = deque()

for i in range(G):
    data = tuple(map(int, input().split()))
    
    members = set(data[1:])
    uninvited_sets.append(members)

    for mem in members:
        person_to_groups[mem].append(i)

# print(person_to_groups)
# print(uninvited_sets)


def bfs():
    global ans
    while q:
        curr = q.popleft()
        for group_idx in person_to_groups[curr]:
            if curr in uninvited_sets[group_idx]:
                uninvited_sets[group_idx].remove(curr)
            if len(uninvited_sets[group_idx])==1:
                last_person = uninvited_sets[group_idx].pop()
                if last_person not in is_invited:
                    ans+=1
                    is_invited.add(last_person)
                    q.append(last_person)
    
q.append(1)
bfs()
print(ans)