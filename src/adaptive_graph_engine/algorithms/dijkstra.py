import heapq


def dijkstra(
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

    priority_queue = []

    distance = {}

    parent = {
        source: None
    }

    for node in graph.node:

        distance[
            node
        ] = float(
            "inf"
        )

    distance[
        source
    ] = 0

    heapq.heappush(
        priority_queue,
        (
            0,
            source
        )
    )

    while priority_queue:

        (
            current_distance,
            current_node
        ) = heapq.heappop(
            priority_queue
        )

        if (
            current_distance
            >
            distance[
                current_node
            ]
        ):
            continue

        if (
            current_node
            ==
            target
        ):
            break

        for (
            neighbour,
            weight
        ) in graph.get_weighted_neighbors(
            current_node
        ):

            new_distance = (
                current_distance
                +
                weight
            )

            if (
                new_distance
                <
                distance[
                    neighbour
                ]
            ):

                distance[
                    neighbour
                ] = new_distance

                parent[
                    neighbour
                ] = current_node

                heapq.heappush(
                    priority_queue,
                    (
                        new_distance,
                        neighbour
                    )
                )

    if (
        distance[
            target
        ]
        ==
        float(
            "inf"
        )
    ):
        return None

    path = []

    current_node = target

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

    return {
        "path": path,
        "cost": distance[target]
    }