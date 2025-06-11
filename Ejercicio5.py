matriz = []
for i in range(3):
    fila=[]
    for e in range(3):
        numero = int(input(f"Ingresa el elemento[{i},{e}] de la matriz"))
        fila.append(numero)
    matriz.append(fila)

contador_n = 0
contador_p = 0
contador_z = 0
suma_diagonal = 0
suma_diagonal_x = 0

for i in range(3):
    for e in range(3):
        if (matriz[i][e]>0):
            contador_p +=1
        elif(matriz[i][e]<0):
            contador_n +=1
        else:
            contador_z  = 0

        if i==e:
            suma_diagonal += matriz[i][e]
        if i+e == 2:
            suma_diagonal_x += matriz[i][e]

print(f"Numeros positivos: {contador_p}")
print(f"Numeros negativos: {contador_n}")
print(f"Cantidad de 0:  {contador_z}")
print(f"Suma diagonal izquierda: {suma_diagonal}")
print(f"Suma diagonal derecha: {suma_diagonal_x}")
