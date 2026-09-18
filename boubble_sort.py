import random


def bouble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(n - i - 1):  # O(n^2)
            if lista[j] > lista[j + 1]:  # los intercambio
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


if __name__ == "__main__":
    tamano_linsta = int(input("De que tamano sera la lista: "))

    lista = [random.randint(0, 100) for i in range(tamano_linsta)]
    print(lista)
    lista_ordenada = bouble_sort(lista)
    print(lista_ordenada)
