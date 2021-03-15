import time

from lists import lists


# Algoritm Merge Sort

def mergesort(array):

    # Se calculeaza lungimea listei.

    length = len(array)

    # Daca lista nu are macar doua elemente nu avem ce sorta, practic este deja deja sortata.

    if length < 2:
        return

    # Se calculeaza indicele elementului din mijlocul listei.

    middle = int(length / 2)

    # Se separa lista initiala in doua liste:
    #   -> left : elementele de la inceputul listei pana la elementul din mijlocul acesteia inclusiv
    #             (prima jumatate din lista initiala);
    #   -> right : elemenetele de dupa cel din mijlocul listei pana la sfarsitul acesteia
    #              (a doua jumatate din lista initiala).

    left = array[:middle]
    right = array[middle:]

    # Se sorteaza crescator cele doua liste.

    mergesort(left)
    mergesort(right)

    # Se seteaza indicii pentru cele doua liste pe 0(inceputul listelor):
    #   -> i - left
    #   -> j - right

    i = j = 0

    # Se calculeaza lungimea celor doua liste.

    lenleft = len(left)
    lenright = len(right)

    # Se goleste de continut lista initiala.

    array.clear()

    # Se parcurg cele doua liste sortate pana cand se ajunge la sfarsitul uneia dintre ele.

    while i < lenleft and j < lenright:

        # Se compara elementul de pe pozitia i din lista left cu cel de pe pozitia j din lista right.
        # Se insereaza in lista valoarea mai mare dintre cele doua si se incrementeaza indicele pentru lista din care a
        # fost adaugat elementul.

        if left[i] <= right[j]:
            array.append(left[i])
            i += 1
        else:
            array.append(right[j])
            j += 1

    # Se adauga la finalul listei elemenetele ramase in cele doua liste, left si right.
    array.extend(left[i:])
    array.extend(right[j:])


def test():
    f = open("mergesort.dat", "w")

    for elem in lists:
        start = time.perf_counter()
        mergesort(elem)
        finish = time.perf_counter()
        f.write((len(elem).__str__() + " " + (finish - start).__str__() + "\n"))
        print(elem)


test()
