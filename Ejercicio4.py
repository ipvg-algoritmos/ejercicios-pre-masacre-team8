numeros = []
while True:
    numero = int(input("Ingresa un número, ingresa un número negativo para finalizar"))
    if numero < 0:
        break
    numeros.append(numero)

if numeros:
    promedio = sum(numeros)/len(numeros)
    print("El promedio de los números es: ", promedio)
else:
    print("No se ingresaron numeros válidos")