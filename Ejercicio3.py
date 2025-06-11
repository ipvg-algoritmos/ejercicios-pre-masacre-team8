numeros = []
while True:
    numero = int(input("Ingresa un número, ingresa un número negativo para finalizar"))
    if numero < 0:
        break
    numeros.append(numero)

print(f"La lista ordenada: {numeros.sort()}")