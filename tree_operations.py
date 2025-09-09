from typing import Optional, List
from collections import deque

class Node:
    def __init__(self, val:int, left:'Optional[Node]'=None, right:'Optional[Node]'=None):
        self.val = val
        self.left = left
        self.right = right

# -------------------------------------------------------------------
# 1) Traversals
# -------------------------------------------------------------------
def preorder(root: Optional[Node]) -> List[int]:
    res = []
    def dfs(n):
        if not n: return
        res.append(n.val)
        dfs(n.left); dfs(n.right)
    dfs(root)
    return res

def inorder(root: Optional[Node]) -> List[int]:
    res = []
    def dfs(n):
        if not n: return
        dfs(n.left); res.append(n.val); dfs(n.right)
    dfs(root)
    return res

def postorder(root: Optional[Node]) -> List[int]:
    res = []
    def dfs(n):
        if not n: return
        dfs(n.left); dfs(n.right); res.append(n.val)
    dfs(root)
    return res

def level_order(root: Optional[Node]) -> List[List[int]]:
    if not root: return []
    q, out = deque([root]), []
    while q:
        level = []
        for _ in range(len(q)):
            n = q.popleft()
            level.append(n.val)
            if n.left:  q.append(n.left)
            if n.right: q.append(n.right)
        out.append(level)
    return out

# -------------------------------------------------------------------
# 2) Height / Max Depth (+ Balanced)
# -------------------------------------------------------------------
def max_depth(root: Optional[Node]) -> int:
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def is_balanced(root: Optional[Node]) -> bool:
    def height(n):
        if not n: return 0
        hl = height(n.left)
        if hl == -1: return -1
        hr = height(n.right)
        if hr == -1: return -1
        if abs(hl - hr) > 1: return -1
        return 1 + max(hl, hr)
    return height(root) != -1

# -------------------------------------------------------------------
# 3) Validate BST
# -------------------------------------------------------------------
def is_valid_bst_range(root: Optional[Node]) -> bool:
    def helper(n, low, high):
        if not n: return True
        if not (low < n.val < high): return False
        return helper(n.left, low, n.val) and helper(n.right, n.val, high)
    return helper(root, float("-inf"), float("inf"))

# -------------------------------------------------------------------
# 4) Lowest Common Ancestor (LCA)
# -------------------------------------------------------------------
def lca_bst(root: Optional[Node], p: Node, q: Node) -> Optional[Node]:
    cur = root
    while cur:
        if p.val < cur.val and q.val < cur.val:
            cur = cur.left
        elif p.val > cur.val and q.val > cur.val:
            cur = cur.right
        else:
            return cur
    return None

def lca_binary_tree(root: Optional[Node], p: Node, q: Node) -> Optional[Node]:
    if not root or root is p or root is q: return root
    L = lca_binary_tree(root.left, p, q)
    R = lca_binary_tree(root.right, p, q)
    if L and R: return root
    return L if L else R

# -------------------------------------------------------------------
# 5) Path Sum (basic)
# -------------------------------------------------------------------
def has_path_sum(root: Optional[Node], target: int) -> bool:
    if not root: return False
    if not root.left and not root.right:
        return root.val == target
    return has_path_sum(root.left, target - root.val) or \
           has_path_sum(root.right, target - root.val)

def path_sum_all(root: Optional[Node], target: int) -> List[List[int]]:
    res, path = [], []
    def dfs(n, rem):
        if not n: return
        path.append(n.val)
        if not n.left and not n.right and rem == n.val:
            res.append(path[:])
        else:
            dfs(n.left, rem - n.val)
            dfs(n.right, rem - n.val)
        path.pop()
    dfs(root, target)
    return res

# -------------------------------------------------------------------
# Helper: build a complete binary tree from list (level order)
# -------------------------------------------------------------------
def build_tree_level(a: List[int]) -> Optional[Node]:
    if not a: return None
    root = Node(a[0]); q = deque([root]); i = 1
    while i < len(a):
        cur = q.popleft()
        if i < len(a):
            cur.left = Node(a[i]); q.append(cur.left); i += 1
        if i < len(a):
            cur.right = Node(a[i]); q.append(cur.right); i += 1
    return root

# -------------------------------------------------------------------
# Minimal Tests
# -------------------------------------------------------------------
if __name__ == "__main__":
    root = build_tree_level([10,5,20,2,7,15,30])

    print("Preorder:", preorder(root))      # [10, 5, 2, 7, 20, 15, 30]
    print("Inorder:", inorder(root))        # [2, 5, 7, 10, 15, 20, 30]
    print("Postorder:", postorder(root))    # [2, 7, 5, 15, 30, 20, 10]
    print("Level Order:", level_order(root))# [[10],[5,20],[2,7,15,30]]

    print("Max Depth:", max_depth(root))    # 3
    print("Balanced?:", is_balanced(root))  # True

    print("Valid BST?:", is_valid_bst_range(root)) # True

    p, q = root.left.left, root.left.right # nodes 2 and 7
    print("LCA (BST):", lca_bst(root, p, q).val)  # 5
    print("LCA (BT):", lca_binary_tree(root, p, q).val) # 5

    print("Has Path Sum 22?:", has_path_sum(root, 22)) # True (10->5->7)
    print("All Path Sums 22:", path_sum_all(root, 22)) # [[10,5,7]]
