from adaptive_graph_engine import Graph
from adaptive_graph_engine.algorithms import dijkstra


def test_dijkstra_finds_lowest_cost_path():

    graph = Graph()

    # Direct route: cost 10
    graph.add_edge(
        "salesforce",
        "dashboard",
        weight=10
    )

    # Longer route: total cost 6
    graph.add_edge(
        "salesforce",
        "customer_raw",
        weight=2
    )

    graph.add_edge(
        "customer_raw",
        "customer_clean",
        weight=2
    )

    graph.add_edge(
        "customer_clean",
        "dashboard",
        weight=2
    )

    result = dijkstra(
        graph,
        "salesforce",
        "dashboard"
    )

    assert result == {
        "path": [
            "salesforce",
            "customer_raw",
            "customer_clean",
            "dashboard"
        ],
        "cost": 6
    }


def test_dijkstra_source_is_target():

    graph = Graph()
    graph.add_node("salesforce")

    result = dijkstra(
        graph,
        "salesforce",
        "salesforce"
    )

    assert result == {
        "path": ["salesforce"],
        "cost": 0
    }


def test_dijkstra_unreachable_target():

    graph = Graph()

    graph.add_node("salesforce")
    graph.add_node("dashboard")

    result = dijkstra(
        graph,
        "salesforce",
        "dashboard"
    )

    assert result is None


def test_dijkstra_missing_node():

    graph = Graph()
    graph.add_node("salesforce")

    result = dijkstra(
        graph,
        "salesforce",
        "does_not_exist"
    )

    assert result is None