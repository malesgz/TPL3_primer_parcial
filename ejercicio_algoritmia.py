# Función que compara ambas cadenas de caracteres.
def comparar_cadenas_lexicograficas(cadena1, cadena2):
    if cadena1 < cadena2:
        return -1
    elif cadena2 < cadena1:
        return 1
    else:
        return 0

print(comparar_cadenas_lexicograficas("abc", "abd"))