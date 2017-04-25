NetworkXを使ったグラフアルゴリズムの実装
===========

ここからは適当にファイルを作成し、プログラムを作成します。
実行する際は以下のコマンドを実行します。

```sh
$ python sample.py
```

## 下準備

NetworkXを使うためにimport文を書きます。

ここでは、```as nx```としているので、今後```nx```でNetworkXを呼び出すことができます。

```python
import networkx as nx
```

## グラフの作成

グラフを作成するときは以下のように書きます。

```python
g = nx.Graph()
```

グラフに頂点や辺を追加するためには以下のように書きます。
辺を追加する際に頂点が無ければ、自動的に頂点も作成されます。

```python
g.add_node("n1")
g.add_edge("n2", "n3")
```

作成したグラフの頂点、辺の情報を取得するためには以下のように書きます。

```python
print(list(g.nodes()))
print(list(g.edges()))
```

最後にこのグラフを画像やGUIで見れるようにします。

```python
import pylab
nx.draw_circular(g, font_size = 40, node_size = 3500)
pylab.savefig("create_graph.png")
pylab.show()
```

ここまでのコードは[create_graph.py](src/create_graph.py)にまとめています。

NetworkXの[サンプル集](https://networkx.readthedocs.io/en/stable/examples/)を参考にしながら、何か作ってみましょう
