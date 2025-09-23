def is_num_palindrome(n:int):
    if n<0:
        return False

    if n!=0 and n%10==0:
        return False
    
    rev = 0
    while n > rev:
        rev = rev*10 + n%10
        n //=10
    
    return rev == n or rev//10 == n

def longest_common_prefix(strlist:list[str]):
    strlist.sort()
    first = strlist[0]
    last = strlist[-1]

    i = 0
    while(i<len(first) and i<len(last) and first[i]==last[i]):
        i+=1
    
    return strlist[0][:i]

#nums = [0,0,1,1,1,2,2,3,3,4]
def remove_duplicates_from_sorted_arr(arr:list[int]):
    wp = 0

    for rp in range(1, len(arr)):
        if arr[rp] != arr[wp]:
            wp+=1
            arr[wp] = arr[rp]
    
    return wp + 1 if arr else 0

"""
Problem: Roman to Integer (LeetCode 13)

Roman numerals are represented by seven symbols:
I=1, V=5, X=10, L=50, C=100, D=500, M=1000.

Rules:
- Normally add values left to right.
- Subtractive cases:
    I before V or X → 4, 9
    X before L or C → 40, 90
    C before D or M → 400, 900

Input:  s = "MCMXCIV"
Output: 1994
"""


def roman_to_int(s:str) -> int:
    
    rtoi = {
    'I':1,
    'IV':4,
    'V':5,
    'IX':9,
    'X':10,
    'XL':40,
    'L':50,
    'XC':90,
    'C':100,
    'CD':400,
    'D':500,
    'CM':900,
    'M':1000
    }

    i = 0
    total = 0
    length = len(s)
    while (i<length):
        if (i+1<length) and s[i:i+2] in rtoi:
            total += rtoi[s[i:i+2]]
            i+=2
        else:
            total += rtoi[s[i]]
            i+=1
    
    return total

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    """Convert Python list → Linked list"""
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def merge_two_sorted_ll_rec(list1, list2):
    if not list1 and not list2: return None
    if not list1: return list2
    if not list2: return list1

    if list1.val < list2.val:
        list1.next = merge_two_sorted_ll_rec(list1.next,list2)
        return list1
    else:
        list2.next= merge_two_sorted_ll_rec(list1, list2.next)
        return list2

# Tree:
#         1
#        / \
#       2   3
#      / \
#     4   5
#
# Start: diameter = 0
#
# dfs(1):
#   dfs(2):
#     dfs(4):
#       dfs(None) → 0
#       dfs(None) → 0
#       dia = max(0, 0+0) = 0
#       return height = 1
#     left = 1
#
#     dfs(5):
#       dfs(None) → 0
#       dfs(None) → 0
#       dia = max(0, 0+0) = 0
#       return height = 1
#     right = 1
#
#     dia = max(0, 1+1) = 2
#     return height = 1 + max(1,1) = 2
#   left = 2
#
#   dfs(3):
#     dfs(None) → 0
#     dfs(None) → 0
#     dia = max(2, 0+0) = 2
#     return height = 1
#   right = 1
#
#   dia = max(2, 2+1) = 3
#   return height = 1 + max(2,1) = 3
#
# Final Answer: diameter = 3

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    """Builds a binary tree from a level-order list (None = empty)."""
    if not values:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if node:
            # left child
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
            q.append(node.left)
            i += 1
            # right child
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
            q.append(node.right)
            i += 1
    return root

def max_dia_bin_tree(root:TreeNode):
    dia = 0
    def dfs(node):
        nonlocal dia
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        dia = max(dia,left+right)#longest path through this node
        return 1+max(left,right) #height of this node (+1 for including node itself)
    
    dfs(root)
    return dia

def find_majority(nums: list) -> int:
    # Approach 1 (simple but slower):
    # Sort and return nums[n//2]
    #
    # Approach 2 (hashmap):
    # Count frequencies and return element with freq > n//2
    #
    # Approach 3 (optimal):
    # Boyer–Moore Voting Algorithm
    
    cand = None
    count = 0

    for n in nums:
        if count == 0:
            cand = n   # reset candidate
        if cand == n:
            count += 1
        else:
            count -= 1

    return cand

def plus_one_bf(nlist):
    num = nlist[0]
    for n in nlist[1:]:
        num = num*10 + n
    num += 1
    return [int(d) for d in str(num)]

def plus_one_op(nlist):
    # We only propagate carry while we see 9’s.
    # As soon as one digit increments safely, we stop.
    l = len(nlist)

    for i in range(l-1,-1,-1):
        if nlist[i] == 9:
            nlist[i] = 0
        else:
            nlist[i] += 1
            return nlist
        
    return [1] + nlist

#Input:  numRows = 5
#Output:
#[
# [1],
# [1,1],
# [1,2,1],
# [1,3,3,1],
# [1,4,6,4,1]
#]

def pascal_triangle(num_rows):
    triangle = []
    for i in range(num_rows):
        row = [1]*(i+1)
        for j in range(1,i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

class Person:
    def __init__(self, name:str, wants:bool):
        self.name = name
        self.wants = wants

class Apt:
    def __init__(self, num:int, rooms:int):
        self.num = num
        self.rooms = rooms

def allocate_units(apts:list[Apt], people:list[Person]) -> dict[int:list[Person]],list[str]:
    apt_map = {}
    for apt in apts:
        apt_map[apt.num] = []
    
    unassigned = []

    for person in people:
        assigned = False
        for apt in apts:
            if person.wants:
                if len(apt_map[apt.num]) < apt.rooms:
                    apt_map[apt.num].append(person.name)
                    assigned = True
                    break
            else:
                if apt.rooms == 1:
                    if len(apt_map[apt.num]) == 0:
                        apt_map[apt.num].append(person.name)
                        assigned = True
                        break
        if not assigned:
            unassigned.append(person.name)

    return apt_map, unassigned

apts = [Apt(101, 2), Apt(102, 1)]
people = [Person("Alice", True), Person("Bob", True), Person("Cara", False)]
expected = {
    101: ["Alice", "Bob"],   # fills both slots
    102: ["Cara"]
}

apt_map = allocate_units(apts, people)

print (apt_map)