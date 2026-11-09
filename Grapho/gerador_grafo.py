import networkx as nx
import random
import string

def _gerar_rotulos(tipo_valor, quantidade, aleatorio):
    valores = []
    
    if tipo_valor == 'numero':
        if aleatorio:
            valores = random.sample(range(1, quantidade * 10 + 100), quantidade)
        else:
            valores = list(range(1, quantidade + 1))
            
    elif tipo_valor == 'letra':
        letras = list(string.ascii_uppercase)
        for i in range(quantidade):
            if i < 26:
                valores.append(letras[i])
            else:
                valores.append(f"{letras[i%26]}{i//26}")
        if aleatorio:
            random.shuffle(valores)
            
    elif tipo_valor == 'palavra':
        substantivos = [
            "Amor", "Vida", "Sol", "Lua", "Estrela", "Gato", "Cafe", "Codigo", 
            "Bug", "Python", "Grafo", "Beijo", "Nuvem", "Vento", "Fogo", "Terra",
            "Flor", "Mar", "Horizonte", "Sonho", "Pixel", "Byte", "Dado", "No",
            "Sombra", "Chuva", "Magia", "Universo", "Galaxia", "Mundo", "Luz",
            "Mente", "Coracao", "Voz", "Arte", "Ritmo", "Tempo", "Espaco", "Jornada", "Chave"
        ]
        
        adjetivos = [
            "Magico", "Brilhante", "Secreto", "Galactico", "Rapido", "Doce", "Quente", "Frio",
            "Suave", "Forte", "Livre", "Vivo", "Puro", "Novo", "Antigo", "Sabio",
            "Eterno", "Infinito", "Radiante", "Calmo", "Veloz", "Cosmico", "Dourado", "Prateado",
            "Silencioso"
        ]
        
        palavras_base = [f"{s}{a}" for s in substantivos for a in adjetivos]
        
        for i in range(quantidade):
            if i < len(palavras_base):
                valores.append(palavras_base[i])
            else:
                base = palavras_base[i % len(palavras_base)]
                repeticao = (i // len(palavras_base)) + 1
                valores.append(f"{base}_{repeticao}")
                
        if aleatorio:
            random.shuffle(valores)
            
    return valores

def _calcular_posicoes_arvore(grafo):
    posicoes = {}
    if len(grafo.nodes) == 0:
        return posicoes
        
    raizes = [n for n, grau in grafo.in_degree() if grau == 0]
    if not raizes:
        return nx.spring_layout(grafo)
        
    x_counter = [0]
    
    def perc_in_order(no, prof=0):
        filhos = list(grafo.successors(no))
        filho_esq, filho_dir = None, None
        
        for f in filhos:
            direcao = grafo.edges[no, f].get('direcao')
            if direcao == 'esquerda':
                filho_esq = f
            elif direcao == 'direita':
                filho_dir = f
        
        if filho_esq is None and filho_dir is None and len(filhos) > 0:
            filho_esq = filhos[0]
            if len(filhos) > 1:
                filho_dir = filhos[1]
                
        if filho_esq:
            perc_in_order(filho_esq, prof + 1)
            
        posicoes[no] = (x_counter[0], -prof)
        x_counter[0] += 1
        
        if filho_dir:
            perc_in_order(filho_dir, prof + 1)
            
    perc_in_order(raizes[0])
    return posicoes

def criar_grafo(tipo_grafo='arvore_binaria', tipo_valor='numero', quantidade_nos=10, aleatorio=True, probabilidade=0.3, gerar_posicoes=False):
    novos_rotulos = _gerar_rotulos(tipo_valor, quantidade_nos, aleatorio)
    G_esqueleto = None

    if tipo_grafo == 'arvore_binaria_busca':
        G_final = nx.DiGraph()
        
        class NoBST:
            def __init__(self, val):
                self.val = val
                self.esq = None
                self.dir = None

        def inserir(raiz, val):
            if raiz is None:
                return NoBST(val)
            if val < raiz.val:
                raiz.esq = inserir(raiz.esq, val)
            elif val > raiz.val:
                raiz.dir = inserir(raiz.dir, val)
            return raiz
            
        raiz_bst = None
        for valor in novos_rotulos:
            raiz_bst = inserir(raiz_bst, valor)
            
        def montar_grafo_nx(no_atual, grafo):
            if no_atual is not None:
                grafo.add_node(no_atual.val)
                if no_atual.esq:
                    grafo.add_edge(no_atual.val, no_atual.esq.val, direcao='esquerda')
                    montar_grafo_nx(no_atual.esq, grafo)
                if no_atual.dir:
                    grafo.add_edge(no_atual.val, no_atual.dir.val, direcao='direita')
                    montar_grafo_nx(no_atual.dir, grafo)
                    
        montar_grafo_nx(raiz_bst, G_final)
        
        if gerar_posicoes:
            posicoes = _calcular_posicoes_arvore(G_final)
            return G_final, posicoes
            
        return G_final
        
    elif tipo_grafo == 'arvore_binaria':
        G_esqueleto = nx.DiGraph()
        for i in range(quantidade_nos):
            if 2 * i + 1 < quantidade_nos:
                G_esqueleto.add_edge(i, 2 * i + 1)
            if 2 * i + 2 < quantidade_nos:
                G_esqueleto.add_edge(i, 2 * i + 2)
                
    elif tipo_grafo == 'direcionado':
        G_esqueleto = nx.erdos_renyi_graph(n=quantidade_nos, p=probabilidade, directed=True)
        
    elif tipo_grafo == 'nao_direcionado':
        G_esqueleto = nx.erdos_renyi_graph(n=quantidade_nos, p=probabilidade, directed=False)
        
    elif tipo_grafo == 'caminho':
        G_esqueleto = nx.path_graph(quantidade_nos, create_using=nx.DiGraph)
        
    else:
        raise ValueError("Tipo invalido")

    mapa_rotulos = {no_antigo: novos_rotulos[i] for i, no_antigo in enumerate(G_esqueleto.nodes())}
    grafo_final = nx.relabel_nodes(G_esqueleto, mapa_rotulos)
    
    if gerar_posicoes:
        if tipo_grafo == 'arvore_binaria':
            posicoes = _calcular_posicoes_arvore(grafo_final)
        elif tipo_grafo == 'caminho':
            posicoes = {mapa_rotulos[i]: (i, 0) for i in G_esqueleto.nodes()}
        else:
            posicoes = nx.spring_layout(grafo_final)
        return grafo_final, posicoes

    return grafo_final