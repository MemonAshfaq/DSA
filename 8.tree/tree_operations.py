from typing import Optional, List
from collections import deque

class Node:
    def __init__(self, val:int, left:'Optional[Node]'=None, right:'Optional[Node]'=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)

#---------------------------------------------------------
# BFS
#---------------------------------------------------------
def print_tree_bfs(root:Node) -> None:
    # add root to queue
    q = deque([root])
    while q:
        # pick from front
        node = q.popleft()
        
        # print this node
        print (node, end=" ")
        
        # add left node to queue
        if node.left:
            q.append(node.left)
        # add right node to queue
        if node.right:
            q.append(node.right)
    print ()

def print_levels_bfs(root:Node) -> List[List[int]]:
    q = deque([root])
    out = []
    while q:
        level = []
        for _ in range(len(q)):
            n = q.popleft()
            level.append(n.val)

            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        print (" "* (10 - (len(out))-len(level)),level)
        out.append(level)
    return out

def max_depth_bfs(root:Node) -> int:
    if not root:
        return 0
    
    q = deque([root])
    depth = 0
    while q:
        depth += 1
        for _ in range(len(q)):
            n = q.popleft()
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
    return depth

def build_tree(a:List[int]) -> Optional['Node']:
    # return an empty tree if empty list
    if not a:
        return None
    
    # start with first element as root
    root = Node(a[0])
    
    # put the root to queue
    q = deque([root])

    # 0th node is already root, start with 1st in the loop
    i = 1
    while (i < len(a)):
        # pick the next node in the queue
        cur = q.popleft()

        # the first if statement below is for the sake of symmetry
        if (i < len(a)):
            if a[i] is not None:
                # fill the left
                cur.left = Node(a[i])
                # add it to queue so the left gets processed first
                q.append(cur.left)
            # move to next i
            i+=1

        # check i for range
        if (i < len(a)):
            if a[i] is not None:
                # fill the right node
                cur.right = Node(a[i])
                # add it to queue so it gets processed second
                q.append(cur.right)
            i+=1

    # return the root
    return root

#---------------------------------------------------------
# DFS
#---------------------------------------------------------
def pre_order(root:Node):
    if not root:
        return
    print (root.val, end=" ")
    pre_order(root.left)
    pre_order(root.right)

def in_order(root:Node):
    if not root:
        return
    in_order(root.left)
    print (root.val, end= " ")
    in_order(root.right)

def post_order(root:Node):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print (root.val, end=" ")

def max_depth_dfs(root:Node) -> int:
    if not root:
        return 0
    stack = [(root,1)]

    max_depth = 0
    while stack:
        n,depth = stack.pop()
        max_depth = max(max_depth, depth)

        # push children with incremented depth
        if n.right:
            stack.append((n.right,depth+1))
        if n.left:
            stack.append((n.left,depth+1))

    return max_depth

def validate_bst(root:Node,low = float('-inf'),high = float('inf')) -> bool:
    if not root:
        return True
    
    if not (low < root.val < high):
       return False
     
    return (validate_bst (root.left, low, root.val) and
            validate_bst (root.right, root.val, high))

def validate_symmetric(root:Optional['Node']) -> bool:
    if not root:
        return True
    
    def is_mirror(a:Node, b:Node):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return ((a.val == b.val) and
                is_mirror(a.left, b.right) and
                is_mirror(a.right, b.left))
    
    return is_mirror(root.left, root.right)

def lca_bst(root: Node, p: Node, q: Node) -> Node:
    cur = root
    while cur:
        if p.val > cur.val and q.val > cur.val:
            cur = cur.right
        elif p.val < cur.val and q.val < cur.val:
            cur = cur.left
        else:
            return cur

root = build_tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print_tree_bfs(root)
print_levels_bfs(root)

print ("---------pre-order-dfs------------")
pre_order(root)
print()
print ("---------in-order-dfs------------")
in_order(root)
print()
print ("---------post-order-dfs------------")
post_order(root)
print()
print (max_depth_dfs(root))
print (max_depth_bfs(root))

root = build_tree([4,2,6,1,3,5,7])
in_order(root)
print()
print (validate_bst(root))

root = build_tree([1,2,2,3,4,4,3,5,6,7,8,8,7,6,5])
print (validate_symmetric(root))

root = build_tree([10,5,20,2,7,15,30])
print_levels_bfs(root)
p, q = root.left.left, root.left.right # nodes 2 and 7
print("LCA (BST):", lca_bst(root, p, q).val)  # 5

#What to do next (high-yield problems)
#
#General LCA (non-BST) — works on any binary tree.
#
#Balanced Binary Tree (height-balance check).
#
#Diameter of Binary Tree (longest path).
#
#Path Sum I/II + Binary Tree Maximum Path Sum (classic tree DP).
#
#Invert/Mirror Tree (quick).
#
#Kth Smallest in BST (inorder / iterative stack).
#
#Serialize / Deserialize Binary Tree (BFS with None markers).
#
#(Bonus) Morris Traversal (O(1) space inorder) & Zigzag / Views (left/right/top).