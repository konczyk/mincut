import random


class MinCut:
    """
    Compute the minimum cut of a connected graph using Karger's algorithm
    with edge contraction
    """

    def __init__(self, graph, runs=lambda n: 2*n):
        """
        Compute the minimum cut for a given graph,
        with number of iterations defined by runs function
        """

        self._graph = graph
        self._mincut = None

        for i in range(runs(graph.v())):
            cut = self._find_mincut()
            if self._mincut is None or self._mincut > cut:
                self._mincut = cut

    def _find_mincut(self):
        v = self._graph.v()
        edges = list(self._graph.edges())

        def pick():
            e = random.choice(edges)
            return e if e[0] != e[1] else pick()

        while v > 2:
            # pick a random edge and contract
            p, q = pick()
            # replace p--q connections with r--q ones
            for i in range(len(edges)):
                edge = edges[i]
                if p in edge:
                    r = edge[0] if edge[0] != p else edge[1]
                    edges[i] = r, q

            # remove self-loops (v--v)
            edges = [x for x in edges if x[0] != x[1]]

            v -= 1

        return len(edges)

    def mincut(self):
        """
        Return the mincut
        """

        return self._mincut
