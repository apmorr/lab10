class EdgeSet:
    def __init__(self, V = None, E = None):
        self._V = set()
        self._E = set()
        for v in V:
            self.add_vertex(v)
        for e in E:
            self.add_edge(*e)

    def add_vertex(self, v):
        pass

    def remove_vertex(self, v):
        pass

    def add_edge(self, e):
        pass

    def remove_edge(self, e):
        pass

    def neighbors(self, v):
        return {w for (u, w) in self._E if u == v}


class AdjacencySet:
    def __init__(self, V = None, E = None):
        pass

    def add_vertex(self, v):
        pass

    def remove_vertex(self, v):
        pass

    def add_edge(self, e):
        pass

    def remove_edge(self, e):
        pass

class Graph_ES(EdgeSet):
    def __init__(self, vv, ee):
        super().__init__(vv, ee)

class Graph_AS(AdjacencySet):
    pass


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
    print("Checking neighbors Test: ", end="")
    assert (f.neighbors(5) == {3, 4, 6})
    assert (f.neighbors(3) == {1, 2, 4, 5, 6})
    print("PASSED!")

    print("Adding vertex Test: ", end="")
    f.add_vertex("A")
    f.add_edge(("A", 5))
    assert(f.neighbors("A") == {5})
    print("PASSED!")


    # f.remove_edge(("A", 6))
    print("Removing non-existing edge Test: ", end="")
    try:
        f.remove_edge(("A", 6))
    except KeyError:
        print("PASSED!")

    ########### AdjacencySet #############
    print()
    print("************ ADJACENCYSET TESTS ************ ")
    g = Graph_AS(vs, es)

    print("Checking vertices Test: ", end="")
    assert (g.V == {1, 2, 3, 4, 5, 6})
    print("PASSED!")

    print("Checking neighbors Test: ", end="")
    assert (g.nbrs[4] == {1, 3, 5})
    print("PASSED!")

    print("Newly added vertex with edges Test: ", end="")
    g.add_vertex(10)
    for e in range (2,4):
        g.add_edge((10, e))

    assert (g.nbrs[10] == {2, 3})
    print("PASSED!")

    print("Removing edge Test: ", end="")
    g.remove_edge((5,6))
    g.remove_edge((6,5))
    assert (g.nbrs[5] == {3, 4})
    assert (g.nbrs[6] == {3})
    print("PASSED!")
