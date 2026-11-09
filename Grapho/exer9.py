from gerador_grafo import criar_grafo, nx

grafo, posicoes = criar_grafo(tipo_grafo='arvore_binaria', tipo_valor='numero', quantidade_nos=150, gerar_posicoes=True)

nodes_with_pos = [(node, coords[0], coords[1]) for node, coords in posicoes.items()]
print("Nós com posições extraídos com sucesso!")

# 3. Função corrigida para excluir do GRAFO os nós com ID par
def excluir_pares(arvore):
    nos_para_remover = [no for no in arvore.nodes if no % 2 == 0]
    
    print(f"Quantidade de nós antes: {len(arvore.nodes)}")
    print(f"Nós pares que serão removidos: {nos_para_remover}")

    arvore.remove_nodes_from(nos_para_remover)
    
    print(f"Quantidade de nós depois: {len(arvore.nodes)}")
    print(f"Lista de nós restantes: {list(arvore.nodes)}")
    return arvore

grafo_filtrado = excluir_pares(grafo)
