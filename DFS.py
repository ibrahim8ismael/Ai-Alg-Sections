def DFS(self, goal, start=None, root=None):
    if start is not None:
        lst = [[start]]
    else:
        lst = [[root]]

    visited = []

    while lst:
        # basic search
        current_path = lst.pop()  # LIFO
        current_node = current_path[-1]

        if current_node in visited:
            continue

        visited.append(current_node)

        if current_node == goal:
            return current_path, visited
        else:
            # Sort all elements alphabetically to get a unified answer!
            # Sorting in ascending order to follow "LIFO" principle!
            adjacent_nodes = self.__graph[current_node]
            adjacent_nodes.sort()

            if self.__weighted:
                for node, _ in adjacent_nodes:
                    new_path = current_path.copy()
                    new_path.append(node)
                    lst.append(new_path)
            else:
                for node in adjacent_nodes:
                    new_path = current_path.copy()
                    new_path.append(node)
                    lst.append(new_path)

    raise Exception("Search Failed!")