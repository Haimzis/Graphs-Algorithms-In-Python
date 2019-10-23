from collections import defaultdict
from sys import maxsize
from GraphAlgorithms import sorts
import queue


def dijkstra(graph, weights, start_vertex):
    p_queue = queue.PriorityQueue()
    delta_weights = defaultdict(lambda: maxsize)
    parents_tree = defaultdict(lambda: None)
    initialize_single_source(graph, start_vertex, delta_weights, parents_tree)
    for (vertex, delta_weight) in delta_weights:
        # p_queue.put((delta_weight, vertex))
        pass


def bellman_ford(graph, weights, start_vertex):
    edges_list = get_edge_list(graph)
    delta_weights = defaultdict(lambda: maxsize)
    parents_tree = defaultdict(lambda: None)
    initialize_single_source(graph, start_vertex, delta_weights, parents_tree)
    for _ in range(1, graph.keys().__len__() - 1):
        for (vertex_u, vertex_v) in edges_list:
            relax(vertex_u, vertex_v, delta_weights, weights, parents_tree)
    for (vertex_u, vertex_v) in edges_list:
        if delta_weights[vertex_v] > delta_weights[vertex_u] + weights[(vertex_u, vertex_v)]:
            return tuple(("Success", None, None))
    return tuple(("Success", delta_weights, parents_tree))


def directed_acyclic(graph, weights, start_vertex):
    delta_weights = defaultdict(lambda: maxsize)
    parents_tree = defaultdict(lambda: None)
    initialize_single_source(graph, start_vertex, delta_weights, parents_tree)
    topological_sorted_list = sorts.topological_sorting(graph)
    if topological_sorted_list[0] == "Failure":
        return tuple(("Failure", None, None))
    for vertex_u in topological_sorted_list[1]:
        for vertex_v in graph[vertex_u]:
            relax(vertex_u, vertex_v, delta_weights, weights, parents_tree)
    return tuple(("Success", delta_weights, parents_tree))


def relax(vertex_u, vertex_v, delta_weights, edges_weights, parents):
    if delta_weights[vertex_v] > delta_weights[vertex_u] + edges_weights[vertex_u, vertex_v]:
        delta_weights[vertex_v] = delta_weights[vertex_u] + edges_weights[vertex_u, vertex_v]
        parents[vertex_v] = vertex_u


def initialize_single_source(graph, start_vertex, delta_weights, parents_tree):
    for vertex in graph.keys():
        delta_weights[vertex]
        parents_tree[vertex]
    delta_weights[start_vertex] = 0


def get_edge_list(graph):
    return [(vertex_v, vertex_u) for vertex_v in graph.keys() for vertex_u in graph[vertex_v]]
