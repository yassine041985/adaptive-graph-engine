## Adaptive Graph Engine

**Model dependencies. Analyse relationships. Detect what changed.**

Adaptive Graph Engine is an open-source Python graph engine designed for dependency modelling, relationship analysis and change detection across evolving graph structures.

Whether you're working with data pipelines, software components, workflows or knowledge relationships, the engine helps answer three important questions:

1. **How are components connected?**
2. **What depends on what?**
3. **What changed between two versions of the graph?**

The engine combines graph algorithms, structural analysis, persistence and graph-state comparison in a compact Python package.

Its particular focus is on **evolving dependency networks**, where changes to nodes, relationships and edge weights are as important as the graph itself.

Adaptive Graph Engine was implemented from first principles as an independent engineering project. It is not intended to replace mature graph libraries such as NetworkX, but to provide a focused foundation for dependency modelling and structural change detection.

**Current release:** v0.3.0  
**Python:** 3.11+  
**License:** MIT

## Installation

Install the package from PyPI:

```bash
pip install adaptive-graph-engine
```

To install this specific release:

```bash
pip install adaptive-graph-engine==0.3.0
```

[View on PyPI](https://pypi.org/project/adaptive-graph-engine/0.3.0/)

## Quick Start: Detect Changes in a Dependency Graph

Imagine a data pipeline containing two datasets:

`raw_customers → clean_customers`

A new dashboard is introduced that depends on the cleaned dataset.

Rather than manually comparing both dependency structures, Adaptive Graph Engine can identify the differences between their graph representations.

```python
from adaptive_graph_engine import Graph
from adaptive_graph_engine.changes import compare_graphs

# Original dependency graph
old_graph = Graph()

old_graph.add_edge(
    "raw_customers",
    "clean_customers",
    metadata={"relationship": "TRANSFORMS_TO"}
)

# Updated dependency graph
new_graph = Graph()

new_graph.add_edge(
    "raw_customers",
    "clean_customers",
    metadata={"relationship": "TRANSFORMS_TO"}
)

new_graph.add_edge(
    "clean_customers",
    "dashboard",
    metadata={"relationship": "POWERS"}
)

# Compare graph states
changes = compare_graphs(old_graph, new_graph)

print(changes)
```

The comparison identifies:

- **Node added:** `dashboard`
- **Edge added:** `clean_customers → dashboard`

The same approach can be applied to software architectures, data pipelines, ML workflows and other dependency networks.

**Try it yourself:** Add another component, remove a relationship or change an edge weight. Run the comparison again and inspect the results.

The engine compares graph states supplied by your application. It does not automatically discover dependencies or monitor external platforms.

## Why Use Adaptive Graph Engine?

Many systems can be represented as networks of dependencies.

For example:

**Data engineering**

```text
Salesforce
    |
    v
customer_raw
    |
    v
customer_clean
    |
    v
revenue_model
    |
    v
executive_dashboard
```

**Software architecture**

```text
Frontend
    |
    v
API
    |
    v
Application Service
    |
    v
Database
```

**Machine learning**

```text
Dataset
    |
    v
Feature Engineering
    |
    v
ML Model
    |
    v
Prediction Endpoint
```

In each case, dependencies can change as the system evolves.

Adaptive Graph Engine allows developers to represent these structures, analyse their connections, persist graph states and compare versions.

This makes it useful as a building block for applications concerned with dependency modelling, architecture analysis and structural change tracking.

## Features

### Graph Modelling

- Directed graph representation
- Nodes and edges
- Multiple parallel edges between nodes
- Weighted relationships
- Node metadata
- Relationship metadata
- Neighbour lookup
- Predecessor and successor lookup

### Graph Algorithms

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Dijkstra shortest weighted path
- Directed cycle detection
- Topological sorting

### Structural Analysis

- Connected components
- Local neighbourhood analysis
- Node and edge counts
- In-degree, out-degree and total degree

### Persistence

- Dictionary serialization
- Graph restoration from dictionaries
- JSON save and load

### Graph Change Tracking

- Graph-state comparison
- Node addition and removal detection
- Edge addition and removal detection
- Edge-weight change detection
- Weight-change matching across parallel relationships

## Basic Graph Usage

Create a directed graph and define relationships between components.

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

Nodes and relationships can represent datasets, services, applications, workflows or other connected entities.

## Graph Algorithms

Algorithms are available from `adaptive_graph_engine.algorithms`.

### Breadth-First Search (BFS)

Find a path with the fewest hops in an unweighted graph.

```python
from adaptive_graph_engine.algorithms import find_shortest_path

path = find_shortest_path(
    graph,
    "salesforce",
    "customer_clean"
)

print(path)
```

BFS is useful for discovering short dependency paths and understanding how components are connected.

### Depth-First Search (DFS)

Explore a graph through depth-first traversal.

```python
from adaptive_graph_engine.algorithms import find_depth_first

path = find_depth_first(
    graph,
    "salesforce",
    "customer_clean"
)

print(path)
```

DFS can be useful for exploring dependency chains and graph connectivity.

### Dijkstra's Algorithm

Find the lowest-cost path through a weighted graph.

```python
from adaptive_graph_engine.algorithms import dijkstra

result = dijkstra(
    graph,
    "salesforce",
    "customer_clean"
)

print(result)
```

Dijkstra returns the path and its total cost.

It is suitable for graphs with non-negative edge weights, where the lowest total weight is more important than the fewest hops.

### Cycle Detection

Determine whether a directed graph contains a cycle.

```python
from adaptive_graph_engine.algorithms import has_cycle

contains_cycle = has_cycle(graph)

print(contains_cycle)
```

Cycle detection is useful when modelling dependency systems that should not contain circular dependencies.

### Topological Sorting

Determine a valid ordering of nodes based on their dependencies.

```python
from adaptive_graph_engine.algorithms import topological_sort

order = topological_sort(graph)

print(order)
```

Topological sorting returns `None` when the directed graph contains a cycle.

This is useful for dependency ordering, build systems and workflow planning. The meaning of the returned order depends on the direction in which dependencies are modelled.

### Connected Components

Identify groups of connected nodes.

```python
from adaptive_graph_engine.algorithms import get_connected_components

components = get_connected_components(graph)

print(components)
```

For component membership, the algorithm treats directed edges as undirected connections.

This helps identify isolated or connected groups within a larger dependency network.

### Local Neighbourhood Analysis

Inspect the surrounding graph structure up to a specified depth.

```python
from adaptive_graph_engine.algorithms import get_neighborhood

neighborhood = get_neighborhood(
    graph,
    "customer_raw",
    depth=2
)

print(neighborhood)
```

Neighbourhood analysis helps developers inspect the local connectivity around a particular component.

## Graph Statistics

Adaptive Graph Engine provides structural measurements.

```python
graph.number_of_nodes()
graph.number_of_edges()

graph.in_degree("customer_raw")
graph.out_degree("customer_raw")
graph.degree("customer_raw")
```

These operations allow developers to inspect graph size and node connectivity.

Parallel edges are counted separately.

## Graph Persistence

Graphs can be converted to dictionaries and reconstructed later.

### Dictionary Serialization

```python
data = graph.to_dictionary()

restored_graph = Graph.from_dictionary(data)
```

### JSON Persistence

Save a graph:

```python
from adaptive_graph_engine.io import save_json, load_json

save_json(
    graph,
    "graph.json"
)
```

Load a previously saved graph:

```python
restored_graph = load_json(
    "graph.json"
)
```

Serialization preserves node metadata, edge weights, relationship metadata and parallel edges.

Persisted graph states can subsequently be reconstructed and compared.

## Graph Change Tracking

One of the central capabilities of Adaptive Graph Engine v0.3.0 is comparing two graph states.

The engine can identify structural differences between an original graph and an updated graph.

### Example: Detect an Edge-Weight Change

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

In this example, the relationship remains the same, but its weight changes from `2` to `8`.

The comparison detects this change.

### Supported Change Detection

- Nodes added
- Nodes removed
- Logical edges added
- Logical edges removed
- Edge weights changed
- Weight changes involving parallel relationships

### Parallel Relationship Example

A directed graph may contain multiple relationships between the same pair of nodes.

For example:

```text
customer_clean
      |
      | FEEDS (weight 2)
      | FEEDS (weight 5)
      |
      v
revenue_model
```

If the updated graph contains weights `2` and `8`, the unchanged weight `2` can be matched separately from the changed weight `5 → 8`.

This avoids incorrectly reporting the unchanged parallel relationship as modified.

### Current Limitations

Version 0.3.0 focuses on structural changes and edge weights.

- Node metadata-only changes are not reported as a separate change category.
- Arbitrary relationship metadata changes are not fully compared.
- Edge identities are based on source, target and relationship type.
- Adding or removing duplicate parallel edges with identical logical identities is not fully distinguished by edge addition/removal reporting.
- Automatic dependency discovery and external platform monitoring are not included.

These boundaries are important when using graph comparison in production applications.

## Example Use Cases

### 1. Data Pipeline Dependencies

Represent datasets, transformation stages and analytical outputs as nodes and relationships.

Compare two versions of the dependency graph to identify structural changes.

### 2. Software Architecture

Model relationships between APIs, services, databases and other application components.

Explore paths, detect cycles and compare dependency structures between versions.

### 3. Workflow Dependencies

Represent workflow stages and their dependencies.

Use cycle detection and topological sorting to analyse valid execution orderings.

### 4. Machine Learning Pipelines

Model dependencies between datasets, features, trained models and prediction endpoints.

Compare graph snapshots when the ML workflow changes.

### 5. Knowledge Graph Foundations

Use nodes, directed relationships and metadata to represent connected information.

The package provides graph infrastructure that can support higher-level knowledge applications.

### 6. Graph State Comparison

Save graph representations at different points in time and compare them to identify structural changes.

This can serve as a foundation for dependency-change reporting and graph-based monitoring applications.

## Help Test Adaptive Graph Engine

Adaptive Graph Engine v0.3.0 has been developed with **49 passing automated tests**, covering graph operations, algorithms, structural analysis, persistence and graph change tracking.

I'm interested in feedback from developers working with dependency graphs, data engineering, software architecture and related areas.

### Suggested Testing Challenges

1. Model a system containing 5–20 components.
2. Create relationships between those components.
3. Save the graph as JSON.
4. Modify the dependency structure.
5. Create or load a second graph state.
6. Run `compare_graphs()` to identify the differences.
7. Test unusual graph structures, including parallel relationships and cycles.

If you discover a bug, unexpected result or useful missing feature, please [open a GitHub issue](https://github.com/yassine041985/adaptive-graph-engine/issues).

Minimal reproducible examples and test cases are particularly welcome.

## Project Philosophy

Adaptive Graph Engine was built from first principles to explore how graph data structures, algorithms and state comparison can work together in a small, understandable Python library.

The project has two complementary objectives:

- **Software engineering:** Implement and test graph algorithms, data structures, persistence and comparison logic.
- **Practical graph applications:** Provide reusable components for modelling and analysing dependency networks that evolve over time.

The project does not aim to reproduce the complete functionality or performance characteristics of established graph libraries such as NetworkX.

Instead, it provides a focused implementation that developers can inspect, experiment with and extend.

## Requirements

- Python 3.11 or later

## Version

**Current release: 0.3.0**

Available on [PyPI](https://pypi.org/project/adaptive-graph-engine/0.3.0/).

## Source Code and Feedback

GitHub repository:

https://github.com/yassine041985/adaptive-graph-engine

Bug reports, feature suggestions and contributions are welcome.

## Author

**Yassine Chaachaa**

## License

MIT