from funcoes import formatar_tabela_vf
from meusImports import *
from funcoes import *

#Monte a tabela-verdade de (p→q)↔(¬q→¬p).

p, q, r = symbols('p q r')

tabela = (ttg.Truths(['p', 'q', 'r'], ['~r','~p','p or q', 'q or ~r', 'r or ~p', '(p or r) and (q or ~r) and (r or ~p)'], ints=False))
df = formatar_tabela_vf(tabela, ['p', 'q','r', 'r\'', 'p\'', '(p v q)', '(q v ¬r)', 'r v ¬p', '(p v r) ^ (q v ¬r) ^ (r v ¬p)'])
resultado = classificar_expressao(df, '(p v r) ^ (q v ¬r) ^ (r v ¬p)')
print(f"Esse tabela é: {resultado}")
