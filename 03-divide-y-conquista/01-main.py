def suma(lista):
    if len(lista) == 1:
        return lista[0]
    mitad = len(lista) // 2
    izquierda = suma(lista[:mitad])
    derecha = suma(lista[mitad:])
    return izquierda + derecha

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5]
    resultado = suma(numeros)
    print(f"La suma de {numeros} es: {resultado}")