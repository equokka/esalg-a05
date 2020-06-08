#!/usr/bin/env python

# Pretendemos que desenvolvas uma aplicação em Python para gerir uma rede global
# de agências de notícias. Duas agências estão diretamente ligadas se existe um
# canal de comunicação para enviarem e receberem notícias entre si.

# Deves adotar o paradigma orientado a objetos, considerando as classes
# RedeNoticias, AgenciaNoticias e Grafo, não obstante possas acrescentar mais
# classes. Para simplificar, podes considerar que cada agência de notícias é
# caracterizada pelo nome e pelo email.
# * [x] RedeNoticias
# * [x] AgenciaNoticias
# * [x] Grafo - Graph

# A aplicação deve disponibilizar as seguintes funcionalidades, através de um menu:

# * [x] F1 – Adicionar/remover uma agência de notícias.
# * [x] F2 - Adicionar/remover um canal de comunicação entre duas agências de
#            notícias.
# * [x] F3 - Mostrar no ecrã o estado da rede global de notícias.
# * [x] F4 – Obter as agências de notícias atingíveis através de uma travessia
#            em profundidade com início numa determinada agência de notícias.
# * [ ] F5 – Obter o caminho mais curto (menos vértices) entre duas agências de
#            notícias.
# * [ ] F6 – Obter as agências de notícias mais populares: a que pode comunicar
#            diretamente com mais agências e a que está mais próxima das
#            restantes agências da rede.

from noticias import RedeNoticias
from utils import get_option

rede = RedeNoticias()

# #  A---B---C
# #   \ /   /
# #    D---´   E---F---G
# rede.adicionar_agencia("A")
# rede.adicionar_agencia("B")
# rede.adicionar_agencia("C")
# rede.adicionar_agencia("D")
# rede.adicionar_agencia("E")
# rede.adicionar_agencia("F")
# rede.adicionar_agencia("G")
# print(rede.vertexes)
# rede.adicionar_canal_comunicacao("A", "B")
# rede.adicionar_canal_comunicacao("A", "D")
# rede.adicionar_canal_comunicacao("B", "C")
# rede.adicionar_canal_comunicacao("B", "D")
# rede.adicionar_canal_comunicacao("D", "C")
# rede.adicionar_canal_comunicacao("E", "F")
# rede.adicionar_canal_comunicacao("F", "G")

def hr():
  print("*" * 71)
  for i in rede.agencias:
    num = len(rede.travessia_profundidade_agencias(i))
    p = "ões" if num != 1 else "ão"
    print(f"{i} - {num} ligaç{p}")
  print("*" * 71)

while True:
  hr()
  print(" 1 – Adicionar ou remover agências e ligações entre agências.")
  print(" 2 – Obter as agências de notícias atingíveis através de uma travessia")
  print("     em profundidade com início numa determinada agência de notícias.")
  print(" 3 – Obter um caminho entre duas agências de notícias.")
  print(" 4 – Saír.")
  option = get_option(" > ", 4)
  if option == 1:
    while True:
      hr()
      print(" Agências:")
      print("   1 - Adicionar")
      print("   2 - Remover")
      print(" Ligações:")
      print("   3 - Adicionar")
      print("   4 - Remover")
      print(" 5 - Voltar a tráz")
      option = get_option(" > ", 5)
      if option in [1, 2]:
        agencia = input(" Nome da agência: ").strip()
        if option == 1:   rede.adicionar_agencia(agencia)
        elif option == 2: rede.remover_agencia(agencia)
      elif option in [3, 4]:
        agencia_a = input(" Nome da primeira agência: ").strip()
        agencia_b = input(" Nome da segunda agência:  ").strip()
        if option == 3: rede.adicionar_canal_comunicacao(agencia_a, agencia_b)
        if option == 4: rede.remover_canal_comunicacao(agencia_a, agencia_b)
      elif option == 5:
        break
  elif option == 2:
    hr()
    agencia = input(" Nome da agência: ").strip()
    a = rede.travessia_profundidade_agencias(agencia)
    print(" Agências atingidas:")
    for i in a: print(f" * {i}")
  elif option == 3:
    agencia_a = input(" Nome da primeira agência: ").strip()
    agencia_b = input(" Nome da última agência:   ").strip()
    p = rede.find_path(rede.agencias[agencia_a], rede.agencias[agencia_b])
    print(p)
  elif option == 4:
    break
