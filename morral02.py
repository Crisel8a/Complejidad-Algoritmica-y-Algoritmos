def morral(tamano_morral, pesos, valores, n):
    # Caso base: si no quedan objetos (n == 0) o si el tamaño de la mochila es 0,
    # no se puede agregar nada más, por lo que el valor total es 0.
    if n == 0 or tamano_morral == 0:
        return 0

    # Si el peso del objeto actual (pesos[n - 1]) es mayor que el tamaño disponible
    # de la mochila, no podemos incluir este objeto. Pasamos al siguiente objeto.
    if pesos[n - 1] > tamano_morral:
        print(
            f"No se puede agregar el objeto {n} con peso {pesos[n - 1]} y valor {valores[n - 1]}"
        )
        return morral(tamano_morral, pesos, valores, n - 1)

    # Si el objeto actual puede ser incluido, tenemos dos opciones:
    # 1. Incluir el objeto actual y sumar su valor al resultado.
    # 2. No incluir el objeto actual.
    # Elegimos la opción que nos da el mayor valor total.
    return max(
        valores[n - 1]
        + morral(
            tamano_morral - pesos[n - 1], pesos, valores, n - 1
        ),  # Incluir el objeto
        morral(tamano_morral, pesos, valores, n - 1),  # No incluir el objeto
    )


if __name__ == "__main__":
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 10
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)
