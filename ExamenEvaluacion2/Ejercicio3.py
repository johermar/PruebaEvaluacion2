def magia_numerica(lista_numeros):
    lista_sin_duplicados = list(set(lista_numeros))
    lista_ordenada = sorted(lista_sin_duplicados, reverse=True)
    lista_sin_impares = [num for num in lista_ordenada if num % 2 == 0]
    suma = sum(lista_sin_impares)
    lista_final = [suma] + lista_sin_impares
    return lista_final

# Ejemplo de uso
lista_numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
resultado = magia_numerica(lista_numeros)
print(resultado)
# Verificación
print(resultado[0] == sum(resultado[1:]))