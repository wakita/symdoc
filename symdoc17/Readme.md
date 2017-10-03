# Pandoc

Windows 版はインストールしたことがないけど，↓ でいけるらしい．

https://github.com/jgm/pandoc/releases/tag/1.19.2.1

# Git for Windows

Git for Windows はデフォルトで `c:\Program Files\Git` にインストールされる。

基本的にはMinGWのような気がする。`Win-s "git bash"`を起動すると`/usr/bin/`のさまざまなUNIXコマンドが利用できるようになる。`git`や`ssh`もそれらの一部だと思えばよさそう。これがあれば、Win10 Anniversary editionはあまりいらなさそう。

便利だと思ったら`Git Bash`をスタートメニューとかタスクメニューに保存するとよい。

# Anaconda3 の設定

Anaconda3を本家からダウンロードしてインストール。

## Anaconda の仮想環境 (`glvis`) の作成

`glvis` という名前の Python 3 の環境を作成し，主要なライブラリをインストールする．

`cmd.exe`を開き、以下を実行

~~~
conda create --name glvis python=3
activate glvis
conda install numpy matplotlib scipy sympy
~~~

- [numpy: 基本的な行列計算](https://docs.scipy.org/doc/numpy/reference/)

- matplotlib: グラフ生成

- scipy: 科学技術計算

- [sympy: 数式処理](http://docs.sympy.org/latest/): バージョンによって機能が異なるので，Google検索してドキュメントを見つけたときは，バージョンが最新版なことを確認して下さい．

- [Scipy Lecture Notes](http://www.scipy-lectures.org/): Python で科学技術計算をするためのチュートリアル集．非常にうまくまとまっているので，研究室に所属する人には最初に学んでもらっている．

    - [Sympy](http://www.scipy-lectures.org/packages/sympy.html): SymDoc に必須

    - [数理最適化 --- 関数の最小化](http://www.scipy-lectures.org/advanced/mathematical_optimization/index.html)

        Newton法が含まれています．

    - [NumPyの基礎](http://www.scipy-lectures.org/intro/numpy/index.html)

        行列計算

    - [Matplotlibの基礎](http://www.scipy-lectures.org/intro/matplotlib/index.html)

        グラフ描画

    - [Scipyの基礎](http://www.scipy-lectures.org/intro/scipy.html)

        科学技術計算

## 仮想環境の起動方法

`cmd.exe` を開き，`activate glvis`．これを実行しておけば，前述の仮想環境が利用できるようになる．

# `symdoc` の実行

- GNU make が利用できるのであれば `make` 一発．詳細は `Makefile` の内容を参照のこと．

- `t3d.html` をブラウザで開くとドキュメントが読める．
