from funcoes import *

# Exercício 2
# Construa a tabela-verdade de (p∧q)→p.

p, q = symbols('p q')

tabela = ttg.Truths(['p', 'q'], ['p and q', 'p => q'], ints=False)
df = formatar_tabela_vf(tabela, ['p','q', 'p ^ q', 'p => q'])

