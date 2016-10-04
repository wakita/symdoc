# symdoc
Document Synthesis Project Based on Symbolic Algebra System

JSSST 大会発表に関するプロジェクトです。

- [汎用 Newton-Raphson 法](https://github.com/wakita/symdoc/blob/master/newtonraphson-jp.ipynb)

- [力学モデルに基づいた無向グラフ可視化システム (Kamada-Kawai法)](https://github.com/wakita/symdoc/blob/master/kk.ipynb)


# 調整中

- ３次元グラフィクスのための空間変換ライブラリ (T3D)
- 無向グラフを対象とした対話的な超高次元可視化システム (AGI)

# 必要なソフトウェア

- Python 3 と以下のパッケージ
    - NumPy: the fundamental package for scientific computing with Python
    - SciPy: a Python-based ecosystem of open-source software for mathematics, science, and engineering
    - mpmath: Python library for real and complex floating-point arithmetic with arbitrary precision
    - SymPy開発版: a Python library for symbolic mathematic
    - Jupyter Notebook:  a web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text

## ソフトウェアの準備の方法

以下では、Anaconda の利用を仮定します。

1. SymPy 開発版を入手して、適当な場所に設置します。以下では /home/wakita/dist/sympy に保存するものとして説明します。

        ```
        cd /home/wakita/dist
        git clone https://github.com/sympy/sympy
        ```

    Git に不慣れなひとは、[配布元](https://github.com/sympy/sympy)から Zip ファイルをダウンロードして展開して下さい。

1. 仮想環境を作成します。

        conda create --name symdoc python=3

1. 作成した仮想環境を稼動します。

    Linux ユーザ と Mac ユーザは

        source activate symdoc (for other platforms)

    Windows ユーザは

        activate symdoc (for Windows users)

1. 仮想環境に（SymPy以外の）必要なパッケージをインストールします。

        conda install numpy scipy mpmath notebook

1. 展開した SymPy を Python3 が読み込めるように設定します。

    1. まず、Python を起動し、以下の要領でサイトの構造を調べます。

    ```
    ☁  symdoc  python
Python 3.5.2 |Continuum Analytics, Inc.| (default, Jul  2 2016, 17:52:12)
[GCC 4.2.1 Compatible Apple LLVM 4.2 (clang-425.0.28)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import site
>>> site.getusersitepackages()
'/Users/wakita/.local/lib/python3.5/site-packages'
```

        私の環境では、`/Users/wakita/.local/lib/python3.5/site-packages` だということがわかります。このディレクトリが存在しなかったら作成して下さい。

    1. 今、見つかったディレクトリに `symdoc.pth` という名前のテキストファイルを作成し、そこに `sympy` をインストールしたディレクトリパスを記載します。私の環境の場合は以下のようになります。

    `/home/wakita/dist/sympy`

## 実行の仕方

Anaconda の仮想環境を有効化し(`activate symdoc` あるいは `source activate symdoc`)、Jupyter を開始 (`jupyter notebook`) します。あとのことは Jupyter の入門サイトの情報を参考にしながら試してみて下さい。
