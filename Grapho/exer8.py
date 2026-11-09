from gerador_grafo import criar_grafo, nx

meu_grafo = criar_grafo(tipo_grafo='arvore_binaria', tipo_valor='numero', quantidade_nos=150)

#8. Escreva uma função que exclui todos os nós de uma árvore binária NÃO ordenada com ID par.

def excluir_pares(arvore):
    nos = list(arvore.nodes)
    print(nos)
    for no in nos:
        if (no % 2 == 0):
            nos.remove(no)
    print(f"Lista sem Numeros Pares: {nos}")
    return

excluir_pares(meu_grafo)