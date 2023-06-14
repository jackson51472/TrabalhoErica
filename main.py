import random
from array import array


def mergeSort(lista):
    if len(lista) > 1:                                      #Verifica se e maior que 1
        mid = len(lista) // 2

        esquerda = lista[:mid]                              #Pega do inicio ate o meio
        direita = lista[mid:]                               #Pega do meio ate o fim

        mergeSort(esquerda)                                 #Passa como parametro a metade esquerda para dividir
        mergeSort(direita)                                  #Passa como parametro a metade direita para dividir

        cont_Esquerda = 0 # Contador da esquerda
        cont_Direita = 0  # Contador da direita
        cont_Lista = 0    # Contador da lista

        while cont_Esquerda < len(esquerda) and cont_Direita < len(direita): # Vai rodar ate que o len(direita) ou
                                                                             # len(esquerda) for menor que o seu contador
            if esquerda[cont_Esquerda] < direita[cont_Direita]:
                lista[cont_Lista] = esquerda[cont_Esquerda] # Substitui o valor caso seja menor
                cont_Esquerda += +1                         # Adiciona mais 1 no contador para comparar o proximo valor da Esquerda
            else:
                lista[cont_Lista] = direita[cont_Direita]   # Substitui o valor caso seja menor
                cont_Direita += 1                           # Adiciona mais 1 no contador para comparar o proximo valor da Direita
            cont_Lista += 1                                 # Adiona mais 1 para subtituir o valor por um certo

        # Essa parte vai acontecr quando um contador não chegou o len final da lista
        # EX: direita = [23,54,77,89]
        #     cont_Direita = 2
        # Nesse caso ele entra no segundo while.
        # Ai ele termina de percorrer a lista/vetor do que tiver faltando


        while cont_Esquerda < len(esquerda):
            lista[cont_Lista] = esquerda[cont_Esquerda]
            cont_Esquerda += 1
            cont_Lista += 1


        # Caso do Exemplo
        while cont_Direita < len(direita):
            lista[cont_Lista] = direita[cont_Direita]
            cont_Direita += 1
            cont_Lista += 1

lista = [32,56,43,11,89,23,77,54]

#lista = [54,26,93,17,77,31,44,55,20]

lista = array("i", (random.randint(0, 20000) for i in range(10000))) #Cria a lista ou  vetor

mergeSort(lista) #Chama a função

print(lista)