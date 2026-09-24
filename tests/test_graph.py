from adaptive_graph_engine import Graph


def test_graph_nodes_and_edges():

    graph = Graph()

    graph.add_node("salesforce")
    graph.add_node("customer_raw")
    graph.add_node("customer_clean")

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

    assert "salesforce" in graph.node
    assert "customer_raw" in graph.node
    assert "customer_clean" in graph.node

    assert graph.get_neighbors("salesforce") == ["customer_raw"]
    assert graph.get_successors("customer_raw") == ["customer_clean"]
    assert graph.get_predecessors("customer_clean") == ["customer_raw"]

def test_get_edges():

    graph = Graph()

    graph.add_edge(
        "salesforce",
        "customer_raw",
        metadata={"relationship": "INGESTS_TO"}
    )

    edges = graph.get_edges("salesforce")

    assert len(edges) == 1
    assert edges[0]["target"] == "customer_raw"


def test_edge_weights():

    graph = Graph()

    graph.add_edge(
        "customer_raw",
        "customer_clean",
        weight=5
    )

    weighted_neighbors = graph.get_weighted_neighbors("customer_raw")

    assert weighted_neighbors == [("customer_clean", 5)]


def test_relationship_metadata():

    graph = Graph()

    graph.add_edge(
        "revenue_model",
        "executive_dashboard",
        metadata={"relationship": "POWERS"}
    )

    relationships = graph.get_relationships("revenue_model")

    assert relationships == [
        {
            "target": "executive_dashboard",
            "metadata": {
                "relationship": "POWERS"
            }
        }
    ]
