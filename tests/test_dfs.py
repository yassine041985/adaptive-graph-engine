from adaptive_graph_engine import Graph
from adaptive_graph_engine.algorithms import find_depth_first


def test_dfs_finds_deep_path():

    graph = Graph()

    graph.add_edge("salesforce", "customer_raw")
    graph.add_edge("customer_raw", "customer_clean")
    graph.add_edge("customer_clean", "revenue_model")
    graph.add_edge("revenue_model", "dashboard")

    path = find_depth_first(
        graph,
        "salesforce",
        "dashboard"
    )

    assert path == [
        "salesforce",
        "customer_raw",
        "customer_clean",
        "revenue_model",
        "dashboard"
    ]


def test_dfs_source_is_target():

    graph = Graph()
    graph.add_node("salesforce")

    path = find_depth_first(
        graph,
        "salesforce",
        "salesforce"
    )

    assert path == ["salesforce"]


def test_dfs_unreachable_target():

    graph = Graph()

    graph.add_node("salesforce")
    graph.add_node("dashboard")

    path = find_depth_first(
        graph,
        "salesforce",
        "dashboard"
    )

    assert path is None


def test_dfs_missing_node():

    graph = Graph()
    graph.add_node("salesforce")

    path = find_depth_first(
        graph,
        "salesforce",
        "does_not_exist"
    )

    assert path is None