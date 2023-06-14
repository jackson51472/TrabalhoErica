def func(lista):
    if len(lista) > 1:
        meio_Direita = lista[(len(lista)//2):]
        meio_Esquerda = lista[:(len(lista)//2)]
        print(meio_Esquerda)
        print(meio_Direita)

        func(meio_Esquerda)
        func(meio_Direita)

        pe = 0
        pd = 0
        pl = 0


        while pe < len(meio_Esquerda) and pd < len(meio_Direita):
            if meio_Esquerda[pe] < meio_Direita[pd]:
                lista[pl] = meio_Esquerda[pe]
                pe += +1
            else:
                lista[pl] = meio_Direita[pd]
                pd += 1
            pl += 1


lista = [54,26,93,17,77,31,44,55,20]
func(lista)
print(lista)
