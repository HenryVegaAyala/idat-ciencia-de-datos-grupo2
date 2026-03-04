#1. Crear una lista de productos
vitrina = ["Pan", "Alfajor", "Aceite", "Mantequilla"]

#2. Lista de números
ventas_horas = [10, 20, 15, 20]

#3. Acceder al primer elemento (Indice 0)
primer_producto = vitrina[0]
print(f"Primer producto: {primer_producto}")

#4. Acceder al último elemento (Indice -1)
ultimo_producto = vitrina[-1]
print(f"Ultimo producto: {ultimo_producto}")

#5. Contar cuantos elementos hay en la lista
total_produtos = len(vitrina)
print(f"Total de productos: {total_produtos}")

#6. Agregar un nuevo producto a la lista
vitrina.append("Donut")
print(f"Lista de productos agregado: {vitrina}")

#7. Cambiar o actualizar un producto de la lista
vitrina[2] = "Aceite de Oliva"
print(f"Lista de productos actualizada: {vitrina}")

#8. Eliminar un producto de la lista
vitrina.remove("Pan")
print(f"Lista de productos eliminado: {vitrina}")

#9. Eliminar con del de la lista
del vitrina[0]
print(f"Lista de productos eliminado con del: {vitrina}")

# 10. Uso de pop para una lista
print(f"Vitrina antes de usar pop: {vitrina}")
producto_eliminado = vitrina.pop(1)
print(f"Vitrina despues de usar pop: {vitrina}")
print(f"Producto eliminado con pop: {producto_eliminado}")

# 11. Verificar si existe un producto en la lista
existe_donut = "donut" in vitrina
print(f"¿Existe Donut en la vitrina? {existe_donut}")