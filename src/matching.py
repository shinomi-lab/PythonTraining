import networkx as nx
import pylab
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite
# グラフの生成
g = nx.Graph()
# ノードの追加
g.add_nodes_from(list("abcdef"))
# エッジの追加
g.add_edge('a', 'd')
g.add_edge('a', 'e')
g.add_edge('b', 'e')
g.add_edge('c', 'e')
g.add_edge('c', 'f')
# 二部グラフであるか判定
print(nx.is_bipartite(g))
# グラフを二部に分けてleft,rightに代入
left, right = bipartite.sets(g)
# 最大マッチングを求める
matching = nx.bipartite.maximum_matching(g)
print(matching)

# 表示
# pip install matplotlib
# とimport matplotlib.pyplot as pltが必要
pos = nx.circular_layout(g)
nx.draw_networkx_nodes(g,pos,nodelist=g.nodes())
nx.draw_networkx_edges(g,pos,edgelist=g.edges())
nx.draw_networkx_edges(g,pos,edgelist=[(n,matching[n]) for n in left], edge_color='r')
nx.draw_networkx_nodes(g,pos,nodelist=right,node_color='b')
nx.draw_networkx_labels(g,pos,font_size=10)
plt.axis('off')
plt.show()