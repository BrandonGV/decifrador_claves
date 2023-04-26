
def ordenar_mezlca(array):
    if len(array) > 1:
        medio = len(array) // 2
        mitad_izquierda = array[:medio]
        mitad_derecha = array[medio:]

        ordenar_mezlca(mitad_izquierda)
        ordenar_mezlca(mitad_derecha)

        i = 0
        j = 0
        k = 0

        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if mitad_izquierda[i] < mitad_derecha[j]:
                array[k] = mitad_izquierda[i]
                i += 1
            else:
                array[k] = mitad_derecha[j]
                j += 1
            k += 1

        while i < len(mitad_izquierda):
            array[k] = mitad_izquierda[i]
            i += 1
            k += 1

        while j < len(mitad_derecha):
            array[k] = mitad_derecha[j]
            j += 1
            k += 1

    return array

def busqueda_binaria(array, llave):
    abajo = 0
    alto = len(array) - 1

    while abajo <= alto:
        medio = (abajo + alto) // 2

        if array[medio] == llave:
            return medio
        elif array[medio] < llave:
            abajo = medio + 1
        else:
            alto = medio - 1

    return -1

def decifrar_calve(llave, lista_organizada):
    lista_organizada = ordenar_mezlca(lista_organizada)
    clave_decifrada = ""

    for digit in llave:
        index = busqueda_binaria(lista_organizada, int(digit))

        if index != -1:
            clave_decifrada += str(index)
        else:
            clave_decifrada += digit

    return clave_decifrada


lista_organizada = [5, 2, 8, 1, 9, 0, 3, 7, 4, 6]
llave=[]
for x in range(4):
    valor=int(input("ingresa el valor:"))
    llave.append (valor)
print(llave)
clave_decifrada = decifrar_calve(llave, lista_organizada)
print("Clave decifrada:", clave_decifrada)