import queue


def dfs(graph):
    dfs_order = []
    colors = {vertex: "white" for vertex in graph.keys()}
    for vertex in graph.keys():
        if colors[vertex] == "white":
            visit(graph, vertex, colors, dfs_order)
    return tuple(dfs_order)


def visit(graph, vertex_u, colors, dfs_order):
    colors[vertex_u] = "gray"
    for adjacent in graph[vertex_u]:
        if colors[adjacent] == "white":
            visit(graph, adjacent, colors, dfs_order)
    colors[vertex_u] = "black"
    dfs_order.append(vertex_u)


def bfs(graph, start_vertex):
    delta_routes_length = {vertex: "infinite" for vertex in graph.keys()}
    vertexes_queue = queue.Queue()
    vertexes_queue.queue.append(start_vertex)
    delta_routes_length[start_vertex] = 0
    while not vertexes_queue.empty():
        vertex_u = vertexes_queue.queue.popleft()
        for adjacent in graph[vertex_u]:
            if delta_routes_length[adjacent] == "infinite":
                delta_routes_length[adjacent] = delta_routes_length[vertex_u] + 1
                vertexes_queue.queue.append(adjacent)
    return delta_routes_length


