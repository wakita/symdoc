---
title: T3D (Transform 3D) for Python
layout: page
---



# 同次座標系 (Homogeneous coordinate system)

三次元デカルト座標系(*Cartesian coordinate system*)における点の座標の**同次座標**(*Homogeneous coordinate*)は，任意の非零実数$w$を用いて変換されます。

$$Homogeneous\left(\left(\begin{matrix}x & y & z\end{matrix}\right), w\right) = \left(\begin{matrix}w x & w y & w z & w\end{matrix}\right)$$

同次座標を用いた座標系のことを**同次座標系**(*Homogeneous coordinate system*)と呼びます．

逆に，同次座標をデカルト座標に変換することもできます。

$$Cartesian\left(\left(\begin{matrix}w x & w y & w z & w\end{matrix}\right)\right) = \left(\begin{matrix}x & y & z\end{matrix}\right)$$

# モデル変換

## 回転変換: $\operatorname{Rotate_{X}}{\left (\theta \right )}, \operatorname{Rotate_{Y}}{\left (\theta \right )}, \operatorname{Rotate_{Z}}{\left (\theta \right )}$


- 回転変換行列 ($\operatorname{Rotate_{X}}{\left (\theta \right )}$) に同次座標を乗ずると，その座標を$X$軸のまわりに$\theta$だけ回転した点の同次座標を与えます．

    $$\operatorname{Rotate_{X}}{\left (\theta \right )} \left(\begin{matrix}w x\\w y\\w z\\w\end{matrix}\right) = \left(\begin{matrix}1 & 0 & 0 & 0\\0 & \cos{\left (\theta \right )} & \sin{\left (\theta \right )} & 0\\0 & - \sin{\left (\theta \right )} & \cos{\left (\theta \right )} & 0\\0 & 0 & 0 & 1\end{matrix}\right) \left(\begin{matrix}w x\\w y\\w z\\w\end{matrix}\right) = \left(\begin{matrix}w x\\w y \cos{\left (\theta \right )} + w z \sin{\left (\theta \right )}\\- w y \sin{\left (\theta \right )} + w z \cos{\left (\theta \right )}\\w\end{matrix}\right)$$


- 回転変換行列 ($\operatorname{Rotate_{Y}}{\left (\theta \right )}$) に同次座標を乗ずると，その座標を$Y$軸のまわりに$\theta$だけ回転した点の同次座標を与えます．

    $$\operatorname{Rotate_{Y}}{\left (\theta \right )} \left(\begin{matrix}w x\\w y\\w z\\w\end{matrix}\right) = \left(\begin{matrix}\cos{\left (\theta \right )} & 0 & - \sin{\left (\theta \right )} & 0\\0 & 1 & 0 & 0\\\sin{\left (\theta \right )} & 0 & \cos{\left (\theta \right )} & 0\\0 & 0 & 0 & 1\end{matrix}\right) \left(\begin{matrix}w x\\w y\\w z\\w\end{matrix}\right) = \left(\begin{matrix}w x \cos{\left (\theta \right )} - w z \sin{\left (\theta \right )}\\w y\\w x \sin{\left (\theta \right )} + w z \cos{\left (\theta \right )}\\w\end{matrix}\right)$$


- 回転変換行列 ($\operatorname{Rotate_{Z}}{\left (\theta \right )}$) に同次座標を乗ずると，その座標を$Z$軸のまわりに$\theta$だけ回転した点の同次座標を与えます．

    $$\operatorname{Rotate_{Z}}{\left (\theta \right )} \left(\begin{matrix}w x\\w y\\w z\\w\end{matrix}\right) = \left(\begin{matrix}\cos{\left (\theta \right )} & \sin{\left (\theta \right )} & 0 & 0\\- \sin{\left (\theta \right )} & \cos{\left (\theta \right )} & 0 & 0\\0 & 0 & 1 & 0\\0 & 0 & 0 & 1\end{matrix}\right) \left(\begin{matrix}w x\\w y\\w z\\w\end{matrix}\right) = \left(\begin{matrix}w x \cos{\left (\theta \right )} + w y \sin{\left (\theta \right )}\\- w x \sin{\left (\theta \right )} + w y \cos{\left (\theta \right )}\\w z\\w\end{matrix}\right)$$


-----

では、ここで得られた変換$\operatorname{Rotate_{X}}{\left (\theta \right )}$が確かに回転であることを確認してみましょう。この変換で点$\mathbf{p_1}$が$\mathbf{p_2}$に移ったものとします：

