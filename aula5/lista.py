import math
from funcoes import formatar_tabela_vf
from meusImports import *
from funcoes import *
#region Parte 1
# -----------------------------------------------------------------------------
# Exercício 1
# -----------------------------------------------------------------------------
tipoPaes = 3 
recheios = 4
bebidas = 2
lanches = tipoPaes * recheios * bebidas
print(f'Tipos de Pães: {tipoPaes} | Tipos de Recheio: {recheios} | Bebidas: {bebidas}')
print(f'Pode formar {lanches} combos diferentes.')

# -----------------------------------------------------------------------------
# Exercício 2
# -----------------------------------------------------------------------------
onibus = 2
metro = 3
trajetoTotal = onibus * metro
print(f'Marcos pode ir ao trabalho de {trajetoTotal} maneiras diferentes.')

# -----------------------------------------------------------------------------
# Exercício 3
# -----------------------------------------------------------------------------
letrasAlfabeto = 26
opcoesNumeros = 10
qtdLetrasPlaca = 2
qtdNumerosPlaca = 3
placas = (letrasAlfabeto ** qtdLetrasPlaca) * (opcoesNumeros ** qtdNumerosPlaca)
print(f'A quantidade de placas possíveis de se formar é: {placas}')

# -----------------------------------------------------------------------------
# Exercício 4
# -----------------------------------------------------------------------------
qtdSaladas = 5
qtdPratos = 4
qtdSobremesas = 3
pratoDia = qtdSaladas * qtdPratos * qtdSobremesas
print(f'A quantidade de pratos do dia diferentes é: {pratoDia}')

# -----------------------------------------------------------------------------
# Exercício 5
# -----------------------------------------------------------------------------
qtdPessoa = 5
fila = math.factorial(qtdPessoa)
print(f'A quantidade de maneiras de organizar as pessoas na fila é: {fila}')

# -----------------------------------------------------------------------------
# Exercício 6
# -----------------------------------------------------------------------------
palavra = "livro"
qtdLetras = len(palavra)
qtdAnagramas = math.factorial(qtdLetras)
print(f'A quantidade de anagramas da palavra {palavra} é: {qtdAnagramas}')

# -----------------------------------------------------------------------------
# Exercício 7
# -----------------------------------------------------------------------------
qtdLivros = 4
prateleira = math.factorial(qtdLivros)
print(f'A quantidade de formas de dispor os livros é: {prateleira}')

# -----------------------------------------------------------------------------
# Exercício 8
# -----------------------------------------------------------------------------
qtdAmigos = 7
filaFoto = math.factorial(qtdAmigos)
print(f'A quantidade de maneiras que os amigos podem se sentar para a foto é: {filaFoto}')

# -----------------------------------------------------------------------------
# Exercício 9 (Ajustado para usar variáveis e a função nativa de arranjo math.perm)
# -----------------------------------------------------------------------------
atletas = 6
colocacao = 3
podio = math.perm(atletas, colocacao)
print(f'O pódio pode ser disposto de {podio} maneiras.')

# -----------------------------------------------------------------------------
# Exercício 10
# -----------------------------------------------------------------------------
qtdDigitos = {1, 2, 3, 4, 5}
qtdAlgarismos = 2
qtdNumeros = math.perm(len(qtdDigitos), qtdAlgarismos)
print(f'A quantidade de números de 2 algarismos distintos é: {qtdNumeros}')

# -----------------------------------------------------------------------------
# Exercício 11
# -----------------------------------------------------------------------------
qtdCandidatos = 8
qtdCargos = 2
eleitos = math.perm(qtdCandidatos, qtdCargos)
print(f'A quantidade de maneiras de eleger presidente e vice é: {eleitos}')

# -----------------------------------------------------------------------------
# Exercício 12
# -----------------------------------------------------------------------------
qtdFichas = 7
qtdFichasOrdenar = 4
fichasOrdenadas = math.perm(qtdFichas, qtdFichasOrdenar)
print(f'Pode-se ordenar as fichas de {fichasOrdenadas} maneiras.')

# -----------------------------------------------------------------------------
# Exercício 13
# -----------------------------------------------------------------------------
qtdAlunos = 8
qtdComissoes = 3
comissoesFormadas = math.comb(qtdAlunos, qtdComissoes)
print(f'A quantidade de comissões que podem ser formadas é: {comissoesFormadas}')

# -----------------------------------------------------------------------------
# Exercício 14
# -----------------------------------------------------------------------------
qtdPessoas = 6
apertosMao = math.comb(qtdPessoas, 2)
print(f'A quantidade de apertos de mão é: {apertosMao}')

# -----------------------------------------------------------------------------
# Exercício 15
# -----------------------------------------------------------------------------
qtdFrutasEscolher = 2
qtdFrutasCesto = 5
duplasFrutas = math.comb(qtdFrutasCesto, qtdFrutasEscolher)
print(f'A quantidade de combinações de 2 frutas é: {duplasFrutas}')

# -----------------------------------------------------------------------------
# Exercício 16
# -----------------------------------------------------------------------------
# a) A ordem importa? SIM (cargos diferentes = Arranjo)
qtdPessoas = 5
qtdCargos = 3
eleito = math.perm(qtdPessoas, qtdCargos)
print(f'Item A (Ordem importa = SIM): {eleito} formas de ocupar os cargos.')

# b) A ordem importa? NÃO (comissão sem cargos = Combinação)
qtdSelecionadas = 3
comissao = math.comb(qtdPessoas, qtdSelecionadas)
print(f'Item B (Ordem importa = NÃO): {comissao} formas de escolher a comissão.')
#endregion 

#region Parte 2



#endregion