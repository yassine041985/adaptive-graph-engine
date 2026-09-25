## Adaptive Graph Engine

Adaptive Graph Engine is a Python graph engine for modelling and analysing directed dependency networks. It provides path discovery, BFS/DFS traversal, weighted shortest paths, cycle detection, topological ordering, structural graph analysis, persistence, and change tracking across evolving graph states.

## Features

- Directed graph representation
- Nodes and edges
- Parallel edges
- Edge weights
- Node metadata
- Relationship metadata
- Neighbour lookup
- Predecessor and successor lookup
- Node and edge counts
- In-degree, out-degree and total degree
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Dijkstra shortest weighted path
- Directed cycle detection
- Topological sorting
- Connected components
- Local neighbourhood analysis
- Dictionary serialization and restoration
- JSON save and load
- Graph state comparison
- Node and edge change detection
- Edge weight change detection

## Installation

```bash
pip install adaptive-graph-engine
```

## Basic Usage

```python
from adaptive_graph_engine import Graph

graph = Graph()

graph.add_edge(
    "salesforce",
    "customer_raw",
    metadata={"relationship": "INGESTS_TO"}
)

graph.add_edge(
    "customer_raw",
    "customer_clean",
    metadata={"relationship": "TRANSFORMS_TO"}
)

print(graph.get_neighbors("salesforce"))
```

Output:

```text
['customer_raw']
```

## Graph Algorithms

Algorithms are available from `adaptive_graph_engine.algorithms`.

### Breadth-First Search

Find a path with the fewest hops.

```python
from adaptive_graph_engine.algorithms import find_shortest_path

path = find_shortest_path(
    graph,
    "salesforce",
    "customer_clean"
)
```

### Depth-First Search

Explore a graph using depth-first traversal.

```python
from adaptive_graph_engine.algorithms import find_depth_first

path = find_depth_first(
    graph,
    "salesforce",
    "customer_clean"
)
```

### Dijkstra

Find the lowest-cost path using edge weights.

```python
from adaptive_graph_engine.algorithms import dijkstra

result = dijkstra(
    graph,
    "salesforce",
    "customer_clean"
)
```

Dijkstra returns the path and its total cost.

### Cycle Detection

```python
from adaptive_graph_engine.algorithms import has_cycle

contains_cycle = has_cycle(graph)
```

### Topological Sort

```python
from adaptive_graph_engine.algorithms import topological_sort

order = topological_sort(graph)
```

Topological sorting returns `None` when the directed graph contains a cycle.

### Connected Components

Find groups of connected nodes. Direction is ignored when determining component membership.

```python
from adaptive_graph_engine.algorithms import get_connected_components

components = get_connected_components(graph)
```

### Local Neighbourhood

Inspect the graph surrounding a node up to a specified depth.

```python
from adaptive_graph_engine.algorithms import get_neighborhood

neighborhood = get_neighborhood(
    graph,
    "customer_raw",
    depth=2
)
```

## Graph Statistics

The graph provides basic structural measurements.

```python
graph.number_of_nodes()
graph.number_of_edges()

graph.in_degree("customer_raw")
graph.out_degree("customer_raw")
graph.degree("customer_raw")
```

Parallel edges are counted separately.

## Graph Persistence

Graphs can be converted to dictionaries and reconstructed later.

```python
data = graph.to_dictionary()

restored_graph = Graph.from_dictionary(data)
```

Graph state can also be saved to and loaded from JSON.

```python
from adaptive_graph_engine.io import save_json, load_json

save_json(
    graph,
    "graph.json"
)

restored_graph = load_json(
    "graph.json"
)
```

Serialization preserves node metadata, edge weights, relationship metadata and parallel edges.

## Graph Change Tracking

Adaptive Graph Engine can compare two graph states and report structural changes.

```python
from adaptive_graph_engine import Graph
from adaptive_graph_engine.changes import compare_graphs

old_graph = Graph()

old_graph.add_edge(
    "customer_clean",
    "revenue_model",
    weight=2,
    metadata={
        "relationship": "FEEDS"
    }
)

new_graph = Graph()

new_graph.add_edge(
    "customer_clean",
    "revenue_model",
    weight=8,
    metadata={
        "relationship": "FEEDS"
    }
)

changes = compare_graphs(
    old_graph,
    new_graph
)

print(changes)
```

Graph comparison can detect:

- Nodes added
- Nodes removed
- Edges added
- Edges removed
- Edge weight changes
- Changes across parallel relationships

Change tracking provides a foundation for systems that need to observe how dependency and relationship structures evolve over time.

## Example Use Cases

Adaptive Graph Engine can be used as a foundation for:

- Dependency graphs
- Data lineage
- Provenance graphs
- Workflow dependencies
- Knowledge graph infrastructure
- Relationship-aware systems
- Graph change monitoring
- Evolving dependency networks

## Requirements

Python 3.11 or later.

## Version

Current release: **0.3.0**

## Author

Yassine Chaachaa

## License

MIT