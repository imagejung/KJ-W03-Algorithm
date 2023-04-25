# 트리의 부모 찾기

import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

# 그래프(트리) 입력 받기, 양방향 연결 정보 저장
graph = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문된 노드면 부모값 저장됨. 1부터(루트) 부터 쭉 내려오므
visited = [0]*(n+1)

# 부모 노드 탐색
def dfs(s):
    # 현재 노드와 연결된 노드 확인
    for i in graph[s]:
        # 연결된 노드의 부모x
        if visited[i] == 0:
            # 연결된 노드의 부모는 현재 노드
            visited[i] = s
            #연결된 노드 기준으로 DFS 재진행
            dfs(i)

# 1번 노트부터 탐색 시작(DFS)
dfs(1)

# 2번 노드부터 부모노드 출력
for x in range(2, n+1):
    print(visited[x])



