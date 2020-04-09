#----------------------------------------------------
# Median Sort                            
# Implementaçao em Python do Algoritmo Median Sort 
# Presente no livro Algoritmos  O Guia Essencial
# de Heineman, Pollice e Selkow
# Versao 0.1 
# Data 02/07/2018
#-----------------------------------------------------
from util import swap
from util import my_cmp
def sort(A):
    medianSort(A,0,len(A)-1)


def medianSort(A, left, right):
    if left < right:
        #find media value A[me] in A[left,rigth]
        me = find_Media_Value(A,left, right)
        print("ponto médio :i %d valor : %d" %(me,A[me]))
        mid = (right + left)//2
        A[mid],A[me] = swap(A[mid],A[me])
        for i in range(left,mid):
            if A[i] > A[mid]:
                #find A[k]<= A[mid] where k > mid
                k = find_k(A, mid, right)
                print('VALOR K: IND: %d valor %d' %(k , A[k]))
                A[i],A[k] = swap(A[i],A[k])
        print(A)        
        medianSort(A,left, mid -1)
        medianSort(A,mid + 1, right )
#algoritmos proprios:
def find_Media_Value(A,left,right):
    comparador ={}
    soma = 0
    for i in range(left,(right+1):
        for x in range(left,(right+1):
            if x != i:
                if A[i] > A[x]:
                    soma = soma + 1
        comparador.append(i:soma)
        soma = 0
    guarda_y = 0    
    for y in comparador:
        if ((comparador[y]//len(A)) >= 50) and (comparado[y] < comparador[guarda_y]):
            guarda_y = y     
    return (guarda_y)
def find_k(A,mid,right):
    for i in range((mid + 1),(right+1):
        if A[i] < A[mid]: 
            return i        
    return (mid + 1)
#=====
import util

lista_teste = util.gera_lista(10, util.tipo_lista.DECRESCENTE)
print(lista_teste)
sort(lista_teste)
print(lista_teste)