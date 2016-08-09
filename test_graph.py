import unittest
from graph import Graph


class GraphTest(unittest.TestCase):
    """
    0 -- 1
    |  / |
    | /  |
    2 -- 3
    """
    data = [
        '0 1 2',
        '1 0 2 3',
        '2 0 1 3',
        '3 1 2'
    ]

    def test_empty(self):
        graph = Graph([])

        self.assertEqual(graph.count_vertices(), 0)

    def test_create_graph(self):
        graph = Graph(self.data)

        self.assertEqual(graph.count_vertices(), 4)

    def test_contract_edge(self):
        graph = Graph(self.data)

        graph.contract_edge(0, 2)

        self.assertEqual(graph.count_vertices(), 3)
        self.assertEqual(graph.count_edges(2), 3)
        self.assertEqual(graph.count_edges(1), 3)

    def test_min_cut(self):
        graph = Graph(self.data)

        graph.contract_edge(0, 2)
        graph.contract_edge(1, 2)

        self.assertListEqual(sorted(graph.vertices()), sorted([3, 2]))
        self.assertEqual(graph.count_edges(2), 2)
        self.assertEqual(graph.count_edges(3), 2)


if __name__ == '__main__':
    unittest.main()
