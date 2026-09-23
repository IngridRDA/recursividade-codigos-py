# ============================================================
# Implementar ContaOcorrencia(vet, elemento) de forma recursiva
# ============================================================

def ContaOcorrencia(vet, elemento):
    if len(vet) == 0:
        return 0                                  # caso base: vetor vazio, nenhuma ocorrência
    elif vet[0] == elemento:
        return 1 + ContaOcorrencia(vet[1:], elemento)  # encontrou: soma 1 e continua no resto
    else:
        return ContaOcorrencia(vet[1:], elemento)      # não encontrou: continua no resto


print("2 em [1, 2, 3, 2, 4, 2] =", ContaOcorrencia([1, 2, 3, 2, 4, 2], 2))
print("5 em [5, 5, 5, 7, 8] =", ContaOcorrencia([5, 5, 5, 7, 8], 5))
print("6 em [1, 2, 3, 4, 5] =", ContaOcorrencia([1, 2, 3, 4, 5], 6))
print("10 em [10, 20, 10, 30, 10] =", ContaOcorrencia([10, 20, 10, 30, 10], 10))

