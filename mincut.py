import copy
import random
import math


class MinCut:
    """
    Compute the minimum cut of a connected graph using Karger's algorithm
    """

    def __init__(self, graph, iters=lambda n: int(n**2 * math.log(n))):
        """
        Compute the minimum cut for a given graph,
        with number of iterations defined by iters function
        """

        self._min_graph = None
        for i in range(iters(graph.count_vertices())):
            g = self._find_mincut(copy.deepcopy(graph))
            if self._is_better_cut(g):
                self._min_graph = g

    def _is_better_cut(self, graph):
        return self._min_graph is None or self._size(graph) < self.size()

    @staticmethod
    def _find_mincut(graph):
        while graph.count_vertices() > 2:
            # pick a random edge and contract
            u = random.choice(graph.vertices())
            v = random.choice(tuple(set(graph.edges(u))))
            graph.contract_edge(u, v)

        return graph

    def mincut(self):
        """
        Return the mincut
        """

        return self._min_graph.vertices()

    @staticmethod
    def _size(graph):
        return graph.count_edges(graph.vertices()[0])

    def size(self):
        """
        Return a number of edges for a computed mincut
        """

        return self._size(self._min_graph)
