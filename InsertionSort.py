#definição simples do algoritmo InsertionSort em PYTHON

def insertionSort(array, n):
	for i in range(1, n):
		current = array[i]
		j = i - 1
		while j >= 0 and array[j] > current:
			array[j + 1] = array[j]
			j = j - 1
		
		array[j + 1] = current

insertionSort ([10, 5, 16, 3], 4)
