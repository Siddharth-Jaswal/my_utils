from collections import deque
from typing import List, Tuple, Dict, Any


def shortest_path_in_binary_grid(
    grid: List[List[int]],
    start: Tuple[int, int],
    end: Tuple[int, int],
    options: Dict[str, Any] = {"diagonal": False},
) -> int:
    """
    Generic BFS for shortest path in a grid.

    Parameters:
        grid      : 2D list (0=open, 1=blocked)
        start     : (x_src, y_src)
        end       : (x_dest, y_dest)
        options   : {'diagonal': bool}

    Returns:
        int : shortest path length or -1 if no path exists
    """

    n, m = len(grid), len(grid[0])
    (x_src, y_src), (x_dest, y_dest) = start, end

    # 4 or 8 directional moves
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1)
    ] if not options.get("diagonal", False) else [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    # Check start/end
    if grid[x_src][y_src] == 1 or grid[x_dest][y_dest] == 1:
        return -1

    # BFS queue and visited set
    queue = deque([(x_src, y_src, 1)])  # distance starts at 1
    visited = {(x_src, y_src)}

    while queue:
        x, y, dist = queue.popleft()

        # Reached destination
        if (x, y) == (x_dest, y_dest):
            return dist

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < n and 0 <= ny < m
                and grid[nx][ny] == 0
                and (nx, ny) not in visited
            ):
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))

    return -1







