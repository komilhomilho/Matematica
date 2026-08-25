import numpy as np
import matplotlib.pyplot as plt

valores = {
    "a" : -2,
    "b" : 80,
    "c" : 500
}

def LucroFabrica(x):
    return valores['a'] * x ** 2 + valores["b"] * x - valores["c"]

def NumeroUnidadesLucroMaximo():
    return abs(valores["b"] / (2 * valores["a"]))

unidades_ideais = NumeroUnidadesLucroMaximo()
lucro_max = LucroFabrica(unidades_ideais)

print(f"O Valor De Unidades Necessária Para O Lucro Máximo é: {unidades_ideais:.0f}")
print(f"O Lucro Máximo da Fábrica é: R$ {lucro_max:,.2f}")

x = np.linspace(0, NumeroUnidadesLucroMaximo() * 2, 100)
y = LucroFabrica(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Equação do Lucro (L(x))", color="blue", linewidth=2.5)
plt.plot(unidades_ideais, lucro_max, 'ro', label=f'Lucro Máximo (x={unidades_ideais:.0f})')
plt.title("Análise de Lucro da Fábrica")
plt.xlabel("Quantidade Produzida (x)")
plt.ylabel("Lucro em R$ (y)")

plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.show()
