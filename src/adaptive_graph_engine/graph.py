class Graph:

    def __init__(self):
        # Node storage
        self.node = {}

        # Edge storage
        self.edge = {}

    def add_node(self, node, **metadata):
        """Add a node to the graph with optional metadata."""
        self.node[node] = metadata

    def add_edge(self, source, target, weight=1, metadata=None):
        """Add a directed edge with weight and relationship metadata."""

        if metadata is None:
            metadata = {}

        # Automatically create nodes if they do not already exist
        if source not in self.node:
            self.add_node(source)

        if target not in self.node:
            self.add_node(target)

        edge_data = {
            "target": target,
            "weight": weight,
            "metadata": metadata
        }

        if source in self.edge:
            self.edge[source].append(edge_data)
        else:
            self.edge[source] = [edge_data]

    def get_neighbors(self, node):
        """Return nodes directly reachable from node."""

        neighbors = []

        for edge in self.edge.get(node, []):
            neighbors.append(edge["target"])

        return neighbors

    def get_successors(self, node):
        """Return outgoing neighbours of node."""
        return self.get_neighbors(node)

    def get_predecessors(self, node):
        """Return nodes that have an edge pointing to node."""

        predecessors = []

        for source, edges in self.edge.items():
            for edge in edges:
                if edge["target"] == node:
                    predecessors.append(source)

        return predecessors

    def get_edges(self, node=None):
        """Return edges for one node or all edges."""

        if node is not None:
            return self.edge.get(node, [])

        return self.edge

    def get_weighted_neighbors(self, node):
        """Return neighbours together with their edge weights."""

        weighted_neighbors = []

        for edge in self.edge.get(node, []):
            weighted_neighbors.append(
                (edge["target"], edge["weight"])
            )

        return weighted_neighbors

    def get_relationships(self, node):
        """Return relationship metadata for outgoing edges."""

        relationships = []

        for edge in self.edge.get(node, []):
            relationships.append(
                {
                    "target": edge["target"],
                    "metadata": edge["metadata"]
                }
            )

        return relationships
