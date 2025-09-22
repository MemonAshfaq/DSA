from typing import Optional, List
from collections import deque

_passed = 0
_total = 0

def CHECK (msg:str, cond:bool) -> None:
    global _passed
    global _total
    _total += 1
    if cond : _passed += 1
    print ("[{}] {}".format("PASS" if cond else "FAIL", msg))

class Queue:
    def __init__(self, c:int):
        self.c = c
        self.q = [0]*c
        self.size = 0
        self.front = 0
        self.rear = -1

    def enqueue(self, val:int) -> None:
        if self.size >= self.c:
            print ("Queue Full")
            return
        #print ("Enqueue: {}".format(val))
        self.rear = (self.rear + 1) % self.c
        self.q[self.rear] = val
        self.size += 1
        
    def dequeue(self) -> int:
        if self.size == 0:
            print ("Queue Empty")
            return
        val = self.q[self.front]
        self.front = (self.front + 1) % self.c
        self.size -= 1
        #print ("Dequeue: {}".format(val))
        return val

    def empty(self) -> bool:
        return self.size == 0
    
    def printq(self) -> None:
        if self.empty():
            return print ("Queue Empty")
        i = self.front
        res = []
        for _ in range(self.size):
            res.append(self.q[i])
            i = (i+1) % self.c
        #print ("Q: {}".format(res))

def _demo_queue():
    # Create a queue of capacity 5
    q = Queue(5)

    # Enqueues
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.printq()   # expect [10, 20, 30, 40, 50]

    # Queue full case
    q.enqueue(60)   # should print "Queue Full"

    # Dequeues
    CHECK("Dequeue returns 10", q.dequeue() == 10)
    CHECK("Dequeue returns 20", q.dequeue() == 20)
    q.printq()   # expect [30, 40, 50]

    # Wrap-around test
    q.enqueue(60)
    q.enqueue(70)
    q.printq()   # expect [30, 40, 50, 60, 70]

    # More dequeues
    CHECK("Dequeue returns 30", q.dequeue() == 30)
    CHECK("Dequeue returns 40", q.dequeue() == 40)
    q.printq()   # expect [50, 60, 70]

    # Emptying queue
    q.dequeue()
    q.dequeue()
    q.dequeue()
    CHECK("Queue should be empty", q.empty() == True)
    q.printq()   # expect "Queue Empty"

    # Extra dequeue on empty
    q.dequeue()  # should print "Queue Empty"

class QueueS:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def push(self, val:int):
        self.s1.append(val)
    
    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        return not (self.s1 or self.s2)

def _demo_queue_stack():
    q = QueueS()
    q.push(1)
    q.push(2)
    CHECK("Peek front", q.peek() == 1)   # front is 1
    CHECK("Pop returns 1", q.pop() == 1)
    CHECK("Queue not empty", q.empty() == False)
    CHECK("Pop returns 2", q.pop() == 2)
    CHECK("Queue empty now", q.empty() == True)    
    
def _summarize():
    global _passed
    global _total
    print ("------------------------------------------------------")
    print ("PASS:  {}".format(_passed))
    print ("TOTAL: {}".format(_total))
    print ("------------------------------------------------------")

if __name__ == "__main__":
    _demo_queue()
    _demo_queue_stack()
    _summarize()