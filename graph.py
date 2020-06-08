#!/usr/bin/env python

# adjacent(G, x, y): tests whether there is an edge from the vertex x to the vertex y;
# neighbors(G, x): lists all vertices y such that there is an edge from the vertex x to the vertex y;
# add_vertex(G, x): adds the vertex x, if it is not there;
# remove_vertex(G, x): removes the vertex x, if it is there;
# add_edge(G, x, y): adds the edge from the vertex x to the vertex y, if it is not there;
# remove_edge(G, x, y): removes the edge from the vertex x to the vertex y, if it is there;
# get_vertex_value(G, x): returns the value associated with the vertex x;
# set_vertex_value(G, x, v): sets the value associated with the vertex x to v.

from typing    import Any, Union, Dict, Set, Iterator, List
from uuid      import UUID, uuid4

# this is an UNDIRECTED graph. there are no "directions" for edges, they
# are bidirectional/directionless.

class Graph:
  def __init__(self):
    self.vertexes = {} # type: Dict[UUID, Any]
    self.edges = {} # type: Dict[UUID, Set[UUID]]

  def add_vertex(self, data: Any) -> str:
    _id = uuid4()
    self.vertexes[_id] = data
    self.edges[_id] = set()
    return _id

  def remove_vertex(self, _id: UUID) -> None:
    del self.vertexes[_id]
    del self.edges[_id]
    for key in self.edges.keys(): self.edges[key] -= { _id }

  def get_vertex(self, _id: UUID) -> Union[Any, None]:
    if self.vertex_exists(_id):
      return self.vertexes[_id]
    return None

  def vertex_exists(self, _id: UUID) -> bool:
    return _id in self.vertexes.keys()

  def add_edge(self, key_a: UUID, key_b: UUID) -> None:
    if self.vertex_exists(key_a) and self.vertex_exists(key_b):
      self.edges[key_a] |= { key_b }

  def edge_exists(self, key_a: UUID, key_b: UUID) -> bool:
    if self.vertex_exists(key_a) and self.vertex_exists(key_b):
      if key_b in self.edges[key_a] or key_a in self.edges[key_b]:
        return True
    return False

  def remove_edge(self, key_a: UUID, key_b: UUID) -> None:
    if self.edge_exists(key_a, key_b):
      self.edges[key_a] ^= { key_b }
      self.edges[key_b] ^= { key_a }

  def adjacent(self, vertex: UUID) -> Set[UUID]:
    o = set()
    o |= self.edges[vertex]
    for _k in filter(lambda k: vertex in self.edges[k], self.edges.keys()):
      o |= self.edges[_k]
    return o

  def traverse_depth_first(self, vertex: UUID, ignore: Set[UUID] = set()) -> Set[UUID]:
    # TODO fix this, it's not working correctly
    # Add the vertex we're traversing from
    explored = { vertex } # type: Set[UUID]

    # Add it to the ignored vertexes
    ignore |= explored

    # For all the vertexes adjacent to this one that are NOT to be ignored...
    for i in filter(lambda w: w not in ignore, self.adjacent(vertex)):
      # Add the vertexes found from traversing them while ignoring
      explored |= self.traverse_depth_first(i, ignore=ignore)

    return explored

  def find_path(self, v_a: UUID, v_b: UUID, path: List[UUID] = []) -> Union[None, List[UUID]]:
    # Add the starting point to the path
    path += [v_a]

    # If we've arrived at point B then return the path
    if v_a == v_b: return path

    # If the vertex doesn't exist return None
    if v_a not in self.vertexes: return None

    # For every vertex adjacent to A that isn't in the path already,
    for wwwww in filter(lambda v: v not in path, self.adjacent(v_a)):
      # Make a new path from that vertex to B, carrying the current path.
      new_path = self.find_path(wwwww, v_b, path)
      # If we get a path back, return it.
      if new_path != None: return new_path

    # Otherwise,
    return None

  # def find_shortest_path(self, v_a: UUID, v_b: UUID, ) -> Union[None, List[UUID]]:
  # TODO

  # Bellman-Ford algorithm ?
  # https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm


# ------

# graph = Graph()

# #  A---B---C
# #   \ /   /
# #    D---´   E---F---G

# a = graph.add_vertex("A")
# b = graph.add_vertex("B")
# c = graph.add_vertex("C")
# d = graph.add_vertex("D")
# e = graph.add_vertex("E")
# f = graph.add_vertex("F")
# g = graph.add_vertex("G")
# graph.add_edge(a, b)
# graph.add_edge(a, d)
# graph.add_edge(b, c)
# graph.add_edge(b, d)
# graph.add_edge(d, c)
# graph.add_edge(e, f)
# graph.add_edge(f, g)

# print(f" a - {a}")
# print(f" b - {b}")
# print(f" c - {c}")
# print(f" d - {d}")
# print(f" e - {e}")
# print(f" f - {f}")
# print(f" g - {g}")

# # print(graph.vertexes)
# # print(graph.edges)

# # print(graph.traverse_depth_first(e))
# # print(graph.traverse_depth_first(a))
# print(graph.find_path(a, c))

