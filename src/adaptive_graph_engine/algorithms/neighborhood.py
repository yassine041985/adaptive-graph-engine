from collections import deque


def get_neighborhood(graph, start_node, depth=1):
    """
    Return the local graph surrounding a node up to a given depth.

    Both outgoing and incoming connections are considered.
    """

    if start_node not in graph.node:
        return {
            "nodes": [],
            "edges": []
        }

    visited = {start_node}

    queue = deque([
        (start_node, 0)
    ])

    while queue:

        current, current_depth = queue.popleft()

        if current_depth >= depth:
            continue

        neighbours = set(
            graph.get_neighbors(current)
        )

        neighbours.update(
            graph.get_predecessors(current)
        )

        for neighbour in neighbours:

            if neighbour not in visited:

                visited.add(neighbour)

                queue.append(
                    (
                        neighbour,
                        current_depth + 1
                    )
                )

    edges = []

    for source in visited:

        for edge in graph.edge.get(source, []):

            target = edge["target"]

            if target in visited:

                edges.append({
                    "source": source,
                    "target": target,
                    "metadata": edge["metadata"]
                })

    return {
        "nodes": sorted(visited),
        "edges": edges
    }