def find_edge(node_a, node_b):
    for edge in node_a.edges:
        if edge.node_b == node_b:
            return edge

def distance_traveled(node, graph):
    distance_traveled = 0
    while node.parent:
        edge = find_edge(node.parent, node)
        distance_traveled += graph.weight[edge]
        node = node.parent
    return distance_traveled


def sort_priority_q(node, heuristic, graph):
    return heuristic[node] + distance_traveled(node, graph)


def change_parent_if_needed(current_parent, new_parent, node, graph):
    current_distance = distance_traveled(node, graph)

    node.parent = new_parent
    new_distance = distance_traveled(node, graph)
    if current_distance < new_distance:
        node.parent = current_parent
    else:
        node.parent = new_parent


def update_priority_queue(priority_queue, to_be_removed, adj_nodes, graph):
    for adj_node in adj_nodes:
        if adj_node.seen:
            continue
        if adj_node in priority_queue:
            change_parent_if_needed(adj_node.parent, to_be_removed, adj_node, graph)
        else:
            adj_node.parent = to_be_removed
            priority_queue.append(adj_node)


def print_path(node):
    path = [node.id]
    while node.parent:
        path.append(node.parent.id)
        node = node.parent
    path.reverse()
    print("path: ", path)

def a_star(graph, start_node, final_node, heuristic):
    priority_queue = [start_node]
    to_be_removed = start_node

    iterations = 0
    while to_be_removed != final_node:
        to_be_removed = priority_queue[0]
        to_be_removed.seen = True
        adj_nodes = to_be_removed.adjacent_nodes

        update_priority_queue(priority_queue, to_be_removed, adj_nodes, graph)

        priority_queue.remove(to_be_removed)
        priority_queue.sort(key=lambda node: sort_priority_q(node, heuristic, graph))

        iterations += 1
    
    print("iterations count: ", iterations)
