from funcoes import formatar_tabela_vf
from sympy import false
from meusImports import *
from funcoes import *

#Monte a tabela-verdade de (p→q)↔(¬q→¬p).

p, q = symbols('p q')

tabela = (ttg.Truths(['p', 'q'], ['~p','~q','p => q', '~q => ~p', '(p => q) = (~q => ~p)'], ints=False))
df = formatar_tabela_vf(tabela, ['p', 'q', 'p\'', 'q\'', '(p→q)', '(¬q→¬p)', '(p→q)↔(¬q→¬p)'])
