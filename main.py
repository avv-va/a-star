from a_star import a_star, print_path, distance_traveled
from models import Node, Edge, Graph


def get_input():
    nodes = []
    for i in range(0, 14):
        nodes.append(Node(i))
    
    start_node = nodes[0]
    final_node = nodes[13]

    e01 = Edge(nodes[0], nodes[1]); e02 = Edge(nodes[0], nodes[2]); e03 = Edge(nodes[0], nodes[3])
    e04 = Edge(nodes[0], nodes[4]); e05 = Edge(nodes[0], nodes[5]); e16 = Edge(nodes[1], nodes[6])
    e17 = Edge(nodes[1], nodes[7]); e21 = Edge(nodes[2], nodes[1]); e27 = Edge(nodes[2], nodes[7])
    e28 = Edge(nodes[2], nodes[8]); e29 = Edge(nodes[2], nodes[9]); e39 = Edge(nodes[3], nodes[9])
    e49 = Edge(nodes[4], nodes[9]); e410 = Edge(nodes[4], nodes[10]); e411 = Edge(nodes[4], nodes[11])
    e45 = Edge(nodes[4], nodes[5]); e511 = Edge(nodes[5], nodes[11]); e512 = Edge(nodes[5], nodes[12])
    e67 = Edge(nodes[6], nodes[7]); e713 = Edge(nodes[7], nodes[13]); e813 = Edge(nodes[8], nodes[13])
    e913 = Edge(nodes[9], nodes[13]); e1013 = Edge(nodes[10], nodes[13]); e1113 = Edge(nodes[11], nodes[13])
    e1211 = Edge(nodes[12], nodes[11])
    
    edges = [e01, e02, e03, e04, e05, e16, e17, e21, e27, e28, e29, e39, e49, e410,
             e411, e45, e511, e512, e67, e713, e813, e913, e1013, e1113, e1211]
    
    weight = {
        e01: 3,
        e02: 1,
        e03: 3,
        e04: 1,
        e05: 3,
        e16: 1,
        e17: 3,
        e21: 0,
        e27: 3,
        e28: 2,
        e29: 1,
        e39: 1,
        e49: 1,
        e410: 2,
        e411: 3,
        e45: 2,
        e511: 1,
        e512: 1,
        e67: 1,
        e713: 1,
        e813: 3,
        e913: 3,
        e1013: 3,
        e1113: 1,
        e1211: 3,
    }

    heuristic = {
        nodes[0]: 4,
        nodes[1]: 3,
        nodes[2]: 3,
        nodes[3]: 3,
        nodes[4]: 3,
        nodes[5]: 3,
        nodes[6]: 2,
        nodes[7]: 1,
        nodes[8]: 1,
        nodes[9]: 1,
        nodes[10]: 1,
        nodes[11]: 1,
        nodes[12]: 2,
        nodes[13]: 0,
    }

    graph = Graph(nodes, edges, weight)

    return graph, start_node, final_node, heuristic

def set_heuristic_zero_for_dijkstra(heuristic):
    for node in heuristic:
        heuristic[node] = 0
    return heuristic


if __name__ == "__main__":
    graph, start_node, final_node, heuristic = get_input()

    # heuristic = set_heuristic_zero_for_dijkstra(heuristic)

    path = a_star(graph, start_node, final_node, heuristic)
    
    print_path(final_node)
    print("distance_traveled: ", distance_traveled(final_node, graph))
