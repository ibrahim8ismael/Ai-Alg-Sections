def A_star(self, goal, start=None):
    if self.__h_flag is None or self.__weighted is None:
        raise Exception("A-Star Algorithm only works with Graphs with Heuristic values and Weighted Graphs!")

    if start is not None:
        lst = [[(start, 0)]]
    else:
        lst = [[("root", 0)]]

    visited = []

    while lst:
        # Sort based on f(n) = g(n) + h(n), and alphabetically
        lst.sort(key=self.__total_cost)

        # Take the path with the lowest cost
        current_path = lst.pop(0)
        current_node = current_path[-1][0]

        if current_node in visited:
            continue

        visited.append(current_node)

        if current_node == goal:
            if self.__check_optimality(current_path):
                print("A-Star Solution is Optimal")
            else:
                print("A-Star Solution is Not Optimal")

            # Return path (just names), visited nodes, and total path cost
            return [node for node, _ in current_path], visited, sum(cost for _, cost in current_path)

        else:
            adjacent_nodes = self.__graph[current_node]
            for node, cost in adjacent_nodes:
                new_path = current_path.copy()
                new_path.append((node, cost))
                lst.append(new_path)

    raise Exception("Search Failed!")