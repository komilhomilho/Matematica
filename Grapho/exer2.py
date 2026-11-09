import networkx as g
#2. Escreva uma função que conta o número de nós de uma árvore binária.
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

def validar_e_contar_arvore(arvore):
    total_de_nos = len(arvore.nodes)
    
    eh_binaria = True
    erros = []
    
    for no in arvore.nodes:
        qtd_filhos = len(arvore.out_edges(no))
        
        qtd_pais = len(arvore.in_edges(no))
        
        if qtd_filhos > 2:
            eh_binaria = False
            erros.append(f"O nó '{no}' inválido: tem {qtd_filhos} filhos.")
            
        if qtd_pais > 1:
            eh_binaria = False
            erros.append(f"O nó '{no}' inválido: tem {qtd_pais} pais.")

    print(f"Quantidade total de nós: {total_de_nos}")
    
    if eh_binaria:
        print("Validação: É uma árvore binária perfeita!")
    else:
        print("Validação: NÃO é uma árvore binária válida.")
        for erro in erros:
            print(f"   -> {erro}")
            
    return eh_binaria, total_de_nos

validar_e_contar_arvore(grafo)
