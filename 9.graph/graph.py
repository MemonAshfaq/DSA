from collections import deque

class Node:
    def __init__(self, val:int):
        self.val :int = val
        self.neighbors :list[Node] = []

    def __eq__(self, other):
        # a == b -> a.__eq__(b)
        return self is other

    def __str__(self):
        return (f"Node({self.val})")
    
    def __hash__(self):
        # id = address of given object
        # when we say x : list = y : list, both x and y are literally same lists
        # and therefore id(x) = id(y). But if two lists have same content, they
        # will still be independent, and they will have different id.
        return id(self)

class Graph:
    def __init__(self, nodes:list[Node]|None=None):
        self.nodes = nodes or []

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def add_edge(self, src:Node, dst_list:list[Node]):
        self.add_node(src)
        for dst in dst_list:
            self.add_node(dst)
            if dst not in src.neighbors:
                src.neighbors.append(dst)

    def add_undirected_edge(self,x:Node, y:Node):
        self.add_node(x)
        self.add_node(y)
        if x not in y.neighbors:
            y.neighbors.append(x)
        if y not in x.neighbors:
            x.neighbors.append(y)

    def print_graph_dfs(self, node):#call stack
        print (f"--------------DFS--------------")
        print (f"--------- Root Node {node.val} ---------")
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            print(f"Node {node.val}: {[neighbor.val for neighbor in node.neighbors]}")
            for neighbor in node.neighbors:
                dfs(neighbor)
        dfs(node)

    def print_entire_graph_dfs(self):#call stack
        print (f"-----------DFS Entire Graph------------")
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            print(f"Node {node.val}: {[neighbor.val for neighbor in node.neighbors]}")
            for neighbor in node.neighbors:
                dfs(neighbor)
        
        for node in self.nodes:
            if node not in visited:
                print (f"starting DFS traversal at {node.val}")
                dfs(node)

    def print_graph_bfs(self, node):
        print (f"--------------BFS--------------")
        print (f"--------- Root Node {node.val} ---------")
        visited = set()
        q = deque([node])
        while q:
            n = q.popleft()
            if n in visited:
                continue
            visited.add(n)
            print (f"Node {n.val}: {[neighbor.val for neighbor in n.neighbors]}")
            for neighbor in n.neighbors:
                q.append(neighbor)

    def print_entire_graph_bfs(self):
        print (f"-----------BFS Entire Graph------------")
        visited = set()

        def bfs(node):
            print (f"--------------BFS--------------")
            q = deque([node])
            while q:
                n = q.popleft()
                if n in visited:
                    continue
                visited.add(n)
                print (f"Node {n.val}: {[neighbor.val for neighbor in n.neighbors]}")
                for neighbor in n.neighbors:
                    q.append(neighbor)

        for node in self.nodes:
            if node not in visited:
                print (f"starting BFS traversal at {node.val}")
                bfs(node)

    def clone_graph(self, node:Node) -> 'Graph':
        #if empty node
        if not node:
            return None
        
        #dict of orig:cloned
        visited = {}

        def dfs(n:Node) -> Node:
            #reached an already cloned node
            if n in visited:
                return visited[n]
            
            #create a clone with same value
            clone:Node = Node(n.val)

            #note down the cloned node
            visited[n] = clone
 
            for nei in n.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone
        
        dfs(node)  

        return Graph(list(visited.values()))

    def clone_entire_graph(self) -> 'Graph':        
        #dict of orig:cloned
        visited = {}

        def dfs(n:Node) -> Node:
            #reached an already cloned node
            if n in visited:
                return visited[n]
            
            #create a clone with same value
            clone:Node = Node(n.val)

            #note down the cloned node
            visited[n] = clone
 
            for nei in n.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone
        
        for node in self.nodes:
            if node not in visited:
                dfs(node)

        return Graph(list(visited.values()))

    def has_path_bfs(self, src:Node, dst:Node) -> bool:
        if not src or not dst:
            return False
        
        if src is dst:
            return True
        
        visited = set()
        q = deque([src])

        while q:
            n = q.popleft()
            if n in visited:
                continue
            visited.add(n)
            for nei in n.neighbors:
                if dst is nei:
                    return True
                q.append(nei)
        
        return False

    def has_path_dfs(self, src:Node, dst:Node) -> bool:
        if not src or not dst:
            return False

        if src is dst:
            return True
        
        visited = set()

        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            if node is dst:
                return True
            for nei in node.neighbors:
                if dfs(nei):
                    return True
            return False

        return dfs(src)

    def count_connected_components(self) -> int:
        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add (node)

            for neighbor in node.neighbors:
                dfs(neighbor)
        
        count = 0
        for node in self.nodes:
            if node not in visited:
                count += 1
                dfs (node)
        
        return count

    def count_report(self, node) -> int:
        visited = set()

        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            count = 0
            for neighbor in node.neighbors:
                count += 1 #count the neighbor itself
                count += dfs(neighbor) # count all neighbors reachable from that neighbor
            return count
        return dfs(node)

    def has_cycle_undirected(self) -> bool:
        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for nei in node.neighbors:
                if (nei in visited) and (nei is not parent):
                    return True
                elif (nei not in visited) and dfs(nei, node):
                    return True
            
            return False

        for node in self.nodes:
            if node not in visited:
                if dfs(node, None):
                    return True
        return False

    def has_cycle_directed(self):
        visited = set()
        stack = set()

        def dfs(node):
            visited.add(node)
            stack.add(node)

            for nei in node.neighbors:
                if nei not in visited:
                    if dfs(nei):
                        return True
                elif nei in stack:
                    return True
            stack.remove(node)
            return False

        for node in self.nodes:
            if node not in visited:
                if dfs(node):
                    return True        
        return False

    def topo_sort_dfs(self):
        visited = set()
        stack = set()
        order = []

        def dfs(node):
            visited.add(node)
            stack.add(node)

            for nei in node.neighbors:
                if nei not in visited:
                    if dfs(nei):
                        return True
                if nei in stack:
                    return True
            stack.remove(node) #backtrack
            order.append(node)
            return False
        
        for node in self.nodes:
            if node not in visited:
                if dfs(node):
                    return None
        
        return order[::-1]

