from adaptive_graph_engine import Graph


def test_number_of_nodes():

    graph = Graph()

    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")

    assert graph.number_of_nodes() == 3


def test_number_of_edges():

    graph = Graph()

    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("A", "C")

    assert graph.number_of_edges() == 3


def test_in_degree():

    graph = Graph()

    graph.add_edge("A", "B")
    graph.add_edge("C", "B")
    graph.add_edge("B", "D")

    assert graph.in_degree("B") == 2


def test_out_degree():

    graph = Graph()

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("D", "A")

    assert graph.out_degree("A") == 2


def test_degree_counts_parallel_edges():

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

    graph.add_edge(
        "salesforce",
        "customer_clean",
        metadata={"relationship": "INGESTS_TO"}
    )

    assert graph.in_degree("customer_clean") == 1
    assert graph.out_degree("customer_clean") == 2
    assert graph.degree("customer_clean") == 3