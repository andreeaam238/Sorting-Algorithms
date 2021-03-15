import time

from lists import lists


# Algoritm Insertion Sort

def insertion_sort(array):
    # Se calculeaza lungimea listei.

    length = len(array)

    # Se parcurge lista element cu element.

    for i in range(1, length):

        # Valoarea de referinta.

        refvalue = array[i]

        # Indicele primului element din stanga valorii de referinta.

        j = i - 1

        # Se compara elementul de referinta(refvaue = array[i]) cu fiecare element din stanga sa
        # (array[i - 1] -> array[0]) pana cand se gaseste unul mai mic decat acesta sau se ajunge cu indicele j in afara
        # listei(j = -1 <=> toate elementele din stanga celui de referinta au fost mai mari decat el).

        # Elementele care indeplinesc conditia de mai sus sunt mutate cu o pozitie la dreapta.

        while j >= 0 and array[j] > refvalue:
            array[j + 1] = array[j]
            j += -1

        # Se insereaza elementul de referinta dupa primul element mai mic decat acesta sau la inceputul listei(in cazul
        # in care nu exista un element mai mic decat referinta).

        array[j + 1] = refvalue


def test():
    f = open("insertionsort1.dat", "w")
    for elem in lists:
        start = time.time()
        insertion_sort(elem)
        finish = time.time()
        f.write((len(elem).__str__() + " " + (finish - start).__str__() + "\n"))


test()
