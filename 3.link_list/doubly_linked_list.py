from typing import Optional, List, Dict

class Node:
    def __init__(self, prev:Optional['Node'] = None, val:int = 0, next:Optional['Node'] = None):
        self.prev = prev
        self.val = val
        self.next = next

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def build_dll(self,arr:List[int]):
        cur = self.head = Node(None, arr[0], None)

        for x in arr[1:]:
            cur.next = Node(cur, x, None)
            cur = cur.next
        
        self.tail = cur

    def print_dll(self):
        cur = self.head
        output = "->"
        while cur:
            output += " {} ->".format(cur.val)
            cur = cur.next
        print (output)

    def print_dll_rev(self):
        cur = self.tail
        output = "<-"
        while cur:
            output += " {} <-".format(cur.val)
            cur = cur.prev
        print (output)

    def insert_at_front(self, val:int = 0):
        node = Node(None, val, self.head)
        if self.head:
            self.head.prev = node
            self.head = node
        else:
            self.tail = node
            self.head = node

    def insert_at_end(self, val:int = 0):
        node = Node(self.tail, val, None)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.tail = node
            self.head = node

    # 1<-> 2 <-> 3 <-> 4 -> none
    # 1 <-> 2  <-> 3 -> None
    def delete_node(self, node:Node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.next = node.prev = None

dll = DLL()
dll.insert_at_front(5)
dll.insert_at_front(8)
dll.insert_at_end(9)
dll.insert_at_front(8)
dll.print_dll()
dll.print_dll_rev()

dll.build_dll([1,2,3])
dll.print_dll()
dll.print_dll_rev()
dll.insert_at_front(11)
dll.print_dll()
dll.print_dll_rev()
dll.insert_at_end(44)
dll.print_dll()
dll.print_dll_rev()
print ("-------------")
dll.build_dll([2])
dll.print_dll()
dll.delete_node(dll.head)
dll.print_dll()
