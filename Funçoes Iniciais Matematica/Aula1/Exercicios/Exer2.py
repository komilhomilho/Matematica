import numpy as np
import matplotlib.pyplot as plt

def V(i):
    return 220 * i

print(f"O Valor Da Tensão é com a corrente em 0,5 é de: {V(0.5):.0f}V")


x = np.linspace(0, 5, 100)

y = V(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Valor Da Tensão: 220 * x", color="blue", linewidth=2.5)
plt.title("Tensão x Corrente")
plt.xlabel("Corrente (x):")
plt.ylabel("Tensão (y):")
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.show()