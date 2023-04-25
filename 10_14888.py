# 연산자 끼워넣기

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

#문제 기준 최대, 최소값 범위 역으로 넣음
hi = -10**10
lo = 10**10

def dfs (cnt, sum, add, sub, mul, div):
    global hi, lo

    # 연산기호 다 썼으면 sum값 최대 최솟값 비교
    if cnt == n:
        hi = max(sum, hi)
        lo = min(sum, lo)
        return

    # 재귀함수 계속 호출하며 add로 시작하는 dfs 다끝나면 sub로 시작하는 dfs ......
    if add:
        dfs(cnt + 1, sum + a[cnt], add-1, sub, mul, div)
    if sub:
        dfs(cnt + 1, sum - a[cnt], add, sub-1, mul, div)
    if mul:
        dfs(cnt + 1, sum * a[cnt], add, sub, mul-1, div)
    if div:
        dfs(cnt + 1, int(sum / a[cnt]), add, sub, mul, div-1)


dfs (1, a[0], add, sub, mul, div)

print(hi)
print(lo)