"""
Napisz program, który utworzy i wypisze listę składającą się z N  liczb z przedziału
[1, 100], a następnie po każdej liczbie pierwszej wstawi nowy element o wartości 0.
Następnie program powinien policzyć sumy podzbiorów znajdujących się pomiędzy zerami.
Lista przed modyfikacją: [7, 45, 45, 34, 53, 45, 4, 3, 11, 18].
Lista po modyfikacji: [7, 0, 45, 45, 34, 53, 0, 45, 4, 3, 0, 11, 0, 18].
Wynik: 7; 177; 52; 11; 18. Wykorzystaj funkcje.
"""

import random


def jest_pierwsza(liczba):
    if liczba < 2:
        return False
    for dzielnik in range(2, int((liczba ** 0.5) + 1)):
        if liczba % dzielnik == 0:
            return False
    return True


def generowanie_listy_nLiczbowej(N):
    generatorLiczb = [
        random.randint(1, 100)
        for _ in range(N)
    ]
    return generatorLiczb


def wstawianie_zera_do_listy(listaLiczbPierwszych):
    for pozycja in range(len(lista) + len(listaLiczbPierwszych)):
        if lista[pozycja] in listaLiczbPierwszych:
            lista.insert(pozycja + 1, 0)
    return lista


def sumowanie_podzbiorow_listy():
    sumyPodzbiorow = []
    sumaLiczb = 0
    for liczba in lista:
        if liczba != 0:
            sumaLiczb += liczba
            # print(sumaLiczb)
        else:
            sumyPodzbiorow.append(sumaLiczb)
            sumaLiczb = 0
    if sumaLiczb != 0:
        sumyPodzbiorow.append(sumaLiczb)

    return sumyPodzbiorow


while True:
    lista = generowanie_listy_nLiczbowej(int(input("Podaj ile liczb ma być w liście z liczbami z zakresu [1, 100]: ")))
    print(f"długość listy: {len(lista)}, lista przed modyfikacji: {lista}")

    listaLiczbPierwszych = []
    for liczba in lista:
        if jest_pierwsza(liczba):
            listaLiczbPierwszych.append(liczba)

    wstawianie_zera_do_listy(listaLiczbPierwszych)  # wywołanie funkcji w celu wstawienia zera do listy
    print(f"długość listy: {len(lista)}, lista po modyfikacją: {lista}")

    # lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 0]  # Jeżeli na końcu jest zero. Co wtedy?

    print(sumowanie_podzbiorow_listy())
