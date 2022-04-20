# Definição do algoritmo HeapSorte em Python

# Max-Heapify é uma rotina recorrente que garante que um Heap Binário cumpra a propriedade de Heap-Máximo.
# Onde A é o Heap Array, n é o tamanho do Heap e i é o elemento raiz atual do Heap
def MaxHeapify(A, n, i):
	maior = i # Inicializar o maior como o elemento raiz atual
	esq = 2 * i + 1	 # Esquerda = (2*i) +1 #considerando o array inicia como zero
	dir = 2 * i + 2	 # Direita = (2*i + 1) +1 #considerando que o array inicia com zero

	# Verifica se o nó esquerdo existe, e se é maior que o máximo atual
	if esq < n and A[maior] < A[esq]:
		maior = esq #se sim, troca o maior para receber a posição da esquerda

	# Verifica se o nó direito existe, e se é maior que o máximo atual (inclusive que o próprio nó esquerdo)
	if dir < n and A[maior] < A[dir]:
		maior = dir #se sim, troca o maior para receber a posição da direita

	# se houve alteração, troca o nó raiz atual pelo maior identificado
	if maior != i:
		A[i],A[maior] = A[maior],A[i] # operação de troca (swap)

		# Aplica o MáxMaxHeapify no raiz atual, após troca com o raiz inicial i.
		MaxHeapify(A, n, maior)

# Função para ordenação de Heap Binário
def heapSort(A):
	n = len(A) #tamanho do array para chamar a função MaxHeapfy

	# Iniciamos com a inicialização BUILD-MAX-HEAP utilizando a função MaxHeapfy
	for i in range(n // 2 - 1, -1, -1): # operação // para divisão sem resto (piso), iniciando no último nó "não-folha" e decaindo -1 até a posição -1
		MaxHeapify(A, n, i) # roda o algoritmo de forma recorrente, tornando o array um HeapMáximo

	# Extração dos elementos um a um, jogando o maior elemento para o fim do array e decrescendo o tamanho do escopo (i) dentro do MaxHeapify
	for i in range(n-1, 0, -1):
		A[i], A[0] = A[0], A[i] # swap
		MaxHeapify(A, i, 0) # executa sempre com 1 elemento a menos, que já foi ordenado

# Array de entrada
A = [ 3, 5, 13, 5, 6, 7]
heapSort(A)
print ("Array ordenado por HeapSort")
n = len(A)
for i in range(n):
	print (A[i])
