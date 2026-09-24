from adaptive_graph_engine import Graph
from adaptive_graph_engine.algorithms import topological_sort


def test_topological_sort_returns_dependency_order():

    graph = Graph()

    graph.add_edge("raw_data", "clean_data")
    graph.add_edge("clean_data", "revenue_model")
    graph.add_edge("revenue_model", "dashboard")

    result = topological_sort(graph)

    assert result == [
        "raw_data",
        "clean_data",
        "revenue_model",
        "dashboard"
    ]


def test_topological_sort_returns_none_for_cycle():

    graph = Graph()

    graph.add_edge("raw_data", "clean_data")
    graph.add_edge("clean_data", "revenue_model")
    graph.add_edge("revenue_model", "dashboard")

    # Creates a cycle
    graph.add_edge("dashboard", "raw_data")

    result = topological_sort(graph)

    assert result is None

def test_topological_sort_empty_graph():

    graph = Graph()

    result = topological_sort(graph)

    assert result == []


def test_topological_sort_single_node():

    graph = Graph()
    graph.add_node("salesforce")

    result = topological_sort(graph)

    assert result == ["salesforce"]
