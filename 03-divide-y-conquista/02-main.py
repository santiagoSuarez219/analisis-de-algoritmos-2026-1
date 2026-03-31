def max_subarray_bruteforce(arr):
    max_sum = float("-inf")
    inicio = 0
    fin = 0

    for i in range(len(arr)):
        suma_actual = 0
        for j in range(i, len(arr)):
            suma_actual = suma_actual + arr[j]

            if suma_actual > max_sum:
                max_sum = suma_actual
                inicio = i
                fin = j
    return inicio, fin, max_sum

if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    inicio, fin, max_sum = max_subarray_bruteforce(arr)
    print(f"El subarreglo con la suma máxima es: {arr[inicio:fin+1]} con suma {max_sum}")