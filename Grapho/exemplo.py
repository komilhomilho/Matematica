from gerador_grafo import criar_grafo, nx
import matplotlib.pyplot as plt

meu_grafo, pos = criar_grafo(tipo_grafo='arvore_binaria_busca', tipo_valor='numero', quantidade_nos=50, aleatorio=True, gerar_posicoes=True)

no_escolhido = list(meu_grafo.nodes())[3] 
antecessores = list(nx.ancestors(meu_grafo, no_escolhido))
print(f"Antecessores do nó {no_escolhido}: {antecessores}")

plt.figure(figsize=(14, 8))
nx.draw(
    meu_grafo, 
    pos,
    with_labels=True, 
    node_color="lightgreen", 
    node_size=600, 
    arrowsize=10, 
    font_size=8
)
plt.show()