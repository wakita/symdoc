from IPython.display import display_markdown as markdown
import numpy as np
import sympy as sp
sp.init_printing()

_Document_ = {}


def md(*args):
    s = ''
    for x in args:
        if (isinstance(x, sp.Basic) or isinstance(x, sp.MutableDenseMatrix) or isinstance(x, tuple)):
            s = s + sp.latex(x)
        elif isinstance(x, np.ndarray):
            s = s + sp.latex(sp.Matrix(x))
        elif (isinstance(x, str)): s = s + x
        elif (isinstance(x, int) or isinstance(x, float)): s = s + str(x)
        else: print(type(x))
    markdown(s, raw=True)


def line(name, *args):
  def conv(x):
    if (isinstance(x, sp.Basic) or
        isinstance(x, sp.MutableDenseMatrix) or
        isinstance(x, tuple)): return sp.latex(x)
    elif isinstance(x, str): return x
    else: print(type(x))

  line = [ conv(x) for x in args ]
  try:
    _Document_[name].append(line)
  except:
    _Document_[name] = [line]


def document(name):
  for line in _Document_[name]:
    markdown(''.join(line), raw=True)


def _subs(EXPR, repl):
    return EXPR.subs(repl, simultaneous=True)
