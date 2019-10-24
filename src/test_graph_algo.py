from GraphAlgorithms import graph
import unittest


class TestGraph(unittest.TestCase):

    def __init__(self):
        super(TestGraph, self).__init__()
        graph_instance1 = (graph.Graph({"a": ["d", "f", "b"], "b": ["c"], "c": ["d", "e"], "d": [], "e": [], "f": []},
                                       {('a', 'b'): 1, ('a', 'd'): 15, ('a', 'f'): 2, ('b', 'c'): 5, ('c', 'd'): 10,
                                        ('c', 'e'): 5}),
                           {"topological_sorting": (),
                            "bfs": (),
                            "dijkstra": (),
                            "bellman_ford": (),
                            "directed_acyclic": ()})
        graph_instance2 = (graph.Graph({"a": ["b", "c"], "b": ["a"], "c": ["b"]},
                                       {('a', 'b'): 8, ('a', 'c'): 5, ('b', 'a'): 3, ('c', 'b'): 2}),
                           {"topological_sorting": (),
                            "bfs": (),
                            "dijkstra": (),
                            "bellman_ford": (),
                            "directed_acyclic": ()})
        graph_instance3 = (graph.Graph({"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": []},
                                       {('a', 'b'): 4, ('a', 'c'): -2, ('b', 'd'): 4, ('b', 'c'): -10, ('c', 'd'): -2}),
                           {"topological_sorting": (),
                            "bfs": (),
                            "dijkstra": (),
                            "bellman_ford": (),
                            "directed_acyclic": ()})
        self.graph_examples = [graph_instance1, graph_instance2, graph_instance3]

    def test_shortest_path_algorithms(self):
        for graph_instance in self.graph_examples:
            self.assertEquals(graph_instance[0].dijkstra('a'), graph_instance[1]['dijkstra'])
            self.assertEquals(graph_instance[0].bellman_ford('a'), graph_instance[1]['bellman_ford'])
            self.assertEquals(graph_instance[0].directed_acyclic('a'), graph_instance[1]['directed_acyclic'])

    def test_topological_sorting(self):
        for graph_instance in self.graph_examples:
            self.assertEquals(graph_instance[0].topological_sorting(), graph_instance[1]['topological_sorting'])

    def test_scans(self):
        for graph_instance in self.graph_examples:
            self.assertEquals(graph_instance[0].bfs('a'), graph_instance[1]['bfs'])


if __name__ == '__main__':
    unittest.main()
