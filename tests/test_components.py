from adaptive_graph_engine import Graph
from adaptive_graph_engine.algorithms import get_connected_components


def test_connected_components_finds_two_components():

    graph = Graph()

    graph.add_edge("A", "B")
    graph.add_edge("B", "C")

    graph.add_edge("D", "E")

    components = get_connected_components(graph)

    component_sets = [set(component) for component in components]

    assert {"A", "B", "C"} in component_sets
    assert {"D", "E"} in component_sets


def test_connected_components_single_component():

    graph = Graph()

    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("C", "D")

    components = get_connected_components(graph)

    assert len(components) == 1
    assert set(components[0]) == {"A", "B", "C", "D"}


def test_connected_components_isolated_node():

    graph = Graph()

    graph.add_node("A")

    components = get_connected_components(graph)

    assert components == [["A"]]


def test_connected_components_empty_graph():

    graph = Graph()

    components = get_connected_components(graph)

    assert components == []