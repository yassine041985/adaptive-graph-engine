from adaptive_graph_engine import Graph
from adaptive_graph_engine.algorithms import has_cycle


def test_cycle_detects_cycle():

    graph = Graph()

    graph.add_edge("salesforce", "customer_raw")
    graph.add_edge("customer_raw", "customer_clean")
    graph.add_edge("customer_clean", "revenue_model")

    # Creates the cycle
    graph.add_edge("revenue_model", "customer_raw")

    result = has_cycle(graph)

    assert result is True


def test_cycle_detects_no_cycle():

    graph = Graph()

    graph.add_edge("salesforce", "customer_raw")
    graph.add_edge("customer_raw", "customer_clean")
    graph.add_edge("customer_clean", "revenue_model")
    graph.add_edge("revenue_model", "dashboard")

    result = has_cycle(graph)

    assert result is False

def test_cycle_empty_graph():

    graph = Graph()

    result = has_cycle(graph)

    assert result is False


def test_cycle_detects_self_loop():

    graph = Graph()

    graph.add_edge(
        "salesforce",
        "salesforce"
    )

    result = has_cycle(graph)

    assert result is True