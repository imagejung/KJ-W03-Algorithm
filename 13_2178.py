#미로 탐색

from collections import deque

#입력부
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


#BFS, 너비 우선 탐색
def bfs(x, y):
    #한 좌표에서 검토할 네 가지 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    #상하좌우 검사하고, 이동한 경우 이동한 좌표 queue에 저장
    #(다음에 queue 저장한 좌표에서 다시 상하좌우 검사)
    queue = deque()
    queue.append((x, y))

    # 검사한 좌표는 queue에서 pop
    while queue:
        x, y = queue.popleft()

        # 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # boundary 넘어서는 경우 continue
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 지나갈 수 없는 영역이므로 continue
            if graph[nx][ny] == 0:
                continue

            # 지나갈 수 있는 and 한 번도 지나가지 않은 영역 이므로 이동
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


    # BFS 다 끝난 후 graph 맨끝 (n-1, m-1) 값 print
    return graph[n - 1][m - 1]

print(bfs(0, 0))
