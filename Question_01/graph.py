class GraphAdjList:
    def __init__(self, num_of_nodes, startNode = 0):
        self.m_num_of_nodes = num_of_nodes
        self.m_graph = []
        self.startNode = startNode


    def add_edge(self, node1, node2, weight):
        self.m_graph.append([node1 - self.startNode, node2 - self.startNode, weight])


    # Finds the root node of a subtree containing node `i`
    def find_subtree(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_subtree(parent, parent[i])


    # Connects subtrees containing nodes `x` and `y`
    def connect_subtrees(self, parent, subtree_sizes, x, y):
        xroot = self.find_subtree(parent, x)
        yroot = self.find_subtree(parent, y)
        if subtree_sizes[xroot] < subtree_sizes[yroot]:
            parent[xroot] = yroot
        elif subtree_sizes[xroot] > subtree_sizes[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            subtree_sizes[xroot] += 1


    def kruskals_mst(self):
        # Resulting tree
        result = []
        # Iterator
        i = 0
        # Number of edges in MST
        e = 0
        # Sort edges by their weight
        self.m_graph = sorted(self.m_graph, key=lambda item: item[2])
        # Auxiliary arrays
        parent = []
        subtree_sizes = []

        # Initialize `parent` and `subtree_sizes` arrays
        for node in range(self.m_num_of_nodes):
            parent.append(node)
            subtree_sizes.append(0)
        # Important property of MSTs
        # number of egdes in a MST is 
        # equal to (m_num_of_nodes - 1)
        while e < (self.m_num_of_nodes - 1):
            # Pick an edge with the minimal weight
            node1, node2, weight = self.m_graph[i]
            i = i + 1
            x = self.find_subtree(parent, node1)
            y = self.find_subtree(parent, node2)
            if x != y:
                e = e + 1
                result.append([node1, node2, weight])
                self.connect_subtrees(parent, subtree_sizes, x, y)
       # Print the resulting MST
        for node1, node2, weight in result:
           print("%d ---> %d: %d" % (node1 + self.startNode, node2 + self.startNode, weight))


class GraphAdjMatrix:
    def __init__(self, num_of_nodes, startNode = 0):
        #Infinity for defining no path
        self.INF = float('inf')
        #Veortex Length
        self.V = num_of_nodes
        self.parent = [i for i in range(self.V)]
        self.graph = []
        for i in range(self.V):
            self.graph.append([self.INF] * self.V)
        self.startNode = startNode
    

    def add_edge(self, node1, node2, weight):
        self.graph[node1 - self.startNode][node2 - self.startNode] = weight
        self.graph[node2 - self.startNode][node1 - self.startNode] = weight


    # Find set of vertex i
    def find(self, i):
        while self.parent[i] != i:
            i = self.parent[i]
        return i


    # Does union of i and j. It returns
    # false if i and j are already in same
    # set.
    def union(self, i, j):
        a = self.find(i)
        b = self.find(j)
        self.parent[a] = b


    # Finds MST using Kruskal's algorithm
    def kruskals_mst(self):
        mincost = 0 # Cost of min MST
        # Initialize sets of disjoint sets
        for i in range(self.V):
            self.parent[i] = i
        # Include minimum weight edges one by one
        edge_count = 0
        while edge_count < self.V - 1:
            min = self.INF
            a = -1
            b = -1
            for i in range(self.V):
                for j in range(self.V):
                    if self.find(i) != self.find(j) and self.graph[i][j] < min:
                        min = self.graph[i][j]
                        a = i
                        b = j
            self.union(a, b)
            print("%d ---> %d: %d" % (a + self.startNode, b + self.startNode, min))
            edge_count += 1
            mincost += min
