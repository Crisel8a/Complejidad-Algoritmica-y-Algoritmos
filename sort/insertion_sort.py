import random


def insertion_sort(lista):
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while (
            posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual
        ):  # O(n^2)
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

    return lista


if __name__ == "__main__":
    tamano_linsta = int(input("De que tamano sera la lista: "))

    lista = [random.randint(0, 100) for i in range(tamano_linsta)]
    print(lista)
    lista_ordenada = insertion_sort(lista)
    print(lista_ordenada)
