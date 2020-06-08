from graph import Graph

class AgenciaNoticias:
  def __init__(self, name: str):
    self.name = name
  def __str__(self) -> str: return f"<{self.name}>"
  def __repr__(self) -> str: return str(self)

class RedeNoticias(Graph):
  def __init__(self):
    super().__init__()
    self.agencias = {} # type: Dict[str, UUID]

  def adicionar_agencia(self, name: str) -> None:
    self.agencias[name] = self.add_vertex(AgenciaNoticias(name))
  def remover_agencia(self, name: str) -> None:
    self.remove_vertex(self.agencias[name])
    del self.agencias[name]

  def adicionar_canal_comunicacao(self, a_1: str, a_2: str) -> None:
    self.add_edge(self.agencias[a_1], self.agencias[a_2])
  def remover_canal_comunicacao(self, a_1: str, a_2: str) -> None:
    self.remove_edge(self.agencias[a_1], self.agencias[a_2])

  def travessia_profundidade_agencias(self, a: str):
    t = self.traverse_depth_first(self.agencias[a])
    t = set(map(lambda x: self.vertexes[x], t))
    return t