# ------------- Create Nodes -----------------
a: Node = Node('a')
b: Node = Node('b')
c: Node = Node('c')
d: Node = Node('d')
e: Node = Node('e')
f: Node = Node('f')
g: Node = Node('g')

# ------------- Build Connected Graph -----------------
display = """
       a
     / | \\
   b   c  d
  /    |   \\
 e     f    g
"""
print (display)
graph1 = Graph()
graph1.add_edge(a, [b, c, d])
graph1.add_edge(b, [e])
graph1.add_edge(c, [f])
graph1.add_edge(d, [g])

print("\n======= DFS & BFS: Connected Graph =======")
graph1.print_graph_dfs(a)
graph1.print_graph_bfs(a)

# ------------- Build Graph With Disconnected Nodes -----------------
display = """
       a
     / | \\
   b   c  d
            
 e     f    g <-- disconnected
"""
print(display)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

graph2 = Graph()
graph2.add_edge(a, [b, c, d])
graph2.add_edge(b, [b, a])  # self-loop and back edge
graph2.add_node(e)
graph2.add_node(f)
graph2.add_node(g)

print("\n======= DFS & BFS: Entire Graph With Disconnected Nodes =======")
graph2.print_entire_graph_dfs()
graph2.print_entire_graph_bfs()

# ------------- Clone Connected Graph Only (reachable from 'a') -----------------
clone1 = graph2.clone_graph(a)

print("\n======= CLONE (Only Connected Component From 'a') =======")
print("---- ORIGINAL DFS ----")
graph2.print_graph_dfs(a)

print("---- CLONED DFS ----")
clone1.print_graph_dfs(clone1.nodes[0])

# ------------- Clone Entire Graph (All Components) -----------------
clone2 = graph2.clone_entire_graph()

print("\n======= CLONE (Entire Graph Including Floating Nodes) =======")
print("---- ORIGINAL ENTIRE DFS ----")
graph2.print_entire_graph_dfs()

