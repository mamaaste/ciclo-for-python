#promedio de notas
#06-03-2026 nelson estuardo maas tecu 
suma = 0


for nota in range(1,6):
 nota = float(input("ingrese 5 notas: "))
 suma =suma+nota

promedio = suma/5

print("el promedio final es: ",promedio)