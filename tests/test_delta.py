from adaptive_graph_engine import Graph
from adaptive_graph_engine.changes import compare_graphs


def test_compare_graphs_detects_added_node():

    old_graph = Graph()
    old_graph.add_node("A")
    old_graph.add_node("B")

    new_graph = Graph()
    new_graph.add_node("A")
    new_graph.add_node("B")
    new_graph.add_node("C")

    changes = compare_graphs(
        old_graph,
        new_graph
    )

    assert changes["nodes_added"] == ["C"]


def test_compare_graphs_detects_removed_node():

    old_graph = Graph()
    old_graph.add_node("A")
    old_graph.add_node("B")
    old_graph.add_node("C")

    new_graph = Graph()
    new_graph.add_node("A")
    new_graph.add_node("B")

    changes = compare_graphs(
        old_graph,
        new_graph
    )

    assert changes["nodes_removed"] == ["C"]


def test_compare_graphs_detects_added_edge():

    old_graph = Graph()
    old_graph.add_node("A")
    old_graph.add_node("B")

    new_graph = Graph()
    new_graph.add_node("A")
    new_graph.add_node("B")

    new_graph.add_edge(
        "A",
        "B",
        metadata={
            "relationship": "FEEDS"
        }
    )

    changes = compare_graphs(
        old_graph,
        new_graph
    )

    assert changes["edges_added"] == [
        ("A", "B", "FEEDS")
    ]


def test_compare_graphs_detects_removed_edge():

    old_graph = Graph()

    old_graph.add_edge(
        "A",
        "B",
        metadata={
            "relationship": "FEEDS"
        }
    )

    new_graph = Graph()
    new_graph.add_node("A")
    new_graph.add_node("B")

    changes = compare_graphs(
        old_graph,
        new_graph
    )

    assert changes["edges_removed"] == [
        ("A", "B", "FEEDS")
    ]


def test_compare_graphs_detects_changed_edge_weight():

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

    assert changes["edges_changed"] == [
        {
            "source": "customer_clean",
            "target": "revenue_model",
            "relationship": "FEEDS",
            "old_weight": 2,
            "new_weight": 8
        }
    ]

def test_compare_graphs_handles_parallel_edges():

    old_graph = Graph()

    old_graph.add_edge(
        "customer_clean",
        "revenue_model",
        weight=2,
        metadata={
            "relationship": "FEEDS"
        }
    )

    old_graph.add_edge(
        "customer_clean",
        "revenue_model",
        weight=5,
        metadata={
            "relationship": "FEEDS"
        }
    )

    new_graph = Graph()

    new_graph.add_edge(
        "customer_clean",
        "revenue_model",
        weight=2,
        metadata={
            "relationship": "FEEDS"
        }
    )

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

    assert changes["edges_changed"] == [
        {
            "source": "customer_clean",
            "target": "revenue_model",
            "relationship": "FEEDS",
            "old_weight": 5,
            "new_weight": 8
        }
    ]