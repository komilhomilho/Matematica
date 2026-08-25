import numpy as np
import matplotlib.pyplot as plt

def CustoTotal(x):
    return 5000 + 120 * x

def CalculoCustoVigia(x):
    return (x - 5000)/120

print(f"O Custo Total e de: R$ {CustoTotal(50):,.2f}")
print(f"A Quantidade de Vigias Que Podem Ser contratados é: {CalculoCustoVigia(11000):.0f}")

x = np.linspace(0, 500, 100)

y = CustoTotal(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y, label="Custo Total 5000 + 120x", color="green", linewidth=2.5)
plt.title("Gráfico de Custo Total")
plt.xlabel("Quantidade Produzida (x)")
plt.ylabel("Custo em R$ (y)")
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.show()


