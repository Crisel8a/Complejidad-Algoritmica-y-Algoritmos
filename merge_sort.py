import random


def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izq = lista[:medio]
        der = lista[medio:]
        print(izq, "*", der)  # muestra las sublistas que se van a mezclar

        # llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izq)
        ordenamiento_por_mezcla(der)

        # iteradores para recorrer las dos sublistas
        i = 0  # izquierda
        j = 0  # derecha
        # iterador para la lista principal
        k = 0

        while i < len(izq) and j < len(der):
            if izq[i] < der[j]:
                lista[k] = izq[i]
                i += 1
            else:
                lista[k] = der[j]
                j += 1
            k += 1

        while i < len(izq):
            lista[k] = izq[i]
            i += 1
            k += 1

        while j < len(der):
            lista[k] = der[j]
            j += 1
            k += 1

        print(izq, "*", der)  # muestra las sublistas que se van a mezclar
        print(lista)  # muestra la lista ya ordenada
        print("-" * 40)  # separador para ver las sublistas que se van a mezclar

    return lista


if __name__ == "__main__":
    tamano_linsta = int(input("De que tamano sera la lista: "))

    lista = [random.randint(0, 100) for i in range(tamano_linsta)]
    print(lista)
    print("-" * 20)
    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)
