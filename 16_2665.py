#미로 만들기

#입력부
import sys
from collections import deque
n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().strip())) for i in range(n)]

#bfs로 탐색
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def bfs ():
    q = deque([(0,0)])
    #visited 배열, 검은 방을 흰 방으로 바꾼 횟수 + 방문한적이 있으면 재방문X 확인 용도
    visited = [[-1] * n for i in range(n)]
    visited[0][0] = 0

    while q:
        #흰방 들어가면 deque에 appendleft로 추가하여 먼저 탐색
        #검은방 들어가야하면 deque에 append로 추가하여 나중에 탐색
        x,y = q.popleft()
        print(visited)
        #최종 목적지 도착하면 변경횟수 출력
        if x == n - 1 and y == n - 1:
            return visited[x][y]

        #4방향 BFS로 탐색
        for i in range(4):
            loc_x = x + dx[i]
            loc_y = y + dy[i]

            #n의 범위안에 있고, 방문한적이 없으면 이동하여 visited에 변경횟수 넣어줌
            #변경횟수가 적은 좌표가 deque의 왼쪽에 들어가기때문에, 변경횟수 적은 좌표기준으로 먼저 검토 및 방문함
            if 0<=loc_x<n and 0<=loc_y<n and visited[loc_x][loc_y] == -1:
                if a[loc_x][loc_y] == 1:
                    visited[loc_x][loc_y] = visited[x][y]
                    q.appendleft((loc_x,loc_y))
                else:
                    visited[loc_x][loc_y] = visited[x][y] + 1
                    q.append((loc_x,loc_y))

print(bfs())