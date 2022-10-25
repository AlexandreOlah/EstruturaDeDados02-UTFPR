from copy import copy
import time
import sys
from random import randint                                                        #Gerar numeros aleatorios 
#---------------------------------------------------------------------------------
#---------------------------------FUNÇÃO VETOR------------------------------------
#---------------------------------------------------------------------------------
def DefineVetor(TipoVetor, TamanhoVetor: int):
  VetorCriado = []
  if TipoVetor == 'C' or TipoVetor == 'c':                                        #Vetor Crescente
    for i in range(int(TamanhoVetor)):                    
      VetorCriado.append(i+1)                                
  elif TipoVetor == 'D' or TipoVetor == 'd':                                      #Vetor Decrescente
    for j in range(int(TamanhoVetor)):                                                  
      AuxVetor = (int(TamanhoVetor) - j)                                                       #Auxiliar para criar vetor de forma decrescente
      VetorCriado.append(AuxVetor)
  elif TipoVetor == 'R' or TipoVetor == 'r':                                      #Vetor Random
    for k in range(int(TamanhoVetor)):
      #print(k)
      VetorCriado.append(randint(0,99))                                                                                                               
  else:                                                                           #ERRO 
    print('ERRO: Caracter Inválido no Arquivo!')  
    exit()
  #print('----------------------------------------------------------------')
  #print('Vetor Criado:', VetorCriado)
  #print('----------------------------------------------------------------')
  return VetorCriado
#---------------------------------------------------------------------------------
#-------------------------------FIM FUNCAO VETOR----------------------------------
#---------------------------------------------------------------------------------
#-----------------------------FUNÇÃO INSERTION SORT-------------------------------
#---------------------------------------------------------------------------------
def Insertion_Sort(array):
  TempoInicio1 = time.time()
  Cont_Insertion_Sort = 0
  for step in range(1, len(array)):
    key = array[step]
    j = step - 1  
    while j >= 0 and key < array[j]:
      array[j + 1] = array[j]
      j = j - 1
      Cont_Insertion_Sort = Cont_Insertion_Sort + 1                                     #Contador de Comparações
    array[j + 1] = key

  InsertionTime = (time.time() - TempoInicio1)
  print('InsertionnSort:',array,Cont_Insertion_Sort,'comp',InsertionTime,'ms\n')
  return array,Cont_Insertion_Sort,InsertionTime
#---------------------------------------------------------------------------------
#-------------------------------FIM INSERTION SORT--------------------------------
#---------------------------------------------------------------------------------
#----------------------------FUNÇÃO SELECTION SORT--------------------------------
#---------------------------------------------------------------------------------
def Selection_Sort(array):
  TempoInicio2 = 0
  TempoInicio2 = time.time()
  Cont_Selection_Sort = 0
  size = len(array)
  for step in range(size):
    min_idx = step
    for i in range(step + 1, size):
      if array[i] < array[min_idx]:
        min_idx = i
      Cont_Selection_Sort = Cont_Selection_Sort + 1                                     #Contador de Comparações
    (array[step], array[min_idx]) = (array[min_idx], array[step])

  SelectionTime = (time.time() - TempoInicio2)
  print('SelectionSort:',array,Cont_Selection_Sort,'comp',SelectionTime,'ms\n')
  return array,Cont_Selection_Sort,SelectionTime
#---------------------------------------------------------------------------------
#-------------------------------FIM SELECTION SORT--------------------------------
#---------------------------------------------------------------------------------
#------------------------------FUNÇÃO BUBBLE SORT---------------------------------
#---------------------------------------------------------------------------------
def Bubble_Sort(array):                                                           #Declarando a função "Bubble_Sort" que recebe um vetor de elementos e um valor para ordenar em ordem crescente ou decrescente  
  TempoInicio3 = 0
  TempoInicio3 = time.time()
  Cont_Bubble_Sort = 0
  for i in range(len(array)):                                                     #Percorre cada elemento do vetor     
    Troca = False                                                                 #Declarando Troca como false para ordenar o vetor
    for j in range(0, len(array) - i - 1):                                        #Loop para comparar os elementos
      if (array[j] > array[j + 1]):                                               #Compara dois elementos vizinhos (adjacentes), prevalece forma crescente
        array[j],array[j+1] = array[j+1],array[j]                                 #A,B = B,A     
        Troca = True                                                              #Troca = True
      Cont_Bubble_Sort = Cont_Bubble_Sort + 1                                     #Contador de Comparações
    if not Troca:                                                                 #Se não ha trocas significa que esta ordenado
      break                                                                       #Para Programa]

  BubbleTime = (time.time() - TempoInicio3)
  print('bubbleSort:',array,Cont_Bubble_Sort,'comp',BubbleTime,'ms\n')
  return array,Cont_Bubble_Sort,BubbleTime
