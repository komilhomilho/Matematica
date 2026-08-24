from funcoes import *
from meusImports import *

p = symbols('p')
#Exercício 3
#Determine se p∨¬p é tautologia, contradição ou contingência.

tabela = ttg.Truths(['p'], ['~p', 'p or ~p'])
df = formatar_tabela_vf(tabela, ['p', 'p\'', 'p v p\''])
resultado = classificar_expressao(df, 'p v p\'')
print(f"Esse tabela é: {resultado}")