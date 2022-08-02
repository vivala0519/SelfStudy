import sys


def preorder(inorder_s, inorder_e, postorder_s, postorder_e):
    if (inorder_s > inorder_e) or (postorder_s > postorder_e):
        return

    p = postorder[postorder_e]
    print(p, end=' ')

    left = pos[p] - inorder_s
    right = inorder_e - pos[p]

    preorder(inorder_s, inorder_s + left - 1, postorder_s, postorder_s + left - 1)
    preorder(inorder_e - right + 1, inorder_e, postorder_e - right, postorder_e - 1)


sys.setrecursionlimit(10 ** 9)
n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
pos = [0] * (n + 1)

for i in range(n):
    pos[inorder[i]] = i

preorder(0, n - 1, 0, n - 1)

