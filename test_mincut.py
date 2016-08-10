import unittest

from graph import Graph
from mincut import MinCut


class MinCutTest(unittest.TestCase):
    """
    0 -- 1
    |  / |
    | /  |
    2 -- 3 -- 4
    """
    data = [
        '0 1 2',
        '1 0 2 3',
        '2 0 1 3',
        '3 1 2 4',
        '4 3'
    ]

    def test_mincut(self):
        graph = Graph(self.data)
        mincut = MinCut(graph)

        self.assertEqual(mincut.mincut(), 1)

if __name__ == '__main__':
    unittest.main()
