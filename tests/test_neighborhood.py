from adaptive_graph_engine import Graph
from adaptive_graph_engine.algorithms import get_neighborhood


def test_neighborhood_depth_one():

    graph = Graph()

    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("C", "D")

    result = get_neighborhood(graph, "B", depth=1)

    assert set(result["nodes"]) == {"A", "B", "C"}


def test_neighborhood_depth_two():

    graph = Graph()

    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("C", "D")

    result = get_neighborhood(graph, "B", depth=2)

    assert set(result["nodes"]) == {"A", "B", "C", "D"}


def test_neighborhood_missing_node():

    graph = Graph()

    graph.add_edge("A", "B")

    result = get_neighborhood(graph, "X", depth=1)

    assert result == {
        "nodes": [],
        "edges": []
    }


def test_neighborhood_includes_internal_edges():

    graph = Graph()

    graph.add_edge(
        "A",
        "B",
        metadata={"relationship": "FEEDS"}
    )

    graph.add_edge(
        "B",
        "C",
        metadata={"relationship": "POWERS"}
    )

    result = get_neighborhood(graph, "B", depth=1)

    assert len(result["edges"]) == 2