#---------------------------------------------------------------------------------
#-------------------------------FIM BUBBLE SORT-----------------------------------
#---------------------------------------------------------------------------------
#------------------------------FUNÇÃO MERGE SORT----------------------------------
#---------------------------------------------------------------------------------
def Merge_Sort(array):
  TempoInicio4 = 0
  TempoInicio4 = time.time()
  Cont_Merge_Sort = 0
  if len(array) > 1:
    r = len(array)//2
    L = array[:r]
    M = array[r:]

    Merge_Sort(L)
    Merge_Sort(M)

    i = j = k = 0

    while i < len(L) and j < len(M):
      if L[i] < M[j]:
        array[k] = L[i]
        i += 1
      else:
        array[k] = M[j]
        j += 1
      k += 1
      Cont_Merge_Sort = Cont_Merge_Sort + 1                                     #Contador de Comparações

    while i < len(L):
      array[k] = L[i]
      i += 1
      k += 1
      Cont_Merge_Sort = Cont_Merge_Sort + 1                                     #Contador de Comparações

    while j < len(M):
      array[k] = M[j]
      j += 1
      k += 1                                                                  #Para Programa
      Cont_Merge_Sort = Cont_Merge_Sort + 1                                     #Contador de Comparações

  #print('MergeSort:',array,Cont_Merge_Sort,'comp',(time.time() - TempoInicio4),'ms\n')
  return Cont_Merge_Sort,(time.time() - TempoInicio4)
#---------------------------------------------------------------------------------
#-------------------------------FIM MERGE SORT------------------------------------
#---------------------------------------------------------------------------------
#------------------------------FUNÇÃO QUICK SORT----------------------------------
#---------------------------------------------------------------------------------
def partition(array, low, high):
  pivot = array[high]
  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return (i + 1)

# function to perform quicksort
def Quick_Sort(array, low, high, ContadorQuick):
  TempoInicio5 = 0
  TempoInicio5 = time.time()
  
  #low = 0
  #high = len(array) - 1

  if low < high:
    pi= partition(array, low, high)
    ContadorQuick = 1 + ContadorQuick 
    Quick_Sort(array, low, pi - 1, ContadorQuick)
    Quick_Sort(array, pi + 1, high, ContadorQuick)

  #print('QuickSort:',array,Cont_Quick_Sort,'comp',(time.time() - TempoInicio5),'ms\n')
  return (time.time() - TempoInicio5)
#---------------------------------------------------------------------------------
#-------------------------------FIM QUICK SORT------------------------------------
#---------------------------------------------------------------------------------
#------------------------------FUNÇÃO HEAP SORT-----------------------------------
#---------------------------------------------------------------------------------
def heapify(array, n, i):
  largest = i
  l = 2 * i + 1
  r = 2 * i + 2 
  Cont = 0
  if l < n and array[i] < array[l]:
    largest = l
    Cont = Cont + 1                                     #Contador de Comparações
  if r < n and array[largest] < array[r]:
    largest = r
    Cont = Cont + 1                                     #Contador de Comparações
  if largest != i:
    array[i], array[largest] = array[largest], array[i]
    Cont = Cont + 1                                     #Contador de Comparações
    heapify(array, n, largest)
  return Cont

  
