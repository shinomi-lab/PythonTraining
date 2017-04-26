# -*- coding: utf-8 -*-
import networkx as nx
import random

g = nx.Graph()
# g.add_node('n1')
# g.add_edge('n2', 'n3') # n2, n3は自動的に追加される
for i in range(10):
    g.add_node(i)
for i in range(10):
    g.add_edge(random.randint(0,9), random.randint(0,9))
print 'nodes', g.nodes()
print 'edges', g.edges()

p = nx.shortest_path(g, 0, 5)
print p
