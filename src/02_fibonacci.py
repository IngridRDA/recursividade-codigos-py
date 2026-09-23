# ============================================================
# Implementar F(n) de acordo com a definição por partes
# ============================================================

def F(n):
    if n < 0:
        return 0                        # caso especial: n negativo
    elif n == 0:
        return 1                        # caso base 1
    elif n == 1:
        return 1                        # caso base 2
    else:
        return F(n - 1) + F(n - 2)      # caso recursivo


print("F(-2) =", F(-2))
print("F(0) =", F(0))
print("F(1) =", F(1))
print("F(2) =", F(2))
print("F(5) =", F(5))
print("F(6) =", F(6))

