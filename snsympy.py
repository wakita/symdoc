import sympy as sp

from nbsupport import md

def display_substitution(substitution):
    md('$', *chain.from_iterable([[v, r'\mapsto ', e, r'\quad '] for v, e in substitution]), '$')


def derivatives(F, X, ARGS):
    FGH = F, G, H = [sp.simplify(F) for F in
            [F, sp.Matrix([F]).jacobian(X).T, sp.hessian(F, X)]]
    return FGH, [sp.lambdify(ARGS, F, dummify=False) for F in FGH]
