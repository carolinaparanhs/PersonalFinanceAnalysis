import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("gastos.csv")

total = dados["valor"].sum()
print("total gasto no mês: R$", total)

por_categoria = dados.groupby("categoria")["valor"].sum()
print("\nGastos por categoria: ")
print(por_categoria)

por_categoria.plot(kind="bar")
plt.title("Gastos por categoria")
plt.ylabel("Valor (R$)")
plt.xlabel("Categoria")
plt.tight_layout()
plt.show()