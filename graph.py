from collections import defaultdict


class Graph:
    """
    Undirected graph data structure
    """

    def __init__(self, data):
        self._graph = {}
        self._load_data(data)

    def _load_data(self, data):
        """
        Load connections from the input (e.g. stdin), where each row represents
        an adjacency list with the vertex in the first column
        Parallel edges are allowed, so adjacency list may contain duplicates
        """

        for line in data:
            row = [int(i) for i in line.split()]
            self._graph[row[0]] = row[1:]

    def contract_edge(self, u, v):
        """
        Contract an edge represented by the passed vertices by fusing u with v
        """

        # remove v -- > u connections
        while u in self._graph[v]:
            self._graph[v].remove(u)

        # add u edges to v (except for v - no self loops)
        self._graph[v] += [x for x in self._graph[u] if x != v]

        # add v to all vertices connected to u and remove their connections to u
        for w in self._graph[u]:
            if w != v:
                while u in self._graph[w]:
                    self._graph[w].remove(u)
                self._graph[w].append(v)

        del self._graph[u]

    def vertices(self):
        """
        Return a list of graph vertices
        """

        return list(self._graph.keys())

    def count_vertices(self):
        """
        Return the number of vertices in the graph
        """

        return len(self._graph)

    def edges(self, u):
        """
        Return a list of edges connected to a given vertex u
        """

        return self._graph[u]

    def count_edges(self, u):
        """
        Return a number of edges connected to a given vertex u
        """

        return len(self.edges(u))

