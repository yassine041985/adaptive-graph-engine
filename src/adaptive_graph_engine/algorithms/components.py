from collections import deque


def get_connected_components(graph):
    """
    Return the connected components of the graph.

    Direction is ignored when determining whether nodes
    belong to the same component.
    """

    visited = set()
    components = []

    for start_node in graph.node:

        if start_node in visited:
            continue

        component = []
        queue = deque([start_node])
        visited.add(start_node)

        while queue:

            current = queue.popleft()
            component.append(current)

            neighbours = set(
                graph.get_neighbors(current)
            )

            neighbours.update(
                graph.get_predecessors(current)
            )

            for neighbour in neighbours:

                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        components.append(component)

    components.sort(
        key=len,
        reverse=True
    )

    return components