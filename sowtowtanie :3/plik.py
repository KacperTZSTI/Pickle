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

#merge:

def scal(lista: list, pomocnicza: list, lewy, srodek, prawy):

    for i in range(lewy, prawy+1):
        pomocnicza[i] = lista[i]

    i = lewy;
    j = srodek + 1
    for k in range(lewy, prawy+1):
        if i <= srodek:
            if j <= prawy:
                if pomocnicza[j] < pomocnicza[i]:
                    lista[k] = pomocnicza[j]
                    j+=1
                else:
                    lista[k] = pomocnicza[i]
                    i+=1
            else:
                lista[k] = pomocnicza[i]
                i+=1
        else:
         
            lista[k] = pomocnicza[j]
            j+=1

def sortowanie_przez_scalanie(lista, pomocnicza, lewy, prawy):
    if lewy < prawy:
        srodek = (prawy + lewy) // 2
        sortowanie_przez_scalanie(lista, pomocnicza, lewy, srodek)
        sortowanie_przez_scalanie(lista, pomocnicza, srodek + 1, prawy)
        scal(lista, pomocnicza, lewy, srodek, prawy)

n = int(input())
lista = []
pomocnicza = n*[0]
for i in range(n): 
    lista.append(int(input()))

sortowanie_przez_scalanie(lista, pomocnicza, 0, n - 1)

for i in range(n):
    print(lista[i])

#wstawianie:

def sortowanie_przez_wstawianie(lista, n):

    for i in range(1, n):
        pom = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > pom:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = pom

n = int(input("Podaj wielość zbioru: "))
lista = []
for i in range(n):
    lista.append(int(input()))
sortowanie_przez_wstawianie(lista, n)
print(*lista)

#kubełkowe:

n = int(input())
p = 2000000000

lista = list(map(int, input().split()))
kubelki = [list() for i in range(len(lista))]

for i in lista:
    kubelki[i // p].append(i)

for i in range(len(kubelki)):
    if len(kubelki[i]) > 1:
        kubelki[i].sort()

for kubelek in kubelki:
    for i in kubelek:
        print(i, end = ' ')

#select:

def sortowanie_przez_selekcje(lista, n):

    for i in range(n):
        mn_index = i
        for j in range(i+1, n):
            if lista[j] < lista[mn_index]:
                mn_index = j

        lista[i], lista[mn_index] = lista[mn_index], lista[i]

n = int(input("Podaj wielość zbioru: "))
lista = []
for i in range(n):
    lista.append(int(input()))
sortowanie_przez_selekcje(lista, n)
print(*lista)