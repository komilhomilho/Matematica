import numpy as np
import matplotlib.pyplot as plt

valores = {
    "a" : -0.5,
    "b" : 4,
    "c" : 10
}

def PoluicaoRio(t):
    return valores["a"] * t ** 2 + valores["b"] * t + valores["c"]

def ConcentracaoMaxima():
    return abs(valores["b"] / (2 * valores["a"]))

print(f"A Concentração Maxima de Poluente no rio é de: {ConcentracaoMaxima()}")
print(f"O valor Maximo Com O nivel de Concentração Maxima é de: {PoluicaoRio(ConcentracaoMaxima()):.2f}")

x = np.linspace(0, ConcentracaoMaxima() * 2, 100)

y = PoluicaoRio(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Nivel de Poluente No Rio", color="blue", linewidth=2.5)
plt.title("Concentração decorrente no tempo: ")
plt.xlabel("Concentração:")
plt.ylabel("Tempo (y):")
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.show()