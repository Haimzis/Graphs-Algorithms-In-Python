from GraphAlgorithms import graph
import unittest


class TestGraph(unittest.TestCase):

    def setUp(self):
        graph_instance1 = (graph.Graph({'a': ['d', 'f', 'b'], 'b': ['c'], 'c': ['d', 'e'], 'd': [], 'e': [], 'f': []},
                                       {('a', 'b'): 1, ('a', 'd'): 15, ('a', 'f'): 2, ('b', 'c'): 5, ('c', 'd'): 10,
                                        ('c', 'e'): 5}),
                           {"topological_sorting": "Success",
                            "bfs": {'a': 0, 'b': 1, 'c': 2, 'd': 1, 'e': 3, 'f': 1},
                            "dijkstra": ("Success", {'a': 0, 'b': 1, 'c': 6, 'd': 15, 'e': 11, 'f': 2}, {'a': None, 'b': 'a', 'c': 'b', 'd': 'a', 'e': 'c', 'f': 'a'}),
                            "bellman_ford": ("Success", {'a': 0, 'b': 1, 'c': 6, 'd': 15, 'e': 11, 'f': 2}, {'a': None, 'b': 'a', 'c': 'b', 'd': 'a', 'e': 'c', 'f': 'a'}),
                            "directed_acyclic": ("Success", {'a': 0, 'b': 1, 'c': 6, 'd': 15, 'e': 11, 'f': 2}, {'a': None, 'b': 'a', 'c': 'b', 'd': 'a', 'e': 'c', 'f': 'a'})})
        graph_instance2 = (graph.Graph({'a': ['b', 'c'], 'b': ['a'], 'c': ['b']},
                                       {('a', 'b'): 8, ('a', 'c'): 5, ('b', 'a'): 3, ('c', 'b'): 2}),
                           {"topological_sorting": "Failure",
                            "bfs": {'a': 0, 'b': 1, 'c': 1},
                            "dijkstra": ("Success", {'a': 0, 'b': 7, 'c': 5}, {'a': None, 'b': 'c', 'c': 'a'}),
                            "bellman_ford": ("Success", {'a': 0, 'b': 7, 'c': 5}, {'a': None, 'b': 'c', 'c': 'a'}),
                            "directed_acyclic": ("Failure", None, None)})
        graph_instance3 = (graph.Graph({'a': ['b', 'c'], 'b': ['c', 'd'], 'c': ['d'], 'd': []},
                                       {('a', 'b'): 4, ('a', 'c'): -2, ('b', 'd'): 4, ('b', 'c'): -10, ('c', 'd'): -2}),
                           {"topological_sorting": "Success",
                            "bfs": {'a': 0, 'b': 1, 'c': 1, 'd': 2},
                            "dijkstra": ("Failure", None, None),
                            "bellman_ford": ("Success", {'a': 0, 'b': 4, 'c': -6, 'd': -8}, {'a': None, 'b': 'a', 'c': 'b', 'd': 'c'}),
                            "directed_acyclic": ("Success", {'a': 0, 'b': 4, 'c': -6, 'd': -8}, {'a': None, 'b': 'a', 'c': 'b', 'd': 'c'})})
        self.graph_examples = [graph_instance1, graph_instance2, graph_instance3]

    def test_shortest_path_algorithms(self):
        for graph_instance in self.graph_examples:
            self.assertEqual(graph_instance[0].bellman_ford('a'), graph_instance[1]["bellman_ford"])
            self.assertEqual(graph_instance[0].directed_acyclic('a'), graph_instance[1]["directed_acyclic"])
            self.assertEqual(graph_instance[0].dijkstra('a'), graph_instance[1]["dijkstra"])

    def test_topological_sorting(self):
        for graph_instance in self.graph_examples:
            self.assertEqual(graph_instance[0].topological_sorting()[0], graph_instance[1]['topological_sorting'])

    def test_scans(self):
        for graph_instance in self.graph_examples:
            self.assertEqual(graph_instance[0].bfs('a'), graph_instance[1]['bfs'])


if __name__ == "__main__":
    unittest.main()

