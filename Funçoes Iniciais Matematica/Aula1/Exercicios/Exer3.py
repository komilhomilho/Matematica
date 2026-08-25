import numpy as np
import matplotlib.pyplot as plt
import math as math

def T(s):
    return 2**s + 3 * s + 1

print(f"O deslocamento Do Pistão com 2s é: {T(2):.2f} m")

x = np.linspace(0, 5, 100)

y = T(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Valor Da Tensão: 220 * x", color="blue", linewidth=2.5)
plt.title("Tensão x Corrente")
plt.xlabel("Corrente (x):")
plt.ylabel("Tensão (y):")
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.show()