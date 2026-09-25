from adaptive_graph_engine import Graph


def test_graph_to_dictionary():

    graph = Graph()

    graph.add_node(
        "salesforce",
        platform="Salesforce"
    )

    graph.add_edge(
        "salesforce",
        "customer_raw",
        weight=2,
        metadata={"relationship": "INGESTS_TO"}
    )

    data = graph.to_dictionary()

    assert "salesforce" in data["nodes"]
    assert "customer_raw" in data["nodes"]
    assert data["edges"]["salesforce"][0]["target"] == "customer_raw"


def test_graph_from_dictionary():

    data = {
        "nodes": {
            "A": {},
            "B": {}
        },
        "edges": {
            "A": [
                {
                    "target": "B",
                    "weight": 3,
                    "metadata": {
                        "relationship": "FEEDS"
                    }
                }
            ]
        }
    }

    graph = Graph.from_dictionary(data)

    assert "A" in graph.node
    assert "B" in graph.node
    assert graph.get_neighbors("A") == ["B"]


def test_serialization_preserves_metadata_and_weight():

    graph = Graph()

    graph.add_node(
        "revenue_model",
        platform="Python",
        environment="production"
    )

    graph.add_edge(
        "revenue_model",
        "executive_dashboard",
        weight=5,
        metadata={
            "relationship": "POWERS"
        }
    )

    restored = Graph.from_dictionary(
        graph.to_dictionary()
    )

    assert restored.node["revenue_model"]["platform"] == "Python"
    assert restored.node["revenue_model"]["environment"] == "production"

    edge = restored.edge["revenue_model"][0]

    assert edge["weight"] == 5
    assert edge["metadata"]["relationship"] == "POWERS"


def test_serialization_preserves_parallel_edges():

    graph = Graph()

    graph.add_edge(
        "customer_clean",
        "revenue_model",
        metadata={"relationship": "FEEDS"}
    )

    graph.add_edge(
        "customer_clean",
        "revenue_model",
        metadata={"relationship": "VALIDATES"}
    )

    restored = Graph.from_dictionary(
        graph.to_dictionary()
    )

    edges = restored.edge["customer_clean"]

    assert len(edges) == 2

    relationships = {
        edge["metadata"]["relationship"]
        for edge in edges
    }

    assert relationships == {
        "FEEDS",
        "VALIDATES"
    }