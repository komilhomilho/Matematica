from funcoes import formatar_tabela_vf
from meusImports import *
from funcoes import *

p, q, r = symbols('p q r')

#region a.
tabela = (ttg.Truths(['p', 'q'], ['~p','~q','~p or ~q'], ints=False))
df = formatar_tabela_vf(tabela, ['p', 'q','¬p','¬q','¬p v ¬q'])
resultado = classificar_expressao(df, '¬p v ¬q')
print(f"Esse tabela é: {resultado}")
#endregion

#region b.
tabela = (ttg.Truths(['p', 'q', 'r'], ['~p','~q','~r','p and ~q','(p and ~q) or r','~p or q','(~p or q) and r', '((p and ~q) or r) and ((~p or q) and r)'], ints=False))
df = formatar_tabela_vf(tabela, ['p', 'q','r','¬p','¬q','¬r','p ^ ¬q','(p ^ ¬q) v r', '¬p v q','(¬p v q) and r', '((¬p ^ ¬q) v r) ^ ((¬p v q) ^ r)'])
resultado = classificar_expressao(df, '((¬p ^ ¬q) v r) ^ ((¬p v q) ^ r)')
print(f"Esse tabela é: {resultado}")
#endregion

#region c.
tabela = (ttg.Truths(['p', 'q'], ['p and q', 'p or q', '(p and q) => (p or q)'], ints=False))
df = formatar_tabela_vf(tabela, ['p', 'q','p ^ q','p v q','(p ^ q) → (p v q)'])
resultado = classificar_expressao(df, '(p ^ q) → (p v q)')
print(f"Esse tabela é: {resultado}")
#endregion

#region d.
tabela = (ttg.Truths(['p', 'q', 'r'], ['p and q', '(p and q) or r'], ints=False))
df = formatar_tabela_vf(tabela, ['p', 'q','r','p ^ q','(p ^ q) v r'])
resultado = classificar_expressao(df, '(p ^ q) v r')
print(f"Esse tabela é: {resultado}")
#endregion

#region e.
tabela = (ttg.Truths(['p', 'q'], ['p and q', '(p and q) => p'], ints=False))
df = formatar_tabela_vf(tabela, ['p', 'q','p ^ q','(p ^ q) → p'])
resultado = classificar_expressao(df, '(p ^ q) → p')
print(f"Esse tabela é: {resultado}")
#endregion

#region f.
tabela = (ttg.Truths(['p', 'q'], ['p or q', 'p => (p or q)'], ints=False))
df = formatar_tabela_vf(tabela, ['p', 'q','p v q','p → (p ^ q)'])
resultado = classificar_expressao(df, 'p → (p ^ q)')
print(f"Esse tabela é: {resultado}")
#endregion

#region g.
tabela = (ttg.Truths(['p', 'q'], ['p => q', 'p and (p => q)','(p and (p => q)) => q'], ints=False))
df = formatar_tabela_vf(tabela, ['p', 'q','p → q','p ^ (p → q)','(p ^ (p → q)) → q'])
resultado = classificar_expressao(df, '(p ^ (p → q)) → q')
print(f"Esse tabela é: {resultado}")
#endregion

#region h.
tabela = (ttg.Truths(['p', 'q'], ['~q','p => q', '(p => q) and ~q','((p => q) and ~q) => ~q'], ints=False))
df = formatar_tabela_vf(tabela, ['p','q','¬q','p → q', '(p → q) ^ ¬q','((p → q) ^ ¬q) → ¬q'])
resultado = classificar_expressao(df, '((p → q) ^ ¬q) → ¬q')
print(f"Esse tabela é: {resultado}")
#endregion

#region i.
tabela = (ttg.Truths(['p', 'q'], ['~q','p => q', '(p => q) and ~q','((p => q) and ~q) => ~q'], ints=False))
df = formatar_tabela_vf(tabela, ['p','q','¬q','p → q', '(p → q) ^ ¬q','((p → q) ^ ¬q) → ¬q'])
resultado = classificar_expressao(df, '((p → q) ^ ¬q) → ¬q')
print(f"Esse tabela é: {resultado}")
#endregion