from typing import List, Dict, Set


def find_all_paths(graph: Dict[int, List[int]], start: int) -> List[List[int]]:
    """
    Return all root-to-leaf DFS paths in an undirected graph.

    A leaf is defined as a node with no unvisited neighbors.
    This function avoids cycles using a visited set and copies
    the current path at each leaf.

    Parameters
    ----------
    graph : Dict[int, List[int]]
        Adjacency list of the graph.
    start : int
        Starting node for DFS traversal.

    Returns
    -------
    List[List[int]]
        A list of all root-to-leaf paths.
    """

    paths: List[List[int]] = []
    curr_path: List[int] = []
    visited: Set[int] = set()

    def dfs(node: int):
        curr_path.append(node)
        visited.add(node)

        leaf = True
        for child in graph[node]:
            if child not in visited:
                leaf = False
                dfs(child)

        if leaf:
            paths.append(curr_path.copy())

        visited.remove(node)
        curr_path.pop()

    dfs(start)
    return paths


# Run a quick check when module is executed directly
if __name__ == "__main__":
    graph = {
        1: [2, 5, 6],
        2: [1, 3, 4],
        3: [2],
        4: [2],
        5: [1],
        6: [1]
    }

    result = find_all_paths(graph, 1)
    print("All root-to-leaf paths:", result)
