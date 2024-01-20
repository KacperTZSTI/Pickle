#quick:

def quick_sort(lista, lewy, prawy):
    if lewy < prawy:
        i = lewy
        j = prawy

        pivot = lista[(lewy + prawy) // 2]
        while True:
            while pivot > lista[i]:
                i+=1

            while pivot < lista[j]:
                j -= 1

            if i <= j:
                lista[i], lista[j] = lista[j], lista[i]
                i+=1
                j-=1
            else:
                break

        if j > lewy:
            quick_sort(lista, lewy, j)
        if i < prawy:
            quick_sort(lista, i, prawy)

lista = list(map(int, input().split()))
quick_sort(lista, 0, len(lista) - 1)
print(*lista)
