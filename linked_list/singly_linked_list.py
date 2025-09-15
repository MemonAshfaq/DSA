from typing import List, Dict, Optional

class Node:
    def __init__(self, val:int = 0, next:Optional['Node'] = None):
        self.val:int = val
        self.next:Node = next

class LL:
    def __init__(self):
        self.head = None

    def build_ll(self, arr:List[int]):
        if not arr:
            return
        cur = self.head = Node(arr[0])
        for val in arr[1:]:
            cur.next = Node(val)
            cur = cur.next

    def print_ll(self):
        cur = self.head
        while cur:
            print ("{} -> ".format(cur.val), end="")
            cur = cur.next
        print ()

    def insert_after(self,node:Node, val:int = 0) -> None:
        if node != None:
            new = Node(val)
            new.next = node.next
            node.next = new

    def delete_after(self, node:Node) -> None:
        if node and node.next:
            node.next = node.next.next

    def reverse_ll(self):
        prev = None
        cur = self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def build_cycle_ll(self, array:List[int], pos:int):
        self.head = Node(array[0])
        cur = self.head
        count = 0
        note = self.head if pos == 0 else None
        for a in array[1:]:
            count += 1
            cur.next = Node(a)
            cur = cur.next
            if count == pos:
                note = cur
        
        if note:
            cur.next = note

    def print_llc(self) -> None:
        cur = self.head
        output = ""
        seen = set()
        while cur:
            if cur in seen:
                break
            output += "{} -> ".format(cur.val)
            seen.add(cur)
            cur = cur.next
        print (output)

    def detect_cycle_bf(self):
        cur = self.head
        cycle = False
        s = set()
        while cur:
            if cur in s:
                return True
            s.add(cur)
            cur = cur.next
        return False

    def detect_cycle_op(self) -> bool:
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def merge_two_sorted_lists(self,ll1:'LL', ll2:'LL'):
        dummy = Node(0)
        cur = dummy
        l1 = ll1.head
        l2 = ll2.head

        while (l1 and l2):
            if (l1.val <= l2.val):
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        cur.next = l1 if l1 else l2

        self.head = dummy.next #head

    def find_nth_from_end(self, n:int) -> int:
        dummy = Node(0,self.head)
        l = r = dummy

        for _ in range(n):
            r = r.next

        while r.next:
            r = r.next
            l = l.next

        return l.next.val

    def remove_nth_from_end(self, n:int) -> int:
        dummy = Node(0,self.head)
        l = r = dummy

        for _ in range(n):
            r = r.next

        while r.next:
            r = r.next
            l = l.next

        l.next = l.next.next

        return dummy.next
    
# ---------------------------------------------------------
# Minimal call-based tests for LL methods 
# ---------------------------------------------------------
def show(title, ll_obj):
    print(f"{title}: ", end="")
    ll_obj.print_ll()

def to_list(head):
    out, seen = [], set()
    cur = head
    while cur and cur not in seen:
        seen.add(cur)
        out.append(cur.val)
        cur = cur.next
    return out

print("=== build_ll / print_ll ===")
ll = LL()
ll.build_ll([1, 2, 3])
show("Initial", ll)                       # 1 ->2 ->3 ->

print("\n=== insert_after ===")
# Insert 4 after node with value 2
node2 = ll.head.next
ll.insert_after(node2, 4)
show("After insert 4 after 2", ll)        # 1 ->2 ->4 ->3 ->
# Insert with node=None (should be no-op)
ll.insert_after(None, 99)
show("Insert with None (no-op)", ll)      # unchanged

print("\n=== delete_after ===")
# Delete node after head (deletes 2)
ll.delete_after(ll.head)
show("After delete_after(head)", ll)      # 1 ->4 ->3 ->
# Delete when next is None (no-op)
tail = ll.head
while tail.next:
    tail = tail.next
ll.delete_after(tail)                     # deleting after tail does nothing
show("Delete after tail (no-op)", ll)     # unchanged

print("\n=== reverse_ll ===")
ll_rev = LL()
ll_rev.build_ll([10, 20, 30, 40])
show("Before reverse", ll_rev)            # 10 ->20 ->30 ->40 ->
ll_rev.reverse_ll()
show("After reverse", ll_rev)             # 40 ->30 ->20 ->10 ->
# Reverse single-node
ll_one = LL()
ll_one.build_ll([99])
show("Single before reverse", ll_one)     # 99 ->
ll_one.reverse_ll()
show("Single after reverse", ll_one)      # 99 ->

print("\n=== build_cycle_ll / print_llc / detect_cycle ===")
llc = LL()
llc.build_cycle_ll([5, 6, 7, 8, 9], pos=2)  # cycle back to value 7
print("Cycle print (stops when repeats): ", end="")
llc.print_llc()
print("detect_cycle_bf:", llc.detect_cycle_bf())   # True
print("detect_cycle_op:", llc.detect_cycle_op())   # True

print("\n=== merge_two_sorted_lists ===")
ll1 = LL(); ll1.build_ll([1, 4, 8, 9])
ll2 = LL(); ll2.build_ll([2, 3, 5, 6, 10])
ll_merged = LL()
ll_merged.merge_two_sorted_lists(ll1, ll2)
show("Merged", ll_merged)                 # 1 ->2 ->3 ->4 ->5 ->6 ->8 ->9 ->10 ->
print("Merged as list:", to_list(ll_merged.head))

print("\n=== find_nth_from_end ===")
# List: 1,2,3,4,5
llN = LL(); llN.build_ll([1, 2, 3, 4, 5])
print("n=1 (tail):", llN.find_nth_from_end(1))     # 5
print("n=5 (head):", llN.find_nth_from_end(5))     # 1
print("n=3 (middle):", llN.find_nth_from_end(3))   # 3

print("\n=== remove_nth_from_end ===")
# Remove head (n = len)
llR = LL(); llR.build_ll([11, 22, 33, 44, 55])
show("Before remove n=len", llR)          # 11 ->22 ->33 ->44 ->55 ->
llR.head = llR.remove_nth_from_end(5)
show("After remove head", llR)            # 22 ->33 ->44 ->55 ->
# Remove tail (n=1)
llR.head = llR.remove_nth_from_end(1)
show("After remove tail", llR)            # 22 ->33 ->44 ->
# Remove middle (n=2 -> remove 44’s predecessor = 33)
llR.head = llR.remove_nth_from_end(2)
show("After remove middle (n=2)", llR)    # 22 ->44 ->
