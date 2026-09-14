from funcoes import formatar_tabela_vf
from meusImports import *
from funcoes import *

p, q, r = symbols('p q r')

# Na biblioteca ttg, '=' representa a equivalência (↔) e 'xor' a disjunção exclusiva (⊕)
tabela = (ttg.Truths(
    ['p', 'q', 'r'], 
    ['p = q', 'q = r', 'p xor r', '(p = q) and (q = r) and (p xor r)'], 
    ints=False
))

# Formata as colunas com os símbolos lógicos originais
df = formatar_tabela_vf(
    tabela, 
    ['p', 'q', 'r', 'p ↔ q', 'q ↔ r', 'p ⊕ r', '(p ↔ q) ∧ (q ↔ r) ∧ (p ⊕ r)']
)

resultado = classificar_expressao(df, '(p ↔ q) ∧ (q ↔ r) ∧ (p ⊕ r)')
print(f"Essa tabela é: {resultado}")