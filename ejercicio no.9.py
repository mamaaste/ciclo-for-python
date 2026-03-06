#contar negativos y positivos
#06-03-2026 nelson estuardo maas tecu 
positivo = 0
negativo = 0

for a in range(10):
    numero = int(input("ingrese numero: ")) 

    if numero >= 0:
     positivo = positivo + 1       
    elif numero < 0:
     negativo = negativo + 1

print("los numero positivos son: ",positivo)
print("los numero negativo son: ",negativo)