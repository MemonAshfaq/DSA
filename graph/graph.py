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
    def __init__(self, nodes:list[Node]=[]):
        self.nodes = nodes

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def add_edge(self, src:Node, dst_list:list[Node]):
        self.add_node(src)
        for dst in dst_list:
            self.add_node(dst)
            if dst not in src.neighbors:
                src.neighbors.append(dst)

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

        for node in self.nodes:
            if node not in visited:
                print (f"starting BFS traversal at {node.val}")
                q = deque([node])
                while q:
                    n = q.popleft()
                    if n in visited:
                        continue
                    visited.add(n)
                    print (f"Node {n.val}: {[neighbor.val for neighbor in n.neighbors]}")
                    for neighbor in n.neighbors:
                        q.append(neighbor)

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
