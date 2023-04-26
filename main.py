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
#busqueda binaria
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

