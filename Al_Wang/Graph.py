#### build a graph
#### bfs and dfs
from typing import List
from collections import deque
class Graph:
    def __init__(self, num_vertices: int):
        self._num_vertices = num_vertices
        self._adjacency = [[] for _ in range(num_vertices)]

    def add_edge(self, s: int, t: int) -> None:
        self._adjacency[s].append(t)
        self._adjacency[t].append(s)

    def _generate_path(self, s: int, t: int, prev: List[int]) :
        if prev[t] or s != t:
            yield from self._generate_path(s, prev[t], prev)
        yield str(t)

    def bfs(self, s: int, t: int) :
        """Print out the path from Vertex s to Vertex t
        using bfs.
        """
        if s == t :
            return 
        visited = [False] * self._num_vertices
        prev  = [None] * self._num_vertices
        que = deque()
        visited[s] = True
        que.append(s)
        while que:
            v = que.popleft()
            for neighbor in self._adjacency[v]:
                if not visited[neighbor]:
                    prev[neighbor] = v
                    if neighbor == t:
                        return print("-->".join(self._generate_path(s,t,prev)))
                    visited[neighbor] = True
                    que.append(neighbor)





    def dfs(self, s:int, t:int):
        """Print out the path from Vertex s to Vertex t
        using dfs.
        """
        visited = [False] * self._num_vertices
        prev  = [None] * self._num_vertices
        found = False
        def dfs_1(v:int):
            nonlocal found
            if found == True:
                return 
            visited[v] = True
            if v == t:
                found = True
                return
            for neighbor in self._adjacency[v]:
                if not visited[neighbor]:
                    prev[neighbor] = v
                    dfs_1(neighbor)
        dfs_1(s)
        print("-->".join(self._generate_path(s,t,prev)))


graph = Graph(8)
graph.add_edge(0, 1)
graph.add_edge(0, 3)
graph.add_edge(1, 2)
graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(4, 6)
graph.add_edge(5, 7)
graph.add_edge(6, 7)

graph.bfs(0, 7)
graph.dfs(0, 7)
