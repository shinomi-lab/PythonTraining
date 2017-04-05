開発の始め方
===========

## Ubuntu 14.04 LTSの人

Ubuntuにはもともとpythonが入ってます。
ただ、少し古い（python2系）ので新しいバージョンを入れます。

端末を開いて以下のコマンドを打ちます。

```sh
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install build-essential #基本的なライブラリのインストール
$ sudo apt-get install python3-dev #python3のインストール
$ python -V
$ python3 -V
Python 3.4.3
```

python3系のインストールが完了すれば次にpipをインストールします。
pipはpythonの各種ライブラリをインストールするときに便利なツールです。

```sh
$ sudo apt-get install python3-setuptools
$ sudo easy_install3 pip
```

最後にpipを用いてグラフアルゴリズムを実装するためのライブラリをインストールします。

```sh
$ sudo pip install networkx
```

これで必要なものは全てインストールできました。

動作確認のために簡単なグラフを作成して表示してみます。

下のコマンドを入力してグラフを作成します。
どのようなグラフを作成しているか考えながらコピーしてください。

```sh
$ python3
>>> import networkx as nx
>>> graph = nx.DiGraph()
>>> graph.add_node('hoge')
>>> graph.add_node('fuga')
>>> graph.add_node('bar')
>>> graph.add_edge('hoge', 'fuga')
>>> graph.add_edge('fuga', 'bar')
>>> graph.add_edge('bar', 'hoge')
>>> print(graph.nodes())
>>> print(graph.edges())
```

特にエラー無く実行できればセットアップは完了です。

## Macの人

WIP（brewとpip使えば簡単にインストールできるはず）

## Windowsの人

WIP

## その他の人

WIP
