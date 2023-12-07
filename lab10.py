class EdgeSet:
    def __init__(self, V , E):
        self._V = set()
        self._E = set()
        for v in V:
            self.add_vertex(v)
        for e in E:
            self.add_edge(e)

    def Testing(self):
        return self._V, self._E,

    def add_vertex(self, v):
        self._V.add(v)

    def remove_vertex(self, v):
        if v not in self._V:
            raise KeyError(f"Vertex {v} not in graph")
        self._V.remove(v)
        self._E = {(u, w) for (u, w) in self._E if u != v and w != v}

    def add_edge(self, e):
        u, v = e
        if u not in self._V or v not in self._V:
            raise KeyError(f"Vertices {e} must be in the graph")
        self._E.add(e)

    def remove_edge(self, e):
        if e not in self._E:
            raise KeyError(f"Edge {e} not in graph")
        self._E.remove(e)

    def _neighbors(self, v):
        return {w for (u, w) in self._E if u == v}


class AdjacencySet:
    def __init__(self, V, E):
        self._V = set()
        self._neighbors = ()
        for v in V:
            self.add_vertex(v)
        for e in E:
            self.add_edge(e)

    def Testing(self):
        return self._V, self._neighbors


    def add_vertex(self, v):
        self._V.add(v)
        self._neighbors[v] = set()

    def remove_vertex(self, v):
        if v not in self._V:
            raise KeyError(f"Vertex {v} not in graph")
        del self._neighbors[v]
        self._V.remove(v)
        for u in self._V:
            self._neighbors[u] = {w for w in self._neighbors[u] if w != v}


    def add_edge(self, w):
        u, v = w
        if u not in self._V or v not in self._V:
            raise KeyError(f"Vertices {w} must be in the graph")
        self._neighbors[u].add(v)

    def remove_edge(self, w):
        u, v = w
        if u not in self._V or v not in self._V:
            raise KeyError(f"Vertices {w} must be in the graph")
        if v in self._neighbors[u]:
            self._neighbors[u].remove(v)

class Graph_ES(EdgeSet):
    def __init__(self, vv, ee):
        super().__init__(vv, ee)

    def vertices(self):
        return iter(self._V)

    def edges(self):
        return iter(self._E)

    def __contains__(self, v):
        return v in self._V

    def __len__(self):
        return len(self._V)

class Graph_AS(AdjacencySet):
    def __init__(self, vv, ee):
        super().__init__(vv, ee)

    def vertices(self):
        return iter(self._V)

    def edges(self):
        for u in self._V:
            for v in self._neighbors[u]:
                yield (u, v)

    def __contains__(self, v):
        return v in self._V

    def __len__(self):
        return len(self._V)



if __name__ == '__main__':
    # Store the following graph:
    #   1--4--5
    #   |\ | /|
    #   | \|/ |
    #   2--3--6

    vs = {1,2,3,4,5,6}
    es = {(1,2), (1,3), (1,4),               # 1s neighbors: {2, 3, 4}
          (2,1), (2,3),                      # 2s neighbors: {1, 3}
          (3,1), (3,2), (3,4), (3,5), (3,6), # 3s neighbors: {1, 2, 4, 5, 6}
          (4,1), (4,3), (4,5),               # 4s neighbors: {1, 3, 5}
          (5,3), (5,4), (5,6),               # 5s neighbors: {3, 4, 6}
          (6,3), (6,5)}                      # 6s neighbors: {3, 5}

    ########### EdgeSet #############
    print("************ EDGESET TESTS ************ ")
    f = Graph_ES(vs, es)
    #print(f.Testing())
    print("Checking neighbors Test: ", end="")
    assert (f._neighbors(5) == {3, 4, 6})
    assert (f._neighbors(3) == {1, 2, 4, 5, 6})
    print("PASSED!")

    print("Adding vertex Test: ", end="")
    f.add_vertex("A")
    f.add_edge(("A", 5))
    assert(f._neighbors("A") == {5})
    print("PASSED!")


    f.remove_edge(("A", 5))
    print("Removing non-existing edge Test: ", end="")
    try:
        f.remove_edge(("A", 5))
    except KeyError:
        print("PASSED!")

    ########### AdjacencySet #############
    print()
    print("************ ADJACENCYSET TESTS ************ ")
    g = Graph_AS(vs, es)
    #print(g.Testing())

    print("Checking vertices Test: ", end="")
    assert (g._V == {1, 2, 3, 4, 5, 6})
    print("PASSED!")

    print("Checking neighbors Test: ", end="")
    assert (g._neighbors[4] == {1, 3, 5})
    print("PASSED!")

    print("Newly added vertex with edges Test: ", end="")
    g.add_vertex(10)
    for e in range (2,4):
        g.add_edge((10, e))

    assert (g._neighbors[10] == {2, 3})
    print("PASSED!")

    print("Removing edge Test: ", end="")
    g.remove_edge((5,6))
    g.remove_edge((6,5))
    assert (g._neighbors[5] == {3, 4})
    assert (g._neighbors[6] == {3})
    print("PASSED!")
