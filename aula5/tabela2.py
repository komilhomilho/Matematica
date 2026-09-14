from funcoes import formatar_tabela_vf
from meusImports import *
from funcoes import *

#Monte a tabela-verdade de (p→q)↔(¬q→¬p).

p, q, r = symbols('p q r')

tabela = (ttg.Truths(['p', 'q', 'r'], ['~p','~q','~r','p or q or r', '~p or ~q or ~r', '(p or r or q) and (~p or ~q or ~r)'], ints=False))
df = formatar_tabela_vf(tabela, ['p', 'q', 'r', '¬p', '¬q', '¬r', 'p v q v r', '¬p v ¬q v ¬r', '(p v q v r) ^ (¬p v ¬q v ¬r)'])
resultado = classificar_expressao(df, '(p v q v r) ^ (¬p v ¬q v ¬r)')
print(f"Esse tabela é: {resultado}")
