def _edge_set(graph):

    edges = set()

    for source, edge_list in graph.edge.items():

        for edge in edge_list:

            relationship = edge["metadata"].get(
                "relationship"
            )

            edges.add(
                (
                    source,
                    edge["target"],
                    relationship
                )
            )

    return edges


def _find_changed_edges(old_graph, new_graph):

    changed_edges = []

    for source, old_edge_list in old_graph.edge.items():

        new_edge_list = new_graph.edge.get(
            source,
            []
        )

        matched_new_edges = set()

        for old_edge in old_edge_list:

            old_relationship = old_edge["metadata"].get(
                "relationship"
            )

            # First look for an exact unchanged edge.
            exact_match = None

            for index, new_edge in enumerate(new_edge_list):

                if index in matched_new_edges:
                    continue

                new_relationship = new_edge["metadata"].get(
                    "relationship"
                )

                if (
                    old_edge["target"] == new_edge["target"]
                    and
                    old_relationship == new_relationship
                    and
                    old_edge["weight"] == new_edge["weight"]
                ):
                    exact_match = index
                    break

            if exact_match is not None:

                matched_new_edges.add(
                    exact_match
                )

                continue

            # No exact match.
            # Now look for the same logical edge with a changed weight.
            for index, new_edge in enumerate(new_edge_list):

                if index in matched_new_edges:
                    continue

                new_relationship = new_edge["metadata"].get(
                    "relationship"
                )

                same_edge = (
                    old_edge["target"] == new_edge["target"]
                    and
                    old_relationship == new_relationship
                )

                if same_edge:

                    matched_new_edges.add(
                        index
                    )

                    changed_edges.append({
                        "source": source,
                        "target": old_edge["target"],
                        "relationship": old_relationship,
                        "old_weight": old_edge["weight"],
                        "new_weight": new_edge["weight"]
                    })

                    break

    return changed_edges

def compare_graphs(old_graph, new_graph):
    """
    Compare two graph states and return the structural changes
    between the old graph and the new graph.
    """

    old_nodes = set(old_graph.node)
    new_nodes = set(new_graph.node)

    nodes_added = new_nodes - old_nodes
    nodes_removed = old_nodes - new_nodes

    old_edges = _edge_set(old_graph)
    new_edges = _edge_set(new_graph)

    edges_added = new_edges - old_edges
    edges_removed = old_edges - new_edges

    edges_changed = _find_changed_edges(
        old_graph,
        new_graph
    )

    return {
        "nodes_added": sorted(nodes_added),
        "nodes_removed": sorted(nodes_removed),
        "edges_added": sorted(edges_added),
        "edges_removed": sorted(edges_removed),
        "edges_changed": edges_changed
    }