def Heap_Sort(array):
  TempoInicio6 = 0
  TempoInicio6 = time.time()
  Cont_Heap_Sort = 0
  n = len(array)
  for i in range(n//2 -1, -1, -1):
    #heapify(array, n, i) 
    Cont_Heap_Sort = heapify(array, n, i)+ Cont_Heap_Sort
  for i in range(n-1, 0, -1):
    array[i], array[0] = array[0], array[i]
    #heapify(array, i, 0)       
    Cont_Heap_Sort = heapify(array, i, 0) + Cont_Heap_Sort

  #print('HeapSort:',array,Cont_Heap_Sort,'comp',(time.time() - TempoInicio6),'ms\n')
  return Cont_Heap_Sort,(time.time() - TempoInicio6)
#---------------------------------------------------------------------------------
#-------------------------------FIM HEAP SORT-------------------------------------
#---------------------------------------------------------------------------------

#VetorDeElementos = [11, -41, 38, -86, -55, -95,  7, 28, -70, 31, 19, -66, 43, -67, 45]
#VetorDeElementos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Ordena_Cre_Dec   = input('Escolha uma das opções:\n1 - Crescente.\n2 - Decrescente.\n')

Entrada = open(sys.argv[1],'r')
Entrada.seek(0,0)                                                                    #Cursor no inicio do arquivo

ArquivoVetorTamanho = (Entrada.readline()).replace('\n', '')  
if (ArquivoVetorTamanho == ''):                                                      #Verifica se o arquivo esta vazio
  print('ERRO: Arquivo Vazio!')
  exit()
if ((ArquivoVetorTamanho.isnumeric()) != True):                                      #Verifica se é numero
  print('ERRO: Tamanho do Vetor deve ser numero!')    
  exit()
ArquivoVetorOrdena  = (Entrada.readline()).replace('\n', '')
#print(ArquivoVetorTamanho) 
#print(ArquivoVetorOrdena)

Entrada.close()

#Passar tamanho do vetor para função DefineVetor
#Passar como ordenar para função DefineVetor
VetorDeElementos = DefineVetor(ArquivoVetorOrdena, ArquivoVetorTamanho)
print('Vetor de Elemnetos:',VetorDeElementos)

#O Vetor retornado deve passar por todos os tipos de ordenações
VetorOrdenadoInsertionSort, ContadorInsertionSort, TempoInsertionSort = (Insertion_Sort(copy(VetorDeElementos)))
VetorOrdenadoSelectionSort, ContadorSelectionSort, TempoSelectionSort = (Selection_Sort(copy(VetorDeElementos)))
VetorOrdenadoBubbleSort, ContadorBubbleSort, TempoBubbleSort = (Bubble_Sort(copy(VetorDeElementos)))
VetorMerge = copy(VetorDeElementos)
ContadorMergeSort, TempoMergeSort = (Merge_Sort(VetorMerge))
print('MergeSort:',VetorMerge,ContadorMergeSort,'comp',TempoMergeSort,'ms\n')
VetorQuick = copy(VetorDeElementos)
ContadorQuickSort = 0
TempoQuickSort = (Quick_Sort(VetorQuick, 0, len(VetorQuick)-1, ContadorQuickSort))
print('QuickSort:',VetorQuick,ContadorQuickSort,'comp',TempoQuickSort,'ms\n')
VetorHeap = copy(VetorDeElementos)
ContadorHeapSort, TempoHeapSort = (Heap_Sort(VetorHeap))
print('HeapSort:',VetorHeap,ContadorHeapSort,'comp',TempoQuickSort,'ms\n')

#Escrever no arquivo de saida cada Ordenação 
Saida = open(sys.argv[2],'w')
Saida.seek(0,0)                                                                    #Cursor no inicio do arquivo

#Saidas InsertionSort
Saida.write('insertionSort: ')
Saida.write(((str(VetorOrdenadoInsertionSort).replace(',','')).replace('[','')).replace(']',''))
Saida.write(', ')
Saida.write(str(ContadorInsertionSort))
Saida.write(' comp, ')
Saida.write(str(TempoInsertionSort))
Saida.write(' ms\n')
#Saidas SelectionSort
Saida.write('selectionSort: ')
Saida.write(((str(VetorOrdenadoSelectionSort).replace(',','')).replace('[','')).replace(']',''))
Saida.write(', ')
Saida.write(str(ContadorSelectionSort))
Saida.write(' comp, ')
Saida.write(str(TempoSelectionSort))
Saida.write(' ms\n')
#Saidas BubbleSort
Saida.write('bubbleSort: ')
Saida.write(((str(VetorOrdenadoBubbleSort).replace(',','')).replace('[','')).replace(']',''))
Saida.write(', ')
Saida.write(str(ContadorBubbleSort))
Saida.write(' comp, ')
Saida.write(str(TempoBubbleSort))
Saida.write(' ms\n')
#Saidas MergeSort
Saida.write('mergeSort: ')
Saida.write(((str(VetorMerge).replace(',','')).replace('[','')).replace(']',''))
Saida.write(', ')
Saida.write(str(ContadorMergeSort))
Saida.write(' comp, ')
Saida.write(str(TempoMergeSort))
Saida.write(' ms\n')
#Saidas QuickSort
Saida.write('quickSort: ')
Saida.write(((str(VetorQuick).replace(',','')).replace('[','')).replace(']',''))
Saida.write(', ')
Saida.write(str(ContadorQuickSort))
Saida.write(' comp, ')
Saida.write(str(TempoQuickSort))
Saida.write(' ms\n')
#Saidas HeapSort
Saida.write('heapSort: ')
Saida.write(((str(VetorHeap).replace(',','')).replace('[','')).replace(']',''))
Saida.write(', ')
Saida.write(str(ContadorHeapSort))
Saida.write(' comp, ')
Saida.write(str(TempoHeapSort))
#Saida.write(' ms\n')


Saida.close()