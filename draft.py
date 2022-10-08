# def dijkstra(source, dest, all_nodes):
#     shortest_path_set = set()
#     total_cost = 0
#     for v in graph.nodes:
#         v.c = -1
#         v.p = None
#         v.d = sys.maxsize

#     source.c = 0
#     source.d = 0

#     while len(all_nodes) != 0:
#         current = extract_min(all_nodes)
#         total_cost += current.d
#         shortest_path_set.add(current)

#         if dest == current:
#             break

#         for v in current.adj:
#             if (min.d + weight[current][v]) < v.d:
#                 v.d = current.d + weight[current][v]
#                 v.p = current
#     return total_cost, shortest_path_set


# def extract_min(nodes):
#     min_dist = min(nodes, key=attrgetter('d'))
#     nodes.remove(min_dist)
#     return min_dist


# weight = [][]  # weight[x][y] is the cost for edge x -> y
