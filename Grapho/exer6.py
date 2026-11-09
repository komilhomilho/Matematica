import networkx as g

grafo = g.DiGraph()

conexoes = [
    (50, 23), (23, 88), (88, 12), (12, 4), (12, 76),
    (88, 34), (34, 9), (23, 61), (61, 45), (45, 92),
    (61, 17), (17, 3),
    
    (50, 81), (81, 29), (29, 5), (5, 67), (29, 99),
    (99, 14), (99, 38), (81, 72), (72, 21), (21, 55),
    (72, 8), (8, 42), (8, 95)
]

grafo.add_edges_from(conexoes)

#6. Escreva uma função para buscar um número ímpar em uma árvore binária NÃO ordenada.

def procurar_valor(arvore, buscar):
    if buscar % 2 == 0:
        print(f"A busca só é realizado com Numeros Impares")
        return
    pai_no = 0
    filhos = 0
    for no in arvore.nodes:
        if (no == buscar):
            pai_no = list(arvore.predecessors(no))
            filhos = list(arvore.successors(no))
            break
    print(f"Numero encontrado: {buscar}")
    print(f"Pai do Nó: {pai_no}")
    print(f"Filhos do Nó: {filhos}")
    return

procurar_valor(grafo, int(input("Insira o valor A ser Buscado: ")))