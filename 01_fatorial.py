# ============================================================
# Calcular o fatorial de forma recursiva
# ============================================================

def fatorial(n):
    if n < 0:
        return None                    # número negativo não tem fatorial
    elif n == 0:
        return 1                       # caso base: 0! = 1
    else:
        return n * fatorial(n - 1)     # caso recursivo: n! = n * (n-1)!


print("Fatorial(-2) =", fatorial(-2))
print("Fatorial(0) =", fatorial(0))
print("Fatorial(1) =", fatorial(1))
print("Fatorial(5) =", fatorial(5))
print("Fatorial(7) =", fatorial(7))

