from sympy import symbols
import ttg
from IPython.display import display
from sympy.logic.boolalg import Or
from sympy.logic.boolalg import Implies
from sympy.logic.boolalg import And
from sympy.logic.boolalg import Not

# Definindo as variáveis simbólicas
p, q, r, s = symbols('p q r s')

# Printando sentenças
display(f'{p}: Se for um dia ensolarado.')
display(f'{q}: e eu tiver tempo livre')
display(f'{r}: então irei à praia')
display(f'{s}: ou farei um piquenique')


# Realizando Calculo
prep = Implies(And(p, q), And(Or(r, s), Not(And(r, s))))

print('\n Preposição completa')
# Pritando Preposição completa
display(prep, 'Se for um dia ensolarado e eu tiver tempo livre, então irei à praia ou farei um piquenique, mas não farei ambos.')

# Tabela Verdade
print('\n Tabela Verdade:')
print(ttg.Truths(['p', 'q','r','s'], ['(p => q)', 'r or s', 'r => s', '(p and q) implies ((r and s) and not(r or s))'], ints=False))