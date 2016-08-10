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

        self.assertEqual(graph.v(), 0)

    def test_create_graph(self):
        graph = Graph(self.data)

        self.assertEqual(graph.v(), 4)
        self.assertCountEqual(graph.edges(), [(0, 1), (0, 2), (1, 2), (1, 3),
                                              (2, 3)])


if __name__ == '__main__':
    unittest.main()
