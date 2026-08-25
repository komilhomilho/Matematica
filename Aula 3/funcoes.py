from meusImports import *

def formatar_tabela_vf(tabela, colunas=None, exibir=True):
    # 1. Pega o DataFrame da tabela ttg
    df = tabela.as_pandas
    
    # 2. Converte 1/0 ou True/False para V e F
    df = df.astype(bool).map(lambda x: 'V' if x else 'F')
    
    # 3. Renomeia as colunas se você passar uma lista de nomes
    if colunas:
        df.columns = colunas
        
    # 4. Imprime no terminal com a grade bonita (opcional)
    if exibir:
        print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))
        
    return df

def classificar_expressao(df, nome_coluna):
    coluna = df[nome_coluna]
    
    # Checa se todos são 'V' (ou True / 1)
    if (coluna == 'V').all() or (coluna == True).all() or (coluna == 1).all():
        return "Tautologia (Tudo verdadeiro)"
    # Checa se todos são 'F' (ou False / 0)
    elif (coluna == 'F').all() or (coluna == False).all() or (coluna == 0).all():
        return "Contradição (Tudo falso)"
    else:
        return "Contingência (Mistura de V e F)"