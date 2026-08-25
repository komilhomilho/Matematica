import numpy as np
import matplotlib.pyplot as plt

valores = {
    "a" : 0.2,
    "b" : 3,
    "c" : 12
}

def Desgaste(t):
    return valores["a"] * t ** 3 - 3 * t ** 2 + 12 * t

print(f"O valor do Desgaste após 2 anos de Operação é: {Desgaste(2):.1f}mm")

x = np.linspace(0, 10, 100)

y = Desgaste(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Curva de Desgaste", color="blue", linewidth=1)
plt.title("Desgaste da Máquina ao Longo do Tempo")
plt.xlabel("Tempo em Anos (t)")
plt.ylabel("Desgaste em mm (y)")
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.show()