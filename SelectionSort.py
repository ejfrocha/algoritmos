#definição simples do algoritmo SelectionSort em PYTHON

def selectionSort(array, n):
   
    for current in range(n):
        min = current
        for i in range(current + 1, n):
            if array[i] < array[min]:
                min = i
        (array[current], array[min]) = (array[min], array[current])

insertionSort ([10, 5, 16, 3], 4)
