#Encontrar numero en la lista

listado = [2, 12, 54, 23, 77, 6, 72, 90, 1, 42]

def buscar_numero():
    if num in listado:
        print(f"El número {num} está en la lista. Se encuentra en la posición {listado.index(num)}")
    else:
        print(f"Wuaja, el número {num} no está en la lista")

num = int(input("""Mi lista contiene 10 numeros, todos entre 1 y 100, \n¿crees poder adivinarlos todos? 
                 Ingresa un número que creas se pueda encontrar en la lista: 
                 """))

buscar_numero()
    