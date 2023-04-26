# 최소비용 구하기

import sys
import heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# bus 정보 입력, 나중에 거리기준으로 우선순위 큐 쓰기 위해 거리정보 c를 먼저 넣어줌
bus = [[] for i in range(n+1)]
visited = [sys.maxsize] * (n+1)
for i in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    bus[a].append([c,b])

# 출발지, 도착지
s,e = map(int, sys.stdin.readline().split())

def dijkstra(x):
    # 우선순위 큐 사용
    # start위치 시간 0으로 넣어줌
    q = []
    heapq.heappush(q, (0,x))
    visited[x] = 0

    while q:
        # 노드, 거리 받아오기
        # heapq로 거리가 제일 짧은 곳 가져오기
        d, x = heapq.heappop(q)

        # 다음 방문할 곳의 저장된 최단거리가, 현재 노드에 저장된 최단거리보다 작으면 검토 필요 X
        if visited[x] < d:
            continue

        # 현재 노드에서 있는 버스 for문으로 모두 검토 / 현재 노드까지 최단거리 + bus[]에 저장된 거리
        for next_d, next_x in bus[x]:
            new_d = d + next_d

            # 검토 결과 최단거리 바뀌면 우선순위 힙 push -> 나중에 최소거리 노드 뽑기 위해
            if visited[next_x] > new_d:
                heapq.heappush(q, (new_d, next_x))
                visited[next_x] = new_d

dijkstra(s)
print(visited[e])