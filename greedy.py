def minimum_coin_change(coins, amount):
    """
    Retorna el número mínimo de monedas y las monedas utilizadas.
    """

    # Guarda resultados ya calculados para evitar repetir trabajo.
    memo = {}

    def auxiliary(remaining):
        # Caso base: ya completamos el cambio.
        if remaining == 0:
            return 0, []

        # Una cantidad negativa no representa una solución válida.
        if remaining < 0:
            return float("inf"), []

        # Reutilizamos el resultado si ya fue calculado.
        if remaining in memo:
            return memo[remaining]

        minimum = float("inf")
        best_combination = []

        # Probamos cada moneda como posible elección.
        for coin in coins:
            quantity, combination = auxiliary(remaining - coin)

            # Si la moneda produjo una solución mejor, la guardamos.
            if quantity != float("inf") and quantity + 1 < minimum:
                minimum = quantity + 1
                best_combination = combination + [coin]

        memo[remaining] = minimum, best_combination
        return memo[remaining]

    return auxiliary(amount)


if __name__ == "__main__":
    coins = [1, 5, 10, 15, 20]
    amount = 27

    result, used_coins = minimum_coin_change(coins, amount)

    print(f"Monedas disponibles: {coins}")
    print(f"Cambio a obtener: {amount}")

    if result == float("inf"):
        print("No se puede hacer el cambio con las monedas dadas.")
    else:
        print(f"Número mínimo de monedas: {result}")
        print(f"Monedas utilizadas: {used_coins}")
