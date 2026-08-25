from meusImports import *

p, q = symbols('p q')
#Exercício 1
#Considere p:'João estuda', q:'João passa na prova'. Construa a tabela-verdade de p→q.

print(f"{p}: João Estuda")
print(f"{q}: João Passa na Prova")

print(ttg.Truths(['p', 'q'], ['p => q'], ints=False))