def UCS(self, goal, start=None, root=None):
    if not self.__weighted:
        raise Exception("Uniform Cost Search only works with Weighted Graphs!")

    if start is not None:
        lst = [[(start, 0)]]
    else:
        lst = [[(root, 0)]]

    visited = []

    while lst:
        # Sort paths by total cost and then alphabetically
        lst.sort(key=self.__path_cost)

        current_path = lst.pop(0)  # FIFO with priority
        current_node = current_path[-1][0]

        if current_node in visited:
            continue

        visited.append(current_node)

        if current_node == goal:
            path_nodes = [node for node, _ in current_path]
            total_cost = sum(cost for _, cost in current_path)
            return path_nodes, total_cost, visited

        adjacent_nodes = self.__graph.get(current_node, [])
        for node, cost in adjacent_nodes:
            new_path = current_path.copy()
            new_path.append((node, cost))
            lst.append(new_path)

    raise Exception("Search Failed!")

def __path_cost(self, path):
    total_cost = sum(cost for _, cost in path)
    return total_cost, path[-1][0]
