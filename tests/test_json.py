from adaptive_graph_engine import Graph
from adaptive_graph_engine.io import save_json, load_json


def test_save_and_load_json(tmp_path):

    graph = Graph()

    graph.add_node(
        "salesforce",
        platform="Salesforce"
    )

    graph.add_edge(
        "salesforce",
        "customer_raw",
        weight=2,
        metadata={
            "relationship": "INGESTS_TO"
        }
    )

    filename = tmp_path / "graph.json"

    save_json(graph, filename)

    restored = load_json(filename)

    assert "salesforce" in restored.node
    assert "customer_raw" in restored.node

    assert restored.node["salesforce"]["platform"] == "Salesforce"

    edge = restored.edge["salesforce"][0]

    assert edge["target"] == "customer_raw"
    assert edge["weight"] == 2
    assert edge["metadata"]["relationship"] == "INGESTS_TO"


def test_json_preserves_parallel_relationships(tmp_path):

    graph = Graph()

    graph.add_edge(
        "customer_clean",
        "revenue_model",
        metadata={
            "relationship": "FEEDS"
        }
    )

    graph.add_edge(
        "customer_clean",
        "revenue_model",
        metadata={
            "relationship": "VALIDATES"
        }
    )

    filename = tmp_path / "graph.json"

    save_json(graph, filename)

    restored = load_json(filename)

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