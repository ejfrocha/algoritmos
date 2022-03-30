#definição simples do algoritmo SelectionSort em PYTHON

def selectionSort(array, n):
   
    for i in range(n):
        min = i

        for i in range(i + 1, n):
            if array[i] < array[min]:
                min = i
        (array[i], array[min]) = (array[min], array[i])

insertionSort ([10, 5, 16, 3], 4)
