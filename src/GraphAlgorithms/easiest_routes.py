def dijkstra(graph, start_vertex):
    pass


def bellman_ford(graph, start_vertex):
    pass


def directed_acyclic(graph, start_vertex):
    pass


def relax(vertex_u,vertex_v,delta_weights, edges_weights, parents):
    if delta_weights[vertex_v] > delta_weights[vertex_u] + edges_weights[vertex_u, vertex_v]:
        delta_weights[vertex_v] = delta_weights[vertex_u] + edges_weights[vertex_u, vertex_v]
        if parents is not None:
            parents[vertex_v] = vertex_u
