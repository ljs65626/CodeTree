import sys
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
arr = [0]
ans = sys.maxsize
visited=[False]*n
# Please write your code here.

def backtrack(curr_node, sum_val, cnt):
    global ans
    if sum_val>=ans:
        return

    if cnt==n:
        if grid[curr_node][0]!=0:
            sum_val+=grid[curr_node][0]
            ans = min(sum_val, ans)
        return
    
    for next_node in range(1, n):
        if visited[next_node]==True or grid[curr_node][next_node]==0:
            continue
        visited[next_node]=True
        backtrack(next_node, sum_val+grid[curr_node][next_node], cnt+1)
        visited[next_node]=False

backtrack(0, 0, 1)
print(ans)




# import sys

# n = int(input())
# grid = [list(map(int, input().split())) for _ in range(n)]
# visited = [False] * n

# ans = sys.maxsize

# # curr_node: 현재 위치한 도시
# # sum_val: 지금까지 발생한 비용
# # count: 지금까지 방문한 도시의 수
# def backtrack(curr_node, sum_val, count):
#     global ans
    
#     # [가지치기 1] 이미 현재 비용이 구상해둔 최소 비용 이상이라면 더 탐색할 필요가 없음
#     if sum_val >= ans:
#         return
    
#     # 기저 조건: 모든 도시를 다 방문했을 때
#     if count == n:
#         # 마지막 도시에서 출발지(0번 도시)로 돌아갈 수 있는지 확인
#         if grid[curr_node][0] != 0:
#             # 돌아가는 비용을 포함하여 최소값 갱신
#             ans = min(ans, sum_val + grid[curr_node][0])
#         return
    
#     for next_node in range(1, n):
#         # 방문하지 않았고, '가는 길이 있는 경우(비용이 0이 아닌 경우)'에만 탐색
#         # [가지치기 2] 갈 수 없는 길은 아예 들어가지 않음으로써 is_True() 함수를 대체함
#         if not visited[next_node] and grid[curr_node][next_node] != 0:
#             visited[next_node] = True
#             backtrack(next_node, sum_val + grid[curr_node][next_node], count + 1)
#             visited[next_node] = False

# # 0번 도시에서 출발 (방문 처리)
# visited[0] = True
# # backtrack(현재 노드, 누적 비용, 방문한 노드 개수)
# backtrack(0, 0, 1)

# print(ans)