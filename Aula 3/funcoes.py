from meusImports import *

def formatar_tabela_vf(tabela, colunas=None, exibir=True):
    df = tabela.as_pandas
    
    df = df.astype(bool).map(lambda x: 'V' if x else 'F')
    
    if colunas:
        df.columns = colunas
        
    if exibir:
        print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))
        
    return df

def classificar_expressao(df, nome_coluna):
    coluna = df[nome_coluna]
    
    if (coluna == 'V').all() or (coluna == True).all() or (coluna == 1).all():
        return "Tautologia (Tudo verdadeiro)"
    elif (coluna == 'F').all() or (coluna == False).all() or (coluna == 0).all():
        return "Contradição (Tudo falso)"
    else:
        return "Contingência (Mistura de V e F)"