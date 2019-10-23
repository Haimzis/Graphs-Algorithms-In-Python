from GraphAlgorithms import graph

if __name__ == '__main__':

    my_graph = graph.Graph({"a": ["d", "f", "b"], "b": ["c"], "c": ["d", "e"], "d": [], "e": [], "f": []},
                           {('a', 'b'): 1, ('a', 'd'): 15, ('a', 'f'): 2, ('b', 'c'): 5, ('c', 'd'): 10, ('c', 'e'): 5})
    print(my_graph.bfs('a'))
    print(my_graph.dfs())
    print(my_graph.topological_sorting())
    print(my_graph.dijkstra('a'))
    print(my_graph.directed_acyclic('a'))
    print(my_graph.bellman_ford('a'))
    print(my_graph.__str__())
