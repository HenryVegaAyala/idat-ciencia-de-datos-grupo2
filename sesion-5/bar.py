import matplotlib.pyplot as plt

ciudades = ["Lima", "Cusco", "Arequipa"]
ventas = [500, 300, 450]

plt.bar(ciudades, ventas, color=["red", "green", "blue"])

plt.title("Ventas por ciudades")
plt.ylabel("Ventas")
plt.xlabel("Ciudades")

plt.show()
