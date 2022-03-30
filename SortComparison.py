# Import OS Module for opening files
import os
# Import Time Module for measuring performance
import time

# Get all inputs available in the Instancies folder, and run Comparison to the Sort Methods
def loadSortInputs():
	for fileName in os.listdir():
		# Check if file is input (and not output)
		if fileName.endswith(".in"):
			print(fileName)
			#Calls Sort Comparison Function
			compareSorts(fileName)

# Function to execute Insert and Selection sorts, and compare results
def compareSorts(inputFile):
	
	inputCases = open(inputFile, "r")
	outputCases = open(outputFile, "a")
	
	totalCases = int(inputCases.readline())
	print(totalCases)
	inputArray = inputCases.read()
	
	#Making text array as Integers
	integerInputArray = [int(i) for i in inputArray.split()]
	#Making a hard copy of the above Array, so the other funcion can be compared with the same inputs
	integerInputArray2 = integerInputArray.copy()
	
	#Selection Sort with performance counter
	ticSelection = time.perf_counter()
	selectionSort(integerInputArray, totalCases)
	tacSelection = time.perf_counter()
	durationSelection = (ticSelection - tacSelection)
	
	#Insertion Sort with performance counter
	ticInsertion = time.perf_counter()
	insertionSort(integerInputArray2, totalCases)
	tacInsertion = time.perf_counter()
	durationInsertion = (ticInsertion - tacInsertion)

	#Print results into an output file
	results = 'For ' + inputFile + ' with #' + str(totalCases) + '\n' + 'Insertion = ' + str(durationInsertion) + ' & ' + 'Selection = ' + str(durationSelection) + ' | Difference of ' + str(durationInsertion - durationSelection)
	outputCases.write(results)
	outputCases.write(':\n')
	
	inputCases.close()
	outputCases.close()


# Insertion Sort function
def insertionSort(array, n):
	for i in range(1, n):
		current = array[i]
		j = i - 1
		while j >= 0 and array[j] > current:
			array[j + 1] = array[j]
			j = j - 1
		
		array[j + 1] = current

# Selection Sort function
def selectionSort(array, n):
    for current in range(n):
        min = current
        for i in range(current + 1, n):
            if array[i] < array[min]:
                min = i
        (array[current], array[min]) = (array[min], array[current])

# Setting path and names
os.chdir("C:\Dev\Python\casos\instancias")
outputFile = "outputs.txt"

# Renew the Output file
outputCases = open(outputFile, "w")
outputCases.close()

#Load Input Cases
loadSortInputs()

#Conclusion Message
print('Inputs Sorted and Performance Measured into Output file')



