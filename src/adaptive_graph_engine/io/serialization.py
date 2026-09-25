import json

from adaptive_graph_engine.graph import Graph


def save_json(graph, filename):
    """
    Save a graph to a JSON file.
    """

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            graph.to_dictionary(),
            file,
            indent=4
        )


def load_json(filename):
    """
    Load a graph from a JSON file.
    """

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    return Graph.from_dictionary(data)