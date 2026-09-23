# ============================================================
# Implementar SomaLista(lista) de forma recursiva
# ============================================================

def SomaLista(lista):
    if len(lista) == 0:
        return 0                              # caso base: lista vazia, soma é 0
    else:
        return lista[0] + SomaLista(lista[1:])  # caso recursivo: primeiro elemento + soma do resto


print("Soma [1, 3, 5, 7, 9] =", SomaLista([1, 3, 5, 7, 9]))
print("Soma [2, 4, 6] =", SomaLista([2, 4, 6]))
print("Soma [10, 20, 30] =", SomaLista([10, 20, 30]))
print("Soma [] =", SomaLista([]))

