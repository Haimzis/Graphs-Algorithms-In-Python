import queue


def topological_sorting(graph):
    top_sort = ()
    sources_queue = queue.Queue()
    in_degrees_counter = in_degrees(graph)
    for vertex, counter in in_degrees_counter.items():
        if counter == 0:
            sources_queue.queue.append(vertex)
    while not sources_queue.empty():
        vertex = sources_queue.queue.popleft()
        top_sort += (vertex,)
        for adjacent in graph[vertex]:
            in_degrees_counter[adjacent] -= 1
            if in_degrees_counter[adjacent] == 0:
                sources_queue.queue.append(adjacent)
    for vertex, counter in in_degrees_counter.items():
        if counter != 0:
            return tuple(("Failure", None))
    return tuple(("Success", top_sort))


def in_degrees(graph):
    in_degree_vertexes = {vertex: 0 for (vertex, adjacency_list) in graph.items()}
    for vertex in graph:
        for adjacent in graph[vertex]:
            in_degree_vertexes[adjacent] += 1
    return in_degree_vertexes
