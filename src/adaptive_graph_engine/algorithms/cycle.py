def detected_cycle(
    graph,
    current_node,
    visited,
    current_path
):

    if current_node in current_path:
        return True

    if current_node in visited:
        return False

    visited.add(
        current_node
    )

    current_path.add(
        current_node
    )

    for neighbour in graph.get_neighbors(
        current_node
    ):

        if detected_cycle(
            graph,
            neighbour,
            visited,
            current_path
        ):

            return True

    current_path.remove(
        current_node
    )

    return False


def has_cycle(
    graph
):

    visited = set()

    current_path = set()

    for node in graph.node:

        if node not in visited:

            if detected_cycle(
                graph,
                node,
                visited,
                current_path
            ):

                return True

    return False