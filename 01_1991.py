#트리순회

import sys
n = int(sys.stdin.readline())
tree = {}

for i in range(n):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]

#전위순회 : 루트->왼쪽자식->오른쪽자식
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

#중위순회 : 왼쪽자식->중위->오른쪽자식
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

#후위순회 : 왼쪽자식->오른쪽자식->루트
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')