\begin{align}
\mathbf{p_1}^T &= \left(\begin{matrix}x & y & z\end{matrix}\right) \\
\mathbf{p_2}^T &= (\operatorname{Rotate_{X}}{\left (\theta \right )} \mathbf{p_1})^T \\
       &= \left(\left(\begin{matrix}1 & 0 & 0 & 0\\0 & \cos{\left (\theta \right )} & \sin{\left (\theta \right )} & 0\\0 & - \sin{\left (\theta \right )} & \cos{\left (\theta \right )} & 0\\0 & 0 & 0 & 1\end{matrix}\right)\left(\begin{matrix}x\\y\\z\end{matrix}\right)\right)^T \\
       &= \left(\begin{matrix}x & y \cos{\left (\theta \right )} + z \sin{\left (\theta \right )} & - y \sin{\left (\theta \right )} + z \cos{\left (\theta \right )}\end{matrix}\right)
\end{align}

1. 変換前後でベクトルと原点の距離は変化しないこと


    \begin{align}
    \|\mathbf{p_1}\|^2 &= \left\|\left(\begin{matrix}x & y & z\end{matrix}\right)^T\right\|^2 = x^{2} + y^{2} + z^{2} \\
    \|\mathbf{p_2}\|^2 &= \left\|\left(\begin{matrix}x & y \cos{\left (\theta \right )} + z \sin{\left (\theta \right )} & - y \sin{\left (\theta \right )} + z \cos{\left (\theta \right )}\end{matrix}\right)^T\right\|^2 \\
    &= x^{2} + y^{2} + z^{2}
    \end{align}

1. 変換前後のベクトルの差分が回転軸となるX軸と直交すること


    $\mathbf{p_1}$をX軸を中心として回転するとき、回転のあいだ$\mathbf{p_1}$はX軸と直交する平面を移動します。したがって、移動後の$\mathbf{p_2}$もそのX軸と直交する平面にあるはずです。$\mathbf{p_1}, \mathbf{p_2}$がともにX軸と直交する平面上の点ということは、$(\mathbf{p_2} - \mathbf{p_1})$はこの平面上のベクトルということになるので、X軸と直交するはずです。

    $$
    (\mathbf{p_2} - \mathbf{p_1}, \mathbf{e_x}) = \left(\left(\begin{matrix}x\\y\\z\end{matrix}\right) - \left(\begin{matrix}x\\y \cos{\left (\theta \right )} + z \sin{\left (\theta \right )}\\- y \sin{\left (\theta \right )} + z \cos{\left (\theta \right )}\end{matrix}\right), \left(\begin{matrix}1\\0\\0\end{matrix}\right)\right) = 0
    $$

    内積が0なので直交していることが確認できました。

