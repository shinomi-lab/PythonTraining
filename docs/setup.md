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
ページ下部にある動作確認へ。

## Macの人

- homebrewのインストール（既に入っている方は飛ばしてください。）
```sh
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

- pyenvのインストール（pythonのバージョン管理ツール）
```sh
$ brew install pyenv
```

- パスの設定
```sh
$ export PYENV_ROOT="$HOME/.pyenv"
$ export PATH="$PYENV_ROOT/bin:$PATH"
$ eval "$(pyenv init -)"
```

- pyenvでインストールできるバージョンを確認
```sh
$ pyenv install --list
```

- Python 3.6.5のインストールし、使うバージョンとして設定確認
```sh
$ pyenv install 3.6.5
$ pyenv global 3.6.5
$ python --version
Python 3.6.5
```

- パッケージ管理ツールのpipをインストール。
```sh
$ easy_install pip
```

- NetWorkXのインストール
```sh
$ pip install networkx
```

これでMacでのインストールは完了です。ページ下部にある動作確認へ。

参考サイト：https://qiita.com/spyc/items/73d1295f8b3dde3b49ca

## Windows(64bit)の人
- [Miniconda](https://conda.io/miniconda.html)のPython 3.6 Windows 64bitのインストーラのダウンロード

- インストーラを起動しインストール
 - Add Anaconda to my PATH environment variableにチェック

- Pythonのバージョンの確認
```sh
$ python --version
```

- コマンドプロンプトを開き、condaからNetworkXのインストール
```sh
$ conda install networkx
```

これでWindowsでのインストールは完了です。ページ下部にある動作確認へ。

## 動作確認
動作確認のために簡単なグラフを作成して表示してみます。

下のコマンドを入力してグラフを作成します。
どのようなグラフを作成しているか考えながらコピーしてください。

```sh
$ python
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
