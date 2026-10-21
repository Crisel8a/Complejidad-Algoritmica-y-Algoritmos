import random


def busqueda_binaria(lista, comienzo, final, objetivo):
    print(
        f"buscando {objetivo} entre {comienzo} y {lista[final - 1]}"
    )  # para ver como va buscando
    if comienzo > final:  # no se econtró el elemento
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:  # se encontró
        return True
    elif lista[medio] < objetivo:  # seguir buscando
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)


if __name__ == "__main__":
    tamano_linsta = int(input("De que tamano sera la lista: "))
    objetivo = int(input("Que numero quieres encontrar: "))

    lista = sorted([random.randint(0, 100) for i in range(tamano_linsta)])
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    print(f"El objetivo {objetivo} {'esta' if encontrado else 'no esta'} en la lista")
