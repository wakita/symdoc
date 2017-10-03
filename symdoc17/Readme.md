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

- numpy: 基本的な行列計算

- matplotlib: グラフ生成

- scipy: 科学技術計算

- scipy: 数式処理

## 仮想環境の起動方法

`cmd.exe` を開き，`activate glvis`．これを実行しておけば，前述の仮想環境が利用できるようになる．

# `symdoc` の実行

- GNU make が利用できるのであれば `make` 一発．詳細は `Makefile` の内容を参照のこと．

- `t3d.html` をブラウザで開くとドキュメントが読める．
