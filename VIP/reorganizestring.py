# dada una string s debemos reordenar los caracteres para q dos caracteres iguales no queden juntos
import heapq
from collections import defaultdict


def reorganizar_string(self, S: str) -> str:
    ocurrenciasPorCaracter = defaultdict(int)
    for caracter in S:
        ocurrenciasPorCaracter[caracter] += 1
        if ocurrenciasPorCaracter[caracter] > (len(S) + 1) // 2:
            return ""  # Si algún caracter aparece más de la mitad del tamaño de la string, no es posible reorganizar

        colaProridad = []
        for caracter, ocurrencuas in ocurrenciasPorCaracter.items():
            colaProridad.append(
                (-ocurrencuas, caracter)
            )  # Usamos negativo para simular un max-heap

        heapq.heapify(colaProridad)  # Convertimos la lista en un heap

        stringOrdenada = []

        return "".join(
            stringOrdenada
        )  # Unimos la lista en una string y la retornamos O(1)
