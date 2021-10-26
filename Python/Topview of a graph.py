# A python program to find the Top view of a binary search tree
# Author: Dara Ekanth

# first we have to build binary search tree.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildtree(root, data):
    if root == None:
        root = Node(data)
    elif data < root.data:
        root.left = buildtree(root.left, data)
    elif data > root.data:
        root.right = buildtree(root.right, data)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def topview(root):  # For topview we require queue and hashmap
    queue = []
    queue.append([root, 0])
    hd = {}
    while queue:
        ele, idx = queue.pop(0)
        if idx not in hd and ele:
            hd[idx] = ele.data
        if ele:
            queue.append([ele.left, idx - 1])
            queue.append([ele.right, idx + 1])
    hd = dict(sorted(hd.items(), key=lambda x: x[1]))
    print(*list(hd.values()), end=" ")


if __name__ == "__main__":
    a = list(map(int, input("Enter a list (space-separated): ").split()))
    root = None
    for i in a:
        root = buildtree(root, i)
    topview(root)
