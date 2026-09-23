# ============================================================
# Implementar Palindromo(palavra) de forma recursiva
# ============================================================

def Palindromo(palavra):
    palavra = palavra.lower()                    # padroniza para minúsculas
    if len(palavra) <= 1:
        return True                              # caso base: 0 ou 1 letra é sempre palíndromo
    elif palavra[0] != palavra[-1]:
        return False                             # caso especial: extremos diferentes
    else:
        return Palindromo(palavra[1:-1])         # caso recursivo: remove as pontas e repete


print("arara:", Palindromo("arara"))
print("radar:", Palindromo("radar"))
print("ovo:", Palindromo("ovo"))
print("python:", Palindromo("python"))
print("casa:", Palindromo("casa"))

