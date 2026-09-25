from collections import deque


def topological_sort(graph):

    incoming_edges = {}

    for node in graph.node:

        incoming_edges[
            node
        ] = 0

    for source in graph.node:

        for target in graph.get_neighbors(
            source
        ):

            incoming_edges[
                target
            ] += 1

    queue = deque()

    for node in incoming_edges:

        if (
            incoming_edges[
                node
            ]
            ==
            0
        ):

            queue.append(
                node
            )

    order = []

    while queue:

        current_node = (
            queue.popleft()
        )

        order.append(
            current_node
        )

        for neighbour in graph.get_neighbors(
            current_node
        ):

            incoming_edges[
                neighbour
            ] -= 1

            if (
                incoming_edges[
                    neighbour
                ]
                ==
                0
            ):

                queue.append(
                    neighbour
                )

    if (
        len(order)
        !=
        len(graph.node)
    ):

        return None

    return order