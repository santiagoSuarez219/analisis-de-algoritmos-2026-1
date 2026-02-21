import time
import random

# Algoritmo de ordenamiento por inserción
def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr

# Algoritmo de ordenamiento por mezcla (merge sort)
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def medir_tiempo(n):
    arr = list(range(n))
    random.shuffle(arr)

    arr1 = arr.copy()

    inicio = time.time()
    insertion_sort(arr)
    fin = time.time()

    inicio2 = time.time()
    merge_sort(arr1)
    fin2 = time.time()

    print(f"Insertion Sort: {fin - inicio:.6f} segundos")
    print(f"Merge Sort: {fin2 - inicio2:.6f} segundos")

    
if __name__ == "__main__":
    for n in [100, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]:
        medir_tiempo(n)

