#compras suma
#06-03-2026 nelson estuardo maas tecu 
total = 0
cantidad = int(input("Ingrese la cantidad de productos: "))

for a in range(1, cantidad+1):
    precio = float(input("Ingrese precio del producto " + str(a) + ": "))
    total = total + precio

print("El gasto total es:", total)