import networkx as g
grafo = g.DiGraph()

conexoes = [
    ("M", "G"), ("G", "D"), ("D", "B"), ("B", "A"), ("B", "C"),
    ("D", "F"), ("F", "E"), ("G", "J"), ("J", "I"), ("I", "H"),
    ("J", "L"), ("L", "K"),
    
    ("M", "T"), ("T", "P"), ("P", "O"), ("O", "N"), ("P", "R"),
    ("R", "Q"), ("R", "S"), ("T", "W"), ("W", "V"), ("V", "U"),
    ("W", "Y"), ("Y", "X"), ("Y", "Z")
]

grafo.add_edges_from(conexoes)

#5. Escreva uma função que calcula a altura de uma árvore binária. 
def calcular_altura(arvore):
    altura = -1
    raiz = [no for no, grau in arvore.in_degree() if grau == 0][0]
    nivel_atual = [raiz]
    
    while len(nivel_atual) != 0:
        proximos_no = []
        for no in nivel_atual:
            filhos = [aresta[1] for aresta in arvore.out_edges(no)]
            proximos_no.extend(filhos)
        nivel_atual = proximos_no
        altura += 1
    print(f'a altura da arvore é: {altura}')
    return 

calcular_altura(grafo)