1. 回転角が$\theta$であること


    X軸を中心として$p$を$\theta$回転して$p'$に移すということは、$p$と$p'$のなす角度が$\theta$というような気もしますが、実はそうではありません。ベクトル$p$は円錐の表面を撫でるようにして$p'$に写るからです。$\theta$となるのは、$p$からX軸への垂線の足となる$\mathbf{p_0}$について$p$と$p'$がなす角度です。

    では、まず$\mathbf{p_0}$を求めてみましょう。これをベクトルだと思うとX軸方向の単位ベクトル$\mathbf{e_x}^T$と同じ向きで、長さが前述の垂線の足にあたる点と原点の距離です。この距離は$p^T$と$\mathbf{e_x}^T$の内積で与えられますので、結局$\mathbf{p_0}^T = (\mathbf{p_1}^T, \mathbf{e_x}^T) \mathbf{e_x}^T = \left(\begin{matrix}x\\0\\0\end{matrix}\right)^T$となります。

    角度が$\theta$であることは($\mathbf{p_1}-\mathbf{p_0}$)と($\mathbf{p_2}-\mathbf{p_0}$)の内積に関する性質について確認すればよいでしょう。

    \begin{align}
    ((p - p_x)^T, (p' - p_x)^T) &= (\left(\begin{matrix}0 & y & z\end{matrix}\right), \left(\begin{matrix}0 & y \cos{\left (\theta \right )} + z \sin{\left (\theta \right )} & - y \sin{\left (\theta \right )} + z \cos{\left (\theta \right )}\end{matrix}\right)) \\
        &= y \left(y \cos{\left (\theta \right )} + z \sin{\left (\theta \right )}\right) + z \left(- y \sin{\left (\theta \right )} + z \cos{\left (\theta \right )}\right) \\
        &= \left(y^{2} + z^{2}\right) \cos{\left (\theta \right )}
    \end{align}

    一方、$p-p_x$と$p'-p_x$のなす角が\thetaならば、その内積は$\ell_1 \ell_2 \cos{\left (\theta \right )}$になるはずです。

    \begin{align}
    \ell_1 &= \|p - p_x\| = \sqrt{y^{2} + z^{2}} \\
    \ell_2 &= \|p' - p_x\| = \sqrt{y^{2} + z^{2}} \\
    \ell_1 \ell_2 \cos{\left (\theta \right )} &= \sqrt{y^{2} + z^{2}} \sqrt{y^{2} + z^{2}} \cos{\left (\theta \right )} = \left(y^{2} + z^{2}\right) \cos{\left (\theta \right )}
    \end{align}

    以上より$((p-p_x)^T, (p'-p_x)^T) = \ell_1 \ell_2 \cos{\left (\theta \right )}$が確認できました。

## 並行移動変換: $\operatorname{Translate}{\left (t_{x},t_{y},t_{z} \right )}$

以下の行列 $\operatorname{Translate}{\left (t_{x},t_{y},t_{z} \right )}$ に同次座標を乗じたものは，デカルト座標を$(t_{x}, t_{y}, t_{z})$だけ平行移動したものの同次座標を与えます．

ここで平行移動を表す行列$\operatorname{Translate}{\left (t_{x},t_{y},t_{z} \right )}$は以下で与えられます．

$$ \operatorname{Translate}{\left (t_{x},t_{y},t_{z} \right )} = \left(\begin{matrix}1 & 0 & 0 & t_{x}\\0 & 1 & 0 & t_{y}\\0 & 0 & 1 & t_{z}\\0 & 0 & 0 & 1\end{matrix}\right) $$

では，本当に平行移動になっているか確認してみましょう．

\begin{align}
\operatorname{Translate}{\left (t_{x},t_{y},t_{z} \right )}Homogeneous\left(\left(\begin{matrix}x\\y\\z\end{matrix}\right)\right)
    &= \left(\begin{matrix}1 & 0 & 0 & t_{x}\\0 & 1 & 0 & t_{y}\\0 & 0 & 1 & t_{z}\\0 & 0 & 0 & 1\end{matrix}\right) \left(\begin{matrix}w x\\w y\\w z\\w\end{matrix}\right) \\
    &= \left(\begin{matrix}w \left(t_{x} + x\right)\\w \left(t_{y} + y\right)\\w \left(t_{z} + z\right)\\w\end{matrix}\right) \\
    &= Homogeneous\left(\left(\begin{matrix}x\\y\\z\end{matrix}\right) + \left(\begin{matrix}t_{x}\\t_{y}\\t_{z}\end{matrix}\right)\right)
\end{align}



### 視野変換 (LookAt)

視野変換は**全体座標系** (*Global coordinate system*)に配置されたオブジェクトを観察者の立場から眺めたときの様子，すなわち**視野座標系**(*Viewing coordinate system*)に変換します．観察者の立ち位置を表現するために観察者の視点(*eye*)，観察者の視線の先の点(*center*)，そして観察者の頭の向き(*up*)を与えます．

視野変換は全体座標系を視点に平行移動する変換$LookAtTranslate$と，視線の向きを$Z$軸方向から視線の向きに回転する
変換$LookAtRotate$を合成($LookAtRotate \times LookAtTranslate$)したものと考えられます．


### 視点へのカメラの移動 (LookAtTranslate)
最初の変換は視点($I$; 眼の eye になぞらえてこの記号を使います)を原点に平行移動します．移動のベクトルは$(0 - I) = -I$ですので：

$$LookAtTranslate = \operatorname{Translate}\left(-\left(\begin{matrix}I_{x}\\I_{y}\\I_{z}\end{matrix}\right)\right) = \left(\begin{matrix}1 & 0 & 0 & - I_{x}\\0 & 1 & 0 & - I_{y}\\0 & 0 & 1 & - I_{z}\\0 & 0 & 0 & 1\end{matrix}\right)$$


念のため、$LookAtTranslate$が視点($I$)を原点に移動することを確認しましょう．

\begin{align}
LookAtTranslate \times Homogeneous\left(\left(\begin{matrix}I_{x}\\I_{y}\\I_{z}\end{matrix}\right)\right) &= \left(\begin{matrix}1 & 0 & 0 & - I_{x}\\0 & 1 & 0 & - I_{y}\\0 & 0 & 1 & - I_{z}\\0 & 0 & 0 & 1\end{matrix}\right) \times \left(\begin{matrix}I_{x}\\I_{y}\\I_{z}\\1\end{matrix}\right) \\
    &= \left(\begin{matrix}0\\0\\0\\1\end{matrix}\right)
\end{align}
    
確かに原点に移動しました．

