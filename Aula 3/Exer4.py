from funcoes import *
from meusImports import *

#Exercício 4
#Verifique se p∧¬p é tautologia ou contradição.
p = symbols('p')

tabela = ttg.Truths(['p'], ['~p', 'p and ~p'])
df = formatar_tabela_vf(tabela, ['p', 'p\'', 'p ^ p\''])
resultado = classificar_expressao(df, 'p ^ p\'')
print(f"Esse tabela é: {resultado}")