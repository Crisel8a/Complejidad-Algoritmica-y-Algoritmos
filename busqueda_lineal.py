import random


def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            # si no hacemos un break, va a seguir buscando en toda la lista
            # i.e. si no le quito el break, me sirve par amas ocurreias
            # esto no afecta la complejidad, pero si el elemento está al principio de la lista, no es necesario seguir buscando
            # y debo pensar siempre en el peor caso, que es cuando el elemento está al final de la lista o no está
            break
    return match


if (
    __name__ == "__main__"
):  # esto hace que si mi programa es ejecutado desde la consola,
    # se ejecute directamente lo que esta aqui dentro
    tamano_linsta = int(input("De que tamano sera la lista: "))
    objetivo = int(input("Que numero quieres encontrar: "))

    lista = [random.randint(0, 100) for i in range(tamano_linsta)]
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f"El objetivo {objetivo} {'esta' if encontrado else 'no esta'} en la lista")
