from adaptive_graph_engine import Graph
from adaptive_graph_engine.algorithms import find_shortest_path


def test_bfs_finds_shortest_path():

    graph = Graph()

    graph.add_edge("salesforce", "customer_raw")
    graph.add_edge("customer_raw", "customer_clean")
    graph.add_edge("customer_clean", "dashboard")

    graph.add_edge("salesforce", "dashboard")

    path = find_shortest_path(
        graph,
        "salesforce",
        "dashboard"
    )

    assert path == [
        "salesforce",
        "dashboard"
    ]


def test_bfs_source_is_target():

    graph = Graph()
    graph.add_node("salesforce")

    path = find_shortest_path(
        graph,
        "salesforce",
        "salesforce"
    )

    assert path == ["salesforce"]


def test_bfs_unreachable_target():

    graph = Graph()

    graph.add_node("salesforce")
    graph.add_node("dashboard")

    path = find_shortest_path(
        graph,
        "salesforce",
        "dashboard"
    )

    assert path is None


def test_bfs_missing_node():

    graph = Graph()
    graph.add_node("salesforce")

    path = find_shortest_path(
        graph,
        "salesforce",
        "does_not_exist"
    )

    assert path is None