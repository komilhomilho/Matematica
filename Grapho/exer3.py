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

# 3. Escreva uma função que conta o número de nós não folha de uma árvore binária. 
def validar_e_contar_arvore(arvore):    
    eh_binaria = True
    erros = []
    total_de_nos = 0
    nos_nao_folha = 0
    
    for no in arvore.nodes:                
        total_de_nos += 1
        
        qtd_filhos = len(arvore.out_edges(no))
        qtd_pais = len(arvore.in_edges(no))
        
        if qtd_filhos > 0:
            nos_nao_folha += 1
            
        if qtd_filhos > 2:
            eh_binaria = False
            erros.append(f"O nó '{no}' tem {qtd_filhos} filhos (máximo é 2).")
            
        if qtd_pais > 1:
            eh_binaria = False
            erros.append(f"O nó '{no}' tem {qtd_pais} pais (indica ciclos/cruzamentos).")

    print(f"Quantidade total de nós: {total_de_nos}")
    print(f"Quantidade de nós NÃO-FOLHA: {nos_nao_folha}") # Resultado do exercício 3
    
    if eh_binaria:
        print("Validação: É uma árvore binária perfeita!")
    else:
        print("Validação: NÃO é uma árvore binária válida.")
        for erro in erros:
            print(f"   -> {erro}")
            
    return eh_binaria, total_de_nos

validar_e_contar_arvore(grafo)