class Graph:
    def __init__(self):
        self.adj = {}

    def add_node(self, node):               # Add a node if it doesn't exist
        if node not in self.adj:
            self.adj[node] = {}
    
    def add_edge(self, src, dest, weight):  # Add an edge with a source, destination, and weight
        self.add_node(src)
        self.add_node(dest)
        self.adj[src][dest] = weight

    def remove_node(self, node):            # Remove a node and all associated edges
        if node in self.adj:
            del self.adj[node]
        for neighbors in self.adj.values():
            neighbors.pop(node, None)

    def remove_edge(self, src, dest):       # Remove an edge from source to destination if it exists
        if src in self.adj and dest in self.adj[src]:
            del self.adj[src][dest]

    def __str__(self):
        return str(self.adj)