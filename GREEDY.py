def Greedy_search(self, goal, start=None):
    if self.__h_flag is None:
        raise Exception("Greedy Search only works with Graphs with Heuristic values!")

    if start is not None:
        lst = [[start]]
    else:
        lst = [["root"]]

    visited = []

    while lst:
        # Sort based on heuristic cost and alphabetical order
        lst.sort(key=lambda path: (self.__heuristic_cost(path[-1]), path[-1]))

        current_path = lst.pop(0)  # FIFO
        lst.clear()  # Greedy: only one path considered at a time
        current_node = current_path[-1]

        if current_node in visited:
            continue

        visited.append(current_node)

        if current_node == goal:
            return current_path, visited
        else:
            adjacent_nodes = self.__graph[current_node]

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

    return "Search Failed"