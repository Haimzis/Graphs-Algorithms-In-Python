from sys import maxsize
import queue


class Graph:
    def __init__(self, adjacency_list, edges_weights):
        self.adjacency_list = adjacency_list
        self.weights = edges_weights

    def __str__(self):
        graph_string = "The vertex of the graph are:\n"
        for counter, vertex in enumerate(self.adjacency_list.keys()):
            graph_string += f"{counter + 1}.{vertex}\n"
        graph_string += "\nThe edges of the graph are:\n| "
        for vertex in self.adjacency_list:
            for adj in self.adjacency_list[vertex]:
                graph_string += f"({vertex},{adj}) | "
        return graph_string

    def add_vertex(self, *args):
        for vertex in args:
            self.adjacency_list[vertex] = []

    def add_edge(self, edge, weight=0):
        vertex_u, vertex_v = edge
        self.adjacency_list[vertex_u].append(vertex_v)
        self.weights[edge] = weight

    # Topological Sort
    def topological_sorting(self):
        top_sort = ()
        sources_queue = queue.Queue()
        in_degrees_counter = self.in_degrees()
        for vertex, counter in in_degrees_counter.items():
            if counter == 0:
                sources_queue.queue.append(vertex)
        while not sources_queue.empty():
            vertex = sources_queue.queue.popleft()
            top_sort += (vertex,)
            for adjacent in self.adjacency_list[vertex]:
                in_degrees_counter[adjacent] -= 1
                if in_degrees_counter[adjacent] == 0:
                    sources_queue.queue.append(adjacent)
        for vertex, counter in in_degrees_counter.items():
            if counter != 0:
                return tuple(("Failure", None))
        return tuple(("Success", top_sort))

    def in_degrees(self):
        in_degree_vertexes = {vertex: 0 for (vertex, adjacency_list) in self.adjacency_list.items()}
        for vertex in self.adjacency_list:
            for adjacent in self.adjacency_list[vertex]:
                in_degree_vertexes[adjacent] += 1
        return in_degree_vertexes

    # Scans
    def dfs(self):
        dfs_order = []
        colors = {vertex: "white" for vertex in self.adjacency_list.keys()}
        for vertex in self.adjacency_list.keys():
            if colors[vertex] == "white":
                self.visit(vertex, colors, dfs_order)
        return tuple(dfs_order)

    def visit(self, vertex_u, colors, dfs_order):
        colors[vertex_u] = "gray"
        for adjacent in self.adjacency_list[vertex_u]:
            if colors[adjacent] == "white":
                self.visit(adjacent, colors, dfs_order)
        colors[vertex_u] = "black"
        dfs_order.append(vertex_u)

    def bfs(self, source_vertex):
        delta_routes_length = {vertex: "infinite" for vertex in self.adjacency_list.keys()}
        vertexes_queue = queue.Queue()
        vertexes_queue.queue.append(source_vertex)
        delta_routes_length[source_vertex] = 0
        while not vertexes_queue.empty():
            vertex_u = vertexes_queue.queue.popleft()
            for adjacent in self.adjacency_list[vertex_u]:
                if delta_routes_length[adjacent] == "infinite":
                    delta_routes_length[adjacent] = delta_routes_length[vertex_u] + 1
                    vertexes_queue.queue.append(adjacent)
        return delta_routes_length

    # Shortest Paths
    def dijkstra(self, source_vertex):
        if min(dict(self.weights).values()) < 0:
            return tuple(("Failure", None, None))
        p_queue = queue.PriorityQueue()
        delta_weights = {}
        parents_tree = {}
        self.initialize_single_source(source_vertex, delta_weights, parents_tree)
        p_queue.put((0, source_vertex))
        while not p_queue.empty():
            vertex_u = p_queue.get()[1]
            for vertex_v in self.adjacency_list[vertex_u]:
                if delta_weights[vertex_v] > delta_weights[vertex_u] + self.weights[(vertex_u, vertex_v)]:
                    p_queue.put((delta_weights[vertex_v], vertex_v))
                self.relax(vertex_u, vertex_v, delta_weights, parents_tree)
        return tuple(("Success", delta_weights, parents_tree))

    def bellman_ford(self, source_vertex):
        edges_list = self.get_edge_list()
        delta_weights = {}
        parents_tree = {}
        self.initialize_single_source(source_vertex, delta_weights, parents_tree)
        for _ in range(1, self.adjacency_list.keys().__len__() - 1):
            for (vertex_u, vertex_v) in edges_list:
                self.relax(vertex_u, vertex_v, delta_weights, parents_tree)
        for (vertex_u, vertex_v) in edges_list:
            if delta_weights[vertex_v] > delta_weights[vertex_u] + self.weights[(vertex_u, vertex_v)]:
                return tuple(("Failure", None, None))
        return tuple(("Success", delta_weights, parents_tree))

    def directed_acyclic(self, source_vertex):
        delta_weights = {}
        parents_tree = {}
        self.initialize_single_source(source_vertex, delta_weights, parents_tree)
        topological_sorted_list = self.topological_sorting()
        if topological_sorted_list[0] == "Failure":
            return tuple(("Failure", None, None))
        for vertex_u in topological_sorted_list[1]:
            for vertex_v in self.adjacency_list[vertex_u]:
                self.relax(vertex_u, vertex_v, delta_weights, parents_tree)
        return tuple(("Success", delta_weights, parents_tree))

    def relax(self, vertex_u, vertex_v, delta_weights, parents):
        if delta_weights[vertex_v] > delta_weights[vertex_u] + self.weights[(vertex_u, vertex_v)]:
            delta_weights[vertex_v] = delta_weights[vertex_u] + self.weights[(vertex_u, vertex_v)]
            parents[vertex_v] = vertex_u

    def initialize_single_source(self, source_vertex, delta_weights, parents_tree):
        for vertex in self.adjacency_list.keys():
            delta_weights[vertex] = maxsize
            parents_tree[vertex] = None
        delta_weights[source_vertex] = 0

    def get_edge_list(self):
        return [(vertex_v, vertex_u) for vertex_v in self.adjacency_list.keys() for vertex_u in
                self.adjacency_list[vertex_v]]

    def kruskal(self):
        forest = []
        disjoint_sets = DisjointSets()
        edges_list = sorted(self.get_edge_list(), key=lambda edge: self.weights[edge], reverse=False)
        for vertex in self.adjacency_list:
            disjoint_sets.make_set(vertex)
        for vertex_u,vertex_v in edges_list:
            if disjoint_sets.find(vertex_v) != disjoint_sets.find(vertex_u):
                forest.append((vertex_u, vertex_v))
                disjoint_sets.union(vertex_v, vertex_u)
        return tuple(forest)

    def prim(self):
        pass


class DisjointSets:
    parent = {}
    rank = {}

    def make_set(self, vertex):
        self.parent[vertex] = vertex
        self.rank[vertex] = 0

    def find(self, vertex):
        if self.parent[vertex] == vertex:
            return vertex
        return self.find(self.parent[vertex])

    def union(self, vertex_u, vertex_v):
        vertex_u_root = self.find(vertex_u)
        vertex_v_root = self.find(vertex_v)

        if self.rank[vertex_u_root] > self.rank[vertex_v_root]:
            self.parent[vertex_v_root] = vertex_u_root
        elif self.rank[vertex_u_root] < self.rank[vertex_v_root]:
            self.parent[vertex_u_root] = vertex_v_root
        else:
            self.parent[vertex_u_root] = vertex_v_root
            self.rank[vertex_v_root] += 1

