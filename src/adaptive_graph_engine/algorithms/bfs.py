from collections import deque


def find_shortest_path(
    graph,
    source,
    target
):

    if (
        source not in graph.node
        or
        target not in graph.node
    ):
        return None

    queue = deque([
        source
    ])

    parent = {
        source: None
    }

    while queue:

        current_node = (
            queue.popleft()
        )

        if (
            current_node
            ==
            target
        ):

            path = []

            while (
                current_node
                is not None
            ):

                path.append(
                    current_node
                )

                current_node = (
                    parent[
                        current_node
                    ]
                )

            path.reverse()

            return path

        for node in graph.get_neighbors(
            current_node
        ):

            if node not in parent:

                parent[
                    node
                ] = current_node

                queue.append(
                    node
                )

    return None