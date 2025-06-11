#Contar vocales y consonantes de una palabra

#Solicitar una palabra al usuario

vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", \
               "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]


contador_v=0
contador_c=0

palabra = input("Ingresa una palabra: ")
for letra in palabra.lower():
    if letra in vocales:
        contador_v +=1
    elif letra in consonantes:
        contador_c +=1

print("Vocales: ", contador_v)
print("Consonantes: ", contador_c)




