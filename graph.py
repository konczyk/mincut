class Graph:
    """
    Undirected graph data structure represented as a list of edges
    and a number of vertices
    """

    def __init__(self, data):
        self._v = 0
        self._edges = []
        self._load_data(data)

    def _load_data(self, data):
        """
        Load connections from the data, where each row represents an adjacency
        list with the vertex in the first column and no parallel edges
        """

        e = set()
        for line in data:
            row = [int(i) for i in line.split()]
            e.update(tuple(sorted((row[0], x))) for x in row[1:])
            self._v += 1

        self._edges = list(e)

    def v(self):
        """
        Return the number of vertices in the graph
        """

        return self._v

    def edges(self):
        """
        Return a list of edges
        """

        return self._edges
