def morral(tamano_morral, pesos, valores, n):
    if n == 0 or tamano_morral == 0:  # caso base, ya esta lleno
        return 0

    if (
        pesos[n - 1] > tamano_morral
    ):  # pesa mas de lo que puede cargar, no se puede incluir
        return morral(
            tamano_morral, pesos, valores, n - 1
        )  # n-1 es prara ver el siguiente elemento de manera recursiva

    else:  # si lo tomo o no q valor me da y elijo el maximo
        return max(
            valores[n - 1]
            + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
            morral(tamano_morral, pesos, valores, n - 1),
        )


if __name__ == "__main__":
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 50
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(
        f"El valor máximo que se puede obtener es: {resultado} en un morral de tamaño {tamano_morral}"
    )
