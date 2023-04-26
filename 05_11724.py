#연결 요소의 개수

#입력부
import sys
sys.setrecursionlimit(10**9)
n, m = map(int, sys.stdin.readline().split())

#그래프 입력
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

#dfs로 연결된 노드 돌면서 visited 1로 변경
visited = [0 for i in range(n+1)]
def dfs(x):
    if visited[x] != 0:
        return
    else:
        visited[x] = 1
        for i in graph[x]:
            dfs(i)

#dfs 한 번 돌때마다 연결요소 하나 확인. ans +1
ans = 0
for i in range(1,n+1):
    if visited[i] == 0:
        dfs(i)
        ans += 1

print(ans)
