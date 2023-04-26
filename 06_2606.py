# 바이러스

# 입력부
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[0] for i in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 1번과 연결되어 있는 노드 DFS로 탐색
visited = [0 for i in range(n+1)]
def dfs(x):
    global cnt
    if visited[x] != 0:
        return
    else: # visited[x] == 0
        visited[x] = 1
        cnt += 1
        for i in graph[x]:
            dfs(i)

cnt = 0
dfs(1)
# visited의 0번이랑 1번 방문하는 2개의 경우 빼야해서 cnt-2
print(cnt-2)