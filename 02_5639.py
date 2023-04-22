#이진 검색 트리

import sys

sys.setrecursionlimit(10 ** 6)
num_list = []
while True:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break


def postorder(first, end):
    # 루트의 자식값이 존재 하지 않는 상황 (터미널 노드)
    if first > end:
        return

    # 루트보다 큰 값이 존재하지 않을 경우를 위함.
    # 모두 왼쪽노드로 보내고, postorder(mid, end) 호출시 first>end 이므로 바로 return
    mid = end + 1

    # first는 root, root보다 큰 값 직전까지가 왼쪽 서브트리
    for i in range(first + 1, end + 1):
        if num_list[first] < num_list[i]:
            mid = i
            break

    #왼쪽 서브트리에서 재귀함수 호출
    postorder(first + 1, mid - 1)
    #오른쪽 서브트리에서 재귀함수 호출
    postorder(mid, end)
    #왼쪽,오른쪽 서브트리 다 끝나면(왼쪽,오른쪽 자식 없으면) 루트 프린트
    print(num_list[first])


postorder(0, len(num_list) - 1)