print("---- CLONED ENTIRE DFS ----")
clone2.print_entire_graph_dfs()

print("\n======= Path Existence Check BFS =======")
"""
Challenge:
You’re given a graph with n nodes (labeled 0 … n-1) and a list of edges.
Determine if there is a path between a given source and destination node.

Input:
n = 6  
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]  

1) source = 0, destination = 5 --> False
2) source = 3, destination = 5 --> True
"""
a = Node('0')
b = Node('1')
c = Node('2')
d = Node('3')
e = Node('4')
f = Node('5')

graph3 = Graph()
graph3.add_undirected_edge(a, b)
graph3.add_undirected_edge(a, c)
graph3.add_undirected_edge(d, f)
graph3.add_undirected_edge(f, e)
graph3.add_undirected_edge(d, e)

check = graph3.has_path_bfs(a,b)
print (check)
check = graph3.has_path_bfs(a,e)
print (check)

print("\n======= Path Existence Check DFS =======")
check = graph3.has_path_dfs(a,b)
print (check)
check = graph3.has_path_dfs(a,e)
print (check)

print("\n======= Count Employee Report DFS =======")
display = """
           a
        /  |  \\
      b    c   d
     / \   |    \\
    e   f  g     h
   /
  i
"""
print (display)

a = Node('0')
b = Node('1')
c = Node('2')
d = Node('3')
e = Node('4')
f = Node('5')
g = Node('6')
h = Node('7')
i = Node('8')

org = Graph()
org.add_edge(a, [b, c, d])
org.add_edge(b, [e,f])
org.add_edge(e, [i])
org.add_edge(c, [g])
org.add_edge(d, [h])
org.print_graph_dfs(a)

print (org.count_report(a))
print (org.count_report(b))

print("\n======= Detect Cycle - Undirected - DFS =======")
display = """
          a
         / |
        b  c
        \  |
          d  
"""
print (display)

a = Node('0')
b = Node('1')
c = Node('2')
d = Node('3')

graph = Graph()
graph.add_undirected_edge(a, b)
graph.add_undirected_edge(b, d)
graph.add_undirected_edge(d, c)
graph.add_undirected_edge(c, a)

print (graph.has_cycle_undirected())

print("\n======= Detect Cycle - Undirected - DFS =======")
display = """
          a
         / |
        b  c
        |  
        d  
"""
print (display)

a = Node('0')
b = Node('1')
c = Node('2')
d = Node('3')

graph = Graph()
graph.add_undirected_edge(a, b)
graph.add_undirected_edge(b, d)
graph.add_undirected_edge(c, a)

print (graph.has_cycle_undirected())

print("\n======= Detect Cycle - Directed - DFS =======")
display = """
        a -> b -> c
        ^          |
        |          |
        <-----------
"""
print (display)

a = Node('0')
b = Node('1')
c = Node('2')

graph = Graph()
graph.add_edge(a, [b])
graph.add_edge(b, [c])
graph.add_edge(c, [a])

print (graph.has_cycle_directed())

display = """
        a -> b -> c
"""
print (display)

a = Node('0')
b = Node('1')
c = Node('2')

graph = Graph()
graph.add_edge(a, [b])
graph.add_edge(b, [c])

print (graph.has_cycle_directed())

print("\n======= Topological Sort - DFS (No Cycle) =======")
display = """
    a → b → c
    a → d → e
"""
print(display)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

graph = Graph()
graph.add_edge(a, [b, d])
graph.add_edge(b, [c])
graph.add_edge(d, [e])

order = graph.topo_sort_dfs()
if order:
    print("Topo order:", [n.val for n in order])
else:
    print("Cycle detected → no topo sort")

print("\n======= Topological Sort - DFS (With Cycle) =======")
display = """
    a → b → c
    ↑       |
    └───────┘
"""
print(display)

a = Node('a')
b = Node('b')
c = Node('c')

graph = Graph()
graph.add_edge(a, [b])
graph.add_edge(b, [c])
graph.add_edge(c, [a])  # cycle here

order = graph.topo_sort_dfs()
if order:
    print("Topo order:", [n.val for n in order])
else:
    print("Cycle detected → no topo sort")
