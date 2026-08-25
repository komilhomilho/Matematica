import numpy as np
import matplotlib.pyplot as plt

def FormatarMonetario(valor):
    return f"R$ {valor:,.2f}"

def Custo(nivelProducao):
    if nivelProducao < 3:
        resultado = (10 * nivelProducao + 5) * 1000000
    elif nivelProducao == 3:
        resultado = 35 * 1000000
    else:
        resultado = (2 * nivelProducao ** 2 - 4 * nivelProducao + 11) * 1000000
    return resultado

print(f"O custo com o Nível de Produção 1 é: {FormatarMonetario(Custo(1))}")
print(f"O custo com o Nível de Produção 3 é: {FormatarMonetario(Custo(3))}")
print(f"O custo com o Nível de Produção 5 é: {FormatarMonetario(Custo(5))}")


x = np.linspace(0, 5, 41)

y = np.asarray([Custo(valor) for valor in x]) / 1000000

plt.figure(figsize=(10, 5))
plt.plot(x, y, label="Custo", color="red", linewidth=2.5)
plt.title("Custo em Milhões Com o Nivel de Produção")
plt.xlabel("Nivel De Produção:")
plt.ylabel("Custo (Milhões de R$)")
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.show()