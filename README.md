# Adaptive Graph Engine

A lightweight Python graph engine for modelling directed graphs, dependencies, relationships and weighted paths.

## Features

- Directed graph representation
- Nodes and edges
- Edge weights
- Relationship metadata
- Neighbour lookup
- Predecessor and successor lookup
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Dijkstra shortest weighted path
- Directed cycle detection
- Topological sorting

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

## Example Use Cases

Adaptive Graph Engine can be used as a foundation for:

- Dependency graphs
- Data lineage
- Provenance graphs
- Workflow dependencies
- Knowledge graph infrastructure
- Relationship-based systems

## Requirements

Python 3.11 or later.

## Version

Current release: **0.2.0**

## Author

Yassine Chaachaa

## License

MIT