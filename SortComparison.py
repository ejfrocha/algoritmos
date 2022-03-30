#Esta versão utiliza os dois algoritmos e compara seus tempos dentro de um arquivo de saída

# Import OS Module for opening files
import os
# Import Time Module for measuring performance
import time

# Folder with cases
path = "C:\Dev\Python\casos"
# Change the directory
os.chdir(path)

def openCases():

	inputCases = open("num.100000.1.in", "r")
	outputCases = open("outputs.txt", "a")
	
	totalCases = int(inputCases.readline())
	inputArray = inputCases.read()
	
	#Making text array as Integers
	integerInputArray = [int(i) for i in inputArray.split()]
	integerInputArray2 = integerInputArray.copy()
	
	ticInsertion = time.perf_counter()
	insertionSort(integerInputArray, totalCases)
	tacInsertion = time.perf_counter()
	durationInsertion = (ticInsertion - tacInsertion)
	
	print(integerInputArray)
	
	ticSelection = time.perf_counter()
	selectionSort(integerInputArray2, totalCases)
	tacSelection = time.perf_counter()
	durationSelection = (ticSelection - tacSelection)
	
	print(integerInputArray2)
	
	results = 'For #' + str(totalCases) + '\n' + 'Insertion = ' + str(durationInsertion) + ' & ' + 'Selection = ' + str(durationSelection) + ' | Difference of ' + str(durationInsertion - durationSelection)
	outputCases.write(results)
	outputCases.write(':\n')
	
	inputCases.close()
	outputCases.close()


def insertionSort(array, n):
	for i in range(1, n):
		current = array[i]
		j = i - 1
		while j >= 0 and array[j] > current:
			array[j + 1] = array[j]
			j = j - 1
		
		array[j + 1] = current

def selectionSort(array, n):
   
    for i in range(n):
        min = i

        for i in range(i + 1, n):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min]:
                min = i
         
        # put min at the correct position
        (array[i], array[min]) = (array[min], array[i])
	

openCases()
print('Arrays sorted and time printed in the output file')



