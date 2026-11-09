from gerador_grafo import criar_grafo, nx
import matplotlib.pyplot as plt

grafo, posicoes = criar_grafo(tipo_grafo='arvore_binaria_busca', tipo_valor='numero', quantidade_nos=50, aleatorio=True, gerar_posicoes=True)
print("Nós com posições extraídos com sucesso!")

#10. Escreva uma função que retorna verdadeiro se uma árvore é binária de busca e falso caso contrário 

def eh_busca(arvore):
    for no in arvore.nodes:
        print(f"nó: {no} | sucessores: {list(arvore.successors(no))}")
    return

nx.draw(
    grafo, 
    posicoes,
    with_labels=True, 
    node_color="lightgreen", 
    node_size=600, 
    arrowsize=10, 
    font_size=8
)
plt.show()
eh_busca(grafo)