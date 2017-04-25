# -*- coding: utf-8 -*-
# NetworkXの読み込み
import networkx as nx
# 画像データに出力するためのライブラリ
import pylab

# グラフの作成
g = nx.Graph()
g.add_node('n1') # 頂点の追加
g.add_edge('n2','n3') # 辺の追加

# グラフの出力(CUI)
print(list(g.nodes())) # ['n1', 'n2', 'n3']
print(list(g.edges())) # [('n2', 'n3')]

# グラフの出力(GUI)
nx.draw_circular(g, font_size = 40, node_size = 3500)
pylab.savefig("create_graph.png") # 画像保存
pylab.show() # windowに表示
