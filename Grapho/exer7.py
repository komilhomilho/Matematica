from gerador_grafo import criar_grafo, nx

meu_grafo = criar_grafo(tipo_grafo='arvore_binaria', tipo_valor='numero', quantidade_nos=150)

def maior_numero(arvore):
    maior = max(arvore.nodes())
    print(f"O maior numero da arvore é: {maior}")
    return maior

maior_numero(meu_grafo)