def find_depth_first(
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

    stack = [
        source
    ]

    parent = {
        source: None
    }

    while stack:

        current_node = (
            stack.pop()
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

                stack.append(
                    node
                